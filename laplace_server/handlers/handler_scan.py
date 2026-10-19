# libraries
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from laplace_server import ServerLHC

import logging

# project
from ..protocol import (
    CMD_SCAN, LOGGER_NAME,
    make_scan_reply, 
)

log = logging.getLogger(LOGGER_NAME)


def handle_scan(server: ServerLHC, message: dict, target: str) -> None:
    log.info(f"[Server {server.name}] Received: '{CMD_SCAN}' from '{target}'.")

    data = message
    server.emit("on_scan", data)
    
    server.socket.send_json(
        make_scan_reply(
            sender=server.name, 
            target=target
        )
    )