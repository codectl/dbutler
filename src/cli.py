import click


@click.group()
def dbutler():
    """Database utility manager for different databases."""
    pass


@dbutler.group()
def postgres():
    """Operations for a postgres database."""
    pass
