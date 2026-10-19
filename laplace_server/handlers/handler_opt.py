# libraries
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from laplace_server import ServerLHC

import logging

# project
from ..protocol import (
    CMD_OPT, LOGGER_NAME,
    make_opt_reply, make_error, 
)
from ..validations import validate_payload

log = logging.getLogger(LOGGER_NAME)


def handle_opt(server: ServerLHC, message: dict, target: str) -> None:
    log.info(f"[Server {server.name}] Received: '{CMD_OPT}' from '{target}'.")
    err = validate_payload(message, expected_keys=["data"])
    if err:
        server.socket.send_json(
            make_error(
                sender=server.name, 
                target=target, 
                cmd=CMD_OPT, 
                error_msg=err
            )
        )
        return
    
    data = message["payload"]["data"]
    server.emit("on_opt", data)
    
    server.socket.send_json(
        make_opt_reply(
            sender=server.name, 
            target=target
        )
    )