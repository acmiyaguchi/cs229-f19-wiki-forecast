import click
from .subgraph.cli import subgraph
from .poisson import main as poisson


@click.group()
def cli():
    pass


cli.add_command(subgraph)
cli.add_command(poisson, "poisson")


if __name__ == "__main__":
    cli()
