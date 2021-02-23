import os

import click


@click.group(name="nd")
@click.pass_context
def node(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('No such sub command %s' % ctx)


@node.command(name="list")
@click.option("--all", "-a", is_flag=True)
@click.option("--output", "-o", type=click.Choice(["json", "yaml", "wide"]))
def list(all, output):
    if all:
        if not output:
            os.system("kubectl get node --all-namespaces")
        else:
            os.system("kubectl get node --all-namespaces -o %s" % output)
    else:
        if not output:
            os.system("kubectl get node")
        else:
            os.system("kubectl get node -o %s" % output)


@node.command(name="get")
@click.option("--name", "-n")
def get(name: str):
    os.system("kubectl describe node %s" % name)
