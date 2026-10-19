# libraries
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from laplace_server import ServerLHC

import logging

# project
from ..protocol import make_stop_reply, CMD_STOP, LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)


def handle_stop(server: ServerLHC, message: dict, target: str) -> None:
    log.info(f"[Server {server.name}] Received: '{CMD_STOP}' from '{target}'.")
    server._running.clear()     # stop the thread
    server.socket.send_json(
        make_stop_reply(
            sender=server.name, 
            target=target
        )
    )