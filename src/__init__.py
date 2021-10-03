__version_info__ = (0, 0, 1)
__version__ = '.'.join(str(c) for c in __version_info__)

from src.cli import dbutler
from src.db.postgres import postgres


def entrypoint():
    """Package entrypoint."""
    dbutler()
