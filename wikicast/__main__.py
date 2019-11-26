import click

from . import baseline, baseline_random, poisson, pipeline, bipartition
from .subgraph.cli import subgraph


@click.group()
def cli():
    pass


cli.add_command(subgraph)
cli.add_command(poisson.main, "poisson")
cli.add_command(baseline.main, "baseline")
cli.add_command(baseline_random.main, "baseline-random")
cli.add_command(pipeline.main, "pipeline")
cli.add_command(bipartition.main, "bipartition")


if __name__ == "__main__":
    cli()
