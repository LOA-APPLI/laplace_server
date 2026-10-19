
# Libraries
import socket as sock  # Rename to avoid conflict with ZMQ
import logging

from .protocol import LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)


def get_ip(name: str) -> str:
    """Return the local IPv4 address selected by the routing table."""
    s = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)

    try:
        # Determine the local IP address used for outbound traffic.
        s.connect(("8.8.8.8", 80))
        addr = s.getsockname()[0]

        log.debug(
            f"[Server {name}] IPv4 address determined using "
            f"the UDP socket method: {addr}"
        )
        return addr

    except OSError as e:
        log.warning(
            f"[Server {name}] Could not determine the IPv4 address "
            f"using the UDP socket method "
            f"(possibly offline or without a default route): {e}"
        )

    finally:
        s.close()

    try:
        # Resolve the local hostname to an IPv4 address.
        hostname = sock.gethostname()
        addr = sock.gethostbyname(hostname)

        log.debug(
            f"[Server {name}] IPv4 address determined using "
            f"the local hostname resolution method "
            f"(gethostname + gethostbyname): {addr}"
        )
        return addr

    except OSError as e:
        log.error(
            f"[Server {name}] Could not determine the IPv4 address "
            f"using the local hostname resolution method: {e}. "
            f"Returning 0.0.0.0 as a fallback."
        )
        return "0.0.0.0"
