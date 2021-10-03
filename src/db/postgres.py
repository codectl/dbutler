from src.cli import dbutler


@dbutler.group()
def postgres():
    """Operations for a postgres database."""
    pass


@postgres.group()
def create():
    """Create postgres resources."""
    pass


@create.group()
def database():
    """Create postgres database."""
    pass


@create.group()
def user():
    """Create postgres user."""
    pass
