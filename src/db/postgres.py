from src.cli import postgres


@postgres.command()
def create():
    print('create')
