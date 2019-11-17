import click

from .baseline import main as baseline
from .baseline_random import main as baseline_random
from .poisson import main as poisson
from .subgraph.cli import subgraph


@click.group()
def cli():
    pass


cli.add_command(subgraph)
cli.add_command(poisson, "poisson")
cli.add_command(baseline, "baseline")
cli.add_command(baseline_random, "baseline-random")


if __name__ == "__main__":
    cli()
