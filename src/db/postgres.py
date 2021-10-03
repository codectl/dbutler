import os

import click
from psycopg2 import connect, extensions, sql

from src.cli import dbutler


@dbutler.group()
@click.option('-h', '--host')
@click.option('-p', '--port')
@click.option('-d', '--database')
@click.option('-u', '--user')
@click.option('-p', '--password')
@click.pass_context
def postgres(ctx, host, port, database, user, password):
    """Operations for a postgres database."""
    ctx.ensure_object(dict)
    ctx.obj['host'] = host or os.getenv('PGHOST', 'localhost')
    ctx.obj['port'] = port or os.getenv('PGPORT', 5432)
    ctx.obj['database'] = database or os.getenv('PGDATABASE', 'postgres')
    ctx.obj['user'] = user or os.getenv('PGUSER', 'postgres')
    ctx.obj['password'] = password or os.getenv('PGPASSWORD')


@postgres.group()
@click.pass_context
def create(ctx):
    """Create postgres resources."""
    ctx.ensure_object(dict)


@create.command(name='database')
@click.argument('database')
@click.pass_context
def database_command(ctx, database):
    """Create postgres database."""
    ctx.ensure_object(dict)
    exec_query(ctx, query=f"CREATE DATABASE {sql.Identifier(database)}")


@create.command(name='user')
def user_command():
    """Create postgres user."""
    pass


def exec_query(ctx, query=''):
    """Execute an postgres sql query."""
    conn = connect(
        host=ctx.obj['host'],
        port=ctx.obj['port'],
        database=ctx.obj['database'],
        user=ctx.obj['user'],
        password=ctx.obj['password']
    )

    # set the isolation level for autocommit
    conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    # instantiate a cursor object from the connection
    cursor = conn.cursor()

    # use the sql module to avoid SQL injection attacks
    cursor.execute(sql.SQL(query))

    print(f"Executed query: {query}")

    cursor.close()
    conn.close()
