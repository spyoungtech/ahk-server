import argparse
import os
import sys

import uvicorn

from ahk_server.app import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser('ahk-server')
    parser.add_argument('--host')
    parser.add_argument('--port')

    args = parser.parse_args()

    env_host = os.environ.get('AHK_SERVER_HOST', '127.0.0.1')
    env_port = os.environ.get('AHK_SERVER_PORT', '8000')

    host = args.host or env_host
    port = args.port or env_port
    try:
        uvicorn.run(app, host=host, port=int(port))
    except KeyboardInterrupt:
        sys.exit(0)
