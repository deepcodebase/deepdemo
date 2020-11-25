import argparse
import os
import subprocess

from demo.server.app import app


def launch_api_server(args):
    app.run(host="0.0.0.0", port=args.port)


def launch_client(args):
    os.chdir('demo/client')
    command = 'yarn serve --port {}'.format(args.port)
    subprocess.call(command, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="The core script of experiment management."
    )
    subparsers = parser.add_subparsers(dest="command")

    parser_s = subparsers.add_parser("launch_server", description="Launch api server.")
    parser_s.add_argument("--port", default=9000, type=int)

    parser_c = subparsers.add_parser(
        'launch_client', description='Launch client user interface.')
    parser_c.add_argument(
        '--port', default=8080, type=int)

    args = parser.parse_args()

    if args.command == "launch_server":
        launch_api_server(args)
    elif args.command == 'launch_client':
        launch_client(args)
    else:
        pass
