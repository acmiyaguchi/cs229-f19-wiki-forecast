from . import sample, summarize
import click


@click.group()
def subgraph():
    pass


subgraph.add_command(sample.sample_subgraph, "sample")
subgraph.add_command(summarize.summarize_graph, "summarize-graph")
