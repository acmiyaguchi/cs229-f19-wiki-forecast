from . import sample, summarize, pageview
import click


@click.group()
def subgraph():
    pass


subgraph.add_command(sample.sample_subgraph, "sample")
subgraph.add_command(pageview.main, "pageview")
subgraph.add_command(summarize.summarize_graph, "summarize-graph")
subgraph.add_command(summarize.summarize_pageview, "summarize-pageview")
