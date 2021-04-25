import argparse
import os
import subprocess

from app import app


def launch_api_server(args):
    with open('client/.env.local', 'w') as f:
        f.write(f'VUE_APP_API_PORT={args.port}')
    app.run(host="0.0.0.0", port=args.port)


def launch_ui_server(args):
    os.chdir('client')
    command = 'yarn serve --port {}'.format(args.port)
    subprocess.call(command, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The core script of demo.")
    subparsers = parser.add_subparsers(dest="command")

    parser_s = subparsers.add_parser(
        "serve_api", description="Launch api server.")
    parser_s.add_argument("--port", default=9000, type=int)

    parser_c = subparsers.add_parser(
        'serve_ui', description='Launch user interface.')
    parser_c.add_argument('--port', default=8080, type=int)

    args = parser.parse_args()

    if args.command == "serve_api":
        launch_api_server(args)
    elif args.command == 'serve_ui':
        launch_ui_server(args)
    else:
        pass
