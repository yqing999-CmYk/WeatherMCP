
from weathermcp.weather import mcp

def main():
    # Initialize and run the server
    #print("Hello from weathermcp!")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
