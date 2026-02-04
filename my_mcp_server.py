from fastmcp  import FastMCP
import sys

server = FastMCP("simple_greeting_server");  # ("MyLocalDemoServer")

@server.tool()
def greet_user(name: str) -> str:
    """
    A tool that returns a greeting message for a given name.
    Args:
        name: The name of the person to greet.
    Returns:
        str: A greeting message.
    """
    return f"Hello {name}, how are you today?"

if __name__ == "__main__":
    # Use stdio transport for local integration
    server.run(transport="stdio")
def greet_user(name: str) -> str:
    """
    A tool that returns a greeting message for a given name.
    Args:
        name: The name of the person to greet.
    Returns:
        str: A greeting message.
    """
    return f"Hello {name}, how are you today?"


if __name__ == "__main__":
    # Use stdio transport for local integration
    server.run(transport="stdio")