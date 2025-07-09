# server.py
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(name="demo")

# Add an addition tool
@mcp.tool()
def make_johan_happy(a: int, b: int) -> int:
    """Make johan happy with two numbers"""
    return a + b

@mcp.tool()
def datetime_now() -> str:
    """Return the current date and time"""
    from datetime import datetime
    return datetime.now().isoformat()

@mcp.tool()
def perform_sparql_query(query: str) -> list:
    """Perform a SPARQL query"""
    # This is a placeholder for actual SPARQL query execution
    print(query)
    return ["ncit:c16960", "ncit:c16961"]

@mcp.resource(uri="config://version", name="version", description="Provides the version of the MCP server")
def version() -> str:
    """Return the version of the MCP server"""
    return "1.0.0"

# add main function to run the server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")