import os

import click


@click.group(name="pd")
@click.pass_context
def pod(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('No such sub command %s' % ctx)


@pod.command(name="list")
@click.option("--all", "-a", is_flag=True)
@click.option("--output", "-o", type=click.Choice(["json", "yaml", "wide"]))
def list(all, output):
    if all:
        if not output:
            os.system("kubectl get pod --all-namespaces")
        else:
            os.system("kubectl get pod --all-namespaces -o %s" % output)
    else:
        if not output:
            os.system("kubectl get pod")
        else:
            os.system("kubectl get pod -o %s" % output)


@pod.command(name="get")
@click.option("--ip")
@click.option("--name")
@click.option("--node")
def get(ip, name, node):
    if isinstance(ip, str) and len(ip) > 0:
        os.system("kubectl get pod --all-namespaces --field-selector=\"status.podIP=%s\" -o wide" % ip)
    if isinstance(name, str) and len(name) > 0:
        pass
        # os.system("kubectl get pod --all-namespaces --field-selector=\"spec.nodeName=%s\" -o wide" % name)
    if isinstance(node, str) and len(node) > 0:
        os.system("kubectl get pod --all-namespaces --field-selector=\"spec.nodeName=%s\" -o wide" % node)
