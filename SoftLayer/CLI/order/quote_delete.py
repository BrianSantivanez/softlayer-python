"""Delete the quote of an order"""
# :license: MIT, see LICENSE for more details.
import click

from SoftLayer.CLI.command import SLCommand as SLCommand
from SoftLayer.CLI import environment
from SoftLayer.managers import ordering


@click.command(cls=SLCommand)
@click.argument('identifier')
@environment.pass_env
def cli(env, identifier):
    """View a quote"""

    manager = ordering.OrderingManager(env.client)
    result = manager.delete_quote(identifier)

    if result:
        env.fout("Quote id: {} was deleted.".format(identifier))