# libraries
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from laplace_server import ServerLHC

import logging

# project
from ..protocol import (
    CMD_SET_ACT, LOGGER_NAME,
    make_scan_reply, make_error, 
)
from ..validations import validate_payload

log = logging.getLogger(LOGGER_NAME)


def handle_set_actuators(server: ServerLHC, message: dict, target: str) -> None:
    log.debug(f"[Server {server.name}] Received: '{CMD_SET_ACT}' from '{target}'")
    err = validate_payload(message, expected_keys=["actuators"])
    if err:
        server.socket.send_json(
            make_error(
                sender=server.name, 
                target=target, 
                cmd=CMD_SET_ACT, 
                error_msg=err
            )
        )
        return
    
    actuators = message["payload"]["actuators"]
    server.emit("on_set_actuators", actuators)
    
    server.socket.send_json(
        make_scan_reply(
            sender=server.name, 
            target=target
        )
    )