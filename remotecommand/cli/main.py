import logging
import argparse

from remotecommand.cli.remotecommad import RemoteCommand

log = logging.getLogger(__name__)


def main(args=None):

    parser = argparse.ArgumentParser(prog='remotecommand', description='Command line interface')

    parser.add_argument(
        '-H','--host', default='127.0.0.1', help='serveur host'
    )
    parser.add_argument(
       '-P', '--port', default='12345', help='port host'
    )
    parser.add_argument(
        '--loglevel', default='info', help='Log level',
        choices=['debug', 'info', 'warning', 'error', 'critical'],
    )

    # Parse all command line arguments
    args = parser.parse_args(args)
    if (args.__contains__(help)):
        # Affichage de l'aide
        parser.print_help()
    else:
        return RemoteCommand(args.host, args.port, args.loglevel)
        
    

 
