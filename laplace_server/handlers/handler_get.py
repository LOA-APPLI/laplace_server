# libraries
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from laplace_server import ServerLHC

import logging

# project
from ..protocol import make_get_reply, CMD_GET, LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)


def handle_get(server: ServerLHC, message: dict, target: str) -> None:
    log.debug(f"[Server {server.name}] Received: '{CMD_GET}' from '{target}'.")
    server.emit("on_get")
    server.socket.send_json(
        make_get_reply(
            sender=server.name, 
            target=target, 
            data=server.data
        )
    )
    if server.empty_data_after_get:
        server.empty_data()
