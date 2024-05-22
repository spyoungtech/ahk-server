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
uvicorn ahk_server.app:app
```

For the client project, see: [ahk-client](https://github.com/spyoungtech/ahk-client).


## Status

This project (and its client counterpart) is usable, but in **very** early stages of development. 
Notably, it does not currently include any authentication mechanisms for securing server connections, so use with caution.


TODO:

A noninclusive list of things that might come in the future:

- [ ] support some kind of basic authentication
- [ ] implement `run_script` functionality
- [ ] implement non-blocking functionality
- [ ] implement extension negotiation with clients
