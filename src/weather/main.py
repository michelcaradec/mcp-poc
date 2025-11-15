import os
from argparse import (
    ArgumentParser,
    Namespace,
)
from asyncio.exceptions import CancelledError
from typing import Literal

from dotenv import load_dotenv

from mcp_server import mcp

load_dotenv(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '.env')))


def __get_arguments() -> Namespace:
    parser = ArgumentParser(description='Weather MCP Server.')

    parser.add_argument(
        '--transport',
        choices=[
            'stdio',
            'sse',
            'streamable-http',
        ],
        help='transport protocol to use',
    )

    # The MCP Inspector may pass some unknown arguments, to be ignored.
    args, _ = parser.parse_known_args()

    return args


def main() -> None:  # noqa: D103
    # Attention! The MCP Inspector doesn't forward the script arguments (an error is raised).
    args = __get_arguments()
    transport: Literal['stdio', 'sse', 'streamable-http'] = args.transport or os.getenv('TRANSPORT') or 'stdio'  # type: ignore

    # Initialize and run the server
    try:
        if transport == 'stdio':
            mcp.run(transport)
        elif transport == 'streamable-http':
            mcp.run(
                transport,
                host='127.0.0.1',
                port=int(os.getenv('MCP_PORT') or 8000),
                stateless_http=True,
            )
        else:
            raise ValueError(transport)
    except CancelledError:
        ...


if __name__ == '__main__':
    main()
