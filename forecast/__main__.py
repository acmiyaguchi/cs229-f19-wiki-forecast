import click
from forecast import extract


@click.group()
def cli():
    pass


cli.add_command(extract.extract_subgraph)
cli.add_command(extract.subgraph_statistics)

if __name__ == "__main__":
    cli()
