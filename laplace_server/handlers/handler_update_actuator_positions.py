# libraries
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from laplace_server import ServerLHC

import logging

# project
from ..protocol import (
    CMD_UPDATE_ACTUATORS_POS, LOGGER_NAME,
    make_scan_reply, make_error, 
)

log = logging.getLogger(LOGGER_NAME)


def handle_update_actuator_positions(server: ServerLHC, message: dict, target: str) -> None:
    log.info(f"[Server {server.name}] Received: '{CMD_UPDATE_ACTUATORS_POS}' from '{target}'")
    server.emit("on_set_actuators", message)
    server.socket.send_json(
        make_scan_reply(
            sender=server.name, 
            target=target
        )
    )