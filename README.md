# Model Context Protocol Proof Of Concept

<details>
<summary>Table of contents</summary>

- [Abstract](#abstract)
- [Bootstrap](#bootstrap)
- [Demonstration Workflow](#demonstration-workflow)
- [MCP Server](#mcp-server)
- [MCP Inspector](#mcp-inspector)
- [AI Applications](#ai-applications)
  - [Claude Desktop](#claude-desktop)
    - [Claude Desktop - Setup](#claude-desktop---setup)
    - [Claude Desktop - Configure MCP Server](#claude-desktop---configure-mcp-server)
    - [Usage](#usage)
  - [Gemini CLI](#gemini-cli)
    - [Gemini CLI - Setup](#gemini-cli---setup)
    - [Gemini CLI - Configure MCP Server](#gemini-cli---configure-mcp-server)
- [Resources](#resources)

</details>

## Abstract

This proof-of-concept project is meant to demonstrate how to create and use an agent using the [Model Context Protocol](https://modelcontextprotocol.io).

This was inspired by the article [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server).

## Bootstrap

Project setup:

```bash
uv init --python 3.10
uv add "fastmcp aiofiles"
```

Environment initialization:

```bash
uv sync --extra dev
```

## Demonstration Workflow

1. Start the [MCP server](#mcp-server).

    ```bash
    uv run ./src/weather/main.py --transport streamable-http
    ```

2. Start [Claude Desktop](#claude-desktop).  

> [!TIP]
> Go to the "Developer Settings", and check that the MCP server is properly [configured](#claude-desktop---configure-mcp-server) and running.

1. Create a new chat.

> [!TIP]
> Click on the button "Search and tools", and check that the MCP server "weather" is activated.  
> Expand the item to view the available and activated tools.
> Disable "Web search" in to force the use of the agent.

1. Run the demonstration prompt `get_demonstration_prompt`.

> [!TIP]
> Click on the button ➕, expand the item "Add from weather", then select the prompt "get_demonstration_prompt".  
> Click on the text file "get_demonstration_prompt.txt" to view the content of the prompt.  
> Click on the button ⬆️ or press [Enter] in the prompt editor to run the prompt.

> [!NOTE]
> If a tool execution is required, a grant will be requested by the AI application.  
> Allow the execution by clicking on either the button "Allow once" or "Always allow".

5. Get the weather of another place with the prompt `get_weather_prompt`.
6. Get some advice with the prompt `get_weather_advice_prompt`.

> [!NOTE]
> We see the interest of an agent, which is triggered by the LLM to satisfy the user request, requiring information on the weather, but not directly about the weather.

7. Get another advice with the prompt `get_where_should_i_go_prompt`.

> [!NOTE]
> Two agents will be executed: `get_favorite_cities_prompt` to get the list of favorite cities, then `get_weather_prompt` for each city.

8. Quit Claude Desktop.
9. Stop the MCP server.

## MCP Server

To manually start the MCP server:

```bash
uv run ./src/weather/main.py [--transport {stdio|sse|streamable-http}]
```

It will listen for messages from MCP hosts.

> [!IMPORTANT]
> Do not forget to stop the MCP server.

## MCP Inspector

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) allows visual testing of tools, prompts and resources exposed by MCP servers.

1. Run the MCP Inspector:

    ```bash
    uv run fastmcp dev ./src/weather/main.py
    ```

> [!TIP]
> See `fastmcp` CLI options at <https://fastmcp.wiki/en/patterns/cli#fastmcp-dev>.

1. Click on the button "Connect".
2. Go to the tab "Tools", and click on "List Tools".

## AI Applications

### Claude Desktop

#### Claude Desktop - Setup

- [How to Install Claude Desktop with MCP Desktop Commander on Ubuntu/Debian Linux](https://studiozandra.com/how-to-install-claude-desktop-with-mcp-desktop-commander-on-ubuntu-debian-systems/).
  - <https://github.com/aaddrick/claude-desktop-debian/releases> (more stars).

    ```bash
    sudo dpkg -i ./claude-desktop_VERSION_ARCHITECTURE.deb

    # If you encounter dependency issues:
    sudo apt --fix-broken install
    ```

- Model Context Protocol settings are stored in the file `claude_desktop_config.json` in the directory `~/.config/Claude` on Linux, `~/Library/ApplicationSupport/Claude` on MacOS.
- Logs are stored in the subfolder `logs`.

#### Claude Desktop - Configure MCP Server

1. Open Claude configuration file:

    ```bash
    nano ~/.config/Claude/claude_desktop_config.json
    ```

2. Declare the MCP server:

    With transport `stdio`:

    ```json
    {
        "mcpServers": {
            "weather": {
                "command": "${HOME}/.local/bin/uv",
                "args": [
                    "--directory",
                    "${HOME}/Projects/mcp-poc",
                    "run",
                    "./src/weather/main.py"
                ]
            }
        }
    }
    ```

    With transport `streamable-http`:

    ```json
    {
        "mcpServers": {
            "weather": {
                "command": "npx",
                "args": [
                    "-y",
                    "mcp-remote",
                    "http://127.0.0.1:8000/mcp/"
                ],
                "env": {
                    "MCP_TRANSPORT_STRATEGY": "http-only"
                }
            }
        }
    }
    ```

> [!TIP]
> You may need to put the full path to the uv executable in the command field.

> [!TIP]
> The [JSON configuration](https://fastmcp.wiki/en/patterns/cli#mcp-json-generation) can be generated with the FastMCP CLI tool:
> `uv run fastmcp install mcp-json ./src/weather/main.py`.

> [!TIP]
> See [Building and Exposing MCP Servers with FastMCP (STDIO, HTTP and SSE)](https://medium.com/%40anil.goyal0057/building-and-exposing-mcp-servers-with-fastmcp-stdio-http-and-sse-ace0f1d996dd) and [Claude Code MCP Guide](https://github.com/majkonautic/claude-code-mcp-guide).

> [!TIP]
> The transport `streamable-http` is more convenient to debug the MCP server.

> [!IMPORTANT]
> A paid subscription of Claude is required in order to add a remote server.

#### Usage

1. Start the MCP server (here with the transport `streamable-http`):

    ```bash
    uv run ./src/weather/main.py --transport streamable-http
    ```

2. Start Claude desktop.
3. Write a prompt:

    > What is the weather in Redmond?

> [!TIP]
> Disable "Web search" in the "Search and tools" menu to force the use of the agent.

> [!TIP]
> To check the listening ports: `netstat -tunlp`.

### Gemini CLI

#### Gemini CLI - Setup

1. Install:

    ```bash
    # Global installation
    npm install -g @google/gemini-cli

    # Instant run (no installation)
    npx https://github.com/google-gemini/gemini-cli
    ```

2. Start the CLI:

    ```bash
    gemini
    ```

#### Gemini CLI - Configure MCP Server

1. Open Gemini CLI configuration file:

    ```bash
    nano ~/.gemini/settings.json
    ```

2. Declare the MCP server:

    With transport `stdio`:

    ```json
    {
        "mcpServers": {
            "weather": {
                "command": "${HOME}.local/bin/uv",
                "args": [
                    "--directory",
                    "${HOME}Projects/mcp-poc",
                    "run",
                    "src/weather/main.py"
                ],
                "trust": false
            }
        }
    }
    ```

> [!TIP]
> You may need to put the full path to the uv executable in the command field.

> [!TIP]
> See [MCP servers with the Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md).

## Resources

- [Python MCP Server: Connect LLMs to Your Data](https://realpython.com/python-mcp/).
- [How to use MCP Inspector](https://medium.com/@laurentkubaski/how-to-use-mcp-inspector-2748cd33faeb).
- [Beginner’s Guide to Building and Testing Your First MCP Server with uv and Claude](https://mahendranp.medium.com/beginners-guide-to-building-and-testing-your-first-mcp-server-with-uv-and-claude-3bfc6198212a).
- [Episode #527 - MCP Servers for Python Devs](https://talkpython.fm/episodes/show/527/mcp-servers-for-python-devs).
- [You Should Write An Agent](https://fly.io/blog/everyone-write-an-agent/).
- [Assistant IA pour le code : comment ça marche ? J'en ai codé un](https://www.youtube.com/watch?v=TodO0qrsDjw).
- [🤖 Gemini dans votre terminal avec Gemini CLI](https://dev.to/zenika/gemini-dans-votre-terminal-avec-gemini-cli-1b6i).
- [gemini-cli: An open-source AI agent that brings the power of Gemini directly into your terminal](https://github.com/google-gemini/gemini-cli).
- [gemini-cli-tips: Gemini CLI Tips and Tricks](https://github.com/addyosmani/gemini-cli-tips).
- [Claude-Code-Usage-Monitor: Real-time Claude Code usage monitor with predictions and warnings](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor).
- [Debugging](https://modelcontextprotocol.io/legacy/tools/debugging).
- [Stumbling into AI: Part 6—I’ve been thinking about Agents and MCP all wrong](https://rmoff.net/2025/11/20/stumbling-into-ai-part-6ive-been-thinking-about-agents-and-mcp-all-wrong/).
- [How MCP Works](https://newsletter.systemdesign.one/p/how-mcp-works).
