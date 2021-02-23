import os

import click


@click.group(name="node")
@click.pass_context
def node(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('No such sub command %s' % ctx)


@node.command(name="get")
def get():
    os.system("kubectl get nodes")
