import click

from .baseline import main as baseline
from .poisson import main as poisson
from .subgraph.cli import subgraph


@click.group()
def cli():
    pass


cli.add_command(subgraph)
cli.add_command(poisson, "poisson")
cli.add_command(baseline, "baseline")


if __name__ == "__main__":
    cli()
