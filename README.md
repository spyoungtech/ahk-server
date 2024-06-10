# ahk-server

A server to allow remote execution of AutoHotkey using the Python [ahk](https://github.com/spyoungtech/ahk) wrapper.
Uses fastapi.


## Installation

```bash
pip install ahk-server
```

Requires you have AutoHotkey installed. See [ahk readme](https://github.com/spyoungtech/ahk) for non-python dependencies.

## Usage

To start the server:

```bash
python -m ahk_server
```
This accepts two optional command line parameters: `--host` and `--port`. Alternatively, you can also configure the host
and port by setting the environment variables `AHK_SERVER_HOST` and `AHK_SERVER_PORT`.

Alternatively still, you can also invoke the server using `uvicorn`
```bash
uvicorn ahk_server.app:app
```

## Standalone release

`ahk-server` is also available in a standalone exe release which can be found in the [releases page](https://github.com/spyoungtech/ahk-server/releases)

For connecting to the server, see the client project: [ahk-client](https://github.com/spyoungtech/ahk-client).


## Status

This project (and its client counterpart) is usable, but in **very** early stages of development.
Notably, it does not currently include any authentication mechanisms for securing server connections, so use with caution.


TODO:

A noninclusive list of things that might come in the future:

- [ ] support some kind of basic authentication
- [ ] implement `run_script` functionality
- [ ] implement non-blocking functionality
- [ ] implement extension negotiation with clients
