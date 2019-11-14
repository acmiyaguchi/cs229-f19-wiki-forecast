import click
from .subgraph.cli import subgraph


@click.group()
def cli():
    pass


cli.add_command(subgraph)

if __name__ == "__main__":
    cli()
