'''
LAPLACE-HC server package.

Provides a ZMQ-based server, protocol definitions, 
validation utilities, handlers, and PyQt6 signal controller.
'''
# libraries
from importlib.metadata import version, PackageNotFoundError
from .server_lhc import ServerLHC

try:
    __version__ = version("laplace-server")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = [
    "__version__",
    "ServerLHC",
]

