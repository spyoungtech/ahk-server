from io import BytesIO
from typing import Any
from typing import Optional

from ahk import AsyncAHK
from ahk._async.transport import AsyncDaemonProcessTransport
from ahk.exceptions import AHKProtocolError
from ahk.message import RequestMessage
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response


class BytesTransport(AsyncDaemonProcessTransport):
    async def send(self, request: RequestMessage, engine: Optional[AsyncAHK[Any]] = None) -> bytes:
        msg = request.format()
        assert self._proc is not None
        async with self.lock:
            self._proc.write(msg)
            await self._proc.adrain_stdin()
            tom = await self._proc.readline()
            num_lines = await self._proc.readline()
            content_buffer = BytesIO()
            content_buffer.write(tom)
            content_buffer.write(num_lines)
            try:
                lines_to_read = int(num_lines) + 1
            except ValueError as e:
                try:
                    stdout = tom + num_lines + await self._proc.read()
                except Exception:
                    stdout = b''
                raise AHKProtocolError(
                    'Unexpected data received. This is usually the result of an unhandled error in the AHK process'
                    + (f': {stdout!r}' if stdout else '')
                ) from e
            for _ in range(lines_to_read):
                part = await self._proc.readline()
                content_buffer.write(part)
            content = content_buffer.getvalue()[:-1]
            return content


app = FastAPI()

ahk = AsyncAHK(TransportClass=BytesTransport)


@app.post('/{method}')
async def call_method(request: Request, method: str):
    args = await request.json()
    message: bytes = await ahk.function_call(method, args, blocking=True)
    return Response(message)


@app.get('/version')
async def version():
    version = await ahk.get_major_version()
    return {'version': version}
