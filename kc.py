import click
from pod import pod
from node import node


@click.group()
@click.pass_context
def cli(ctx):
    pass


cli.add_command(node)
cli.add_command(pod)

if __name__ == '__main__':
    cli()
