# libraries
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from laplace_server import ServerLHC

import logging

# project
from ..protocol import make_pong, CMD_PING, LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)


def handle_ping(server: ServerLHC, message: dict, target: str) -> None:
    log.debug(f"[Server {server.name}] Received: '{CMD_PING}' from '{target}'.")
    server.socket.send_json(
        make_pong(
            sender=server.name, 
            target=target
        )
    )