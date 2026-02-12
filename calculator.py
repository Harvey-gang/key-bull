# server.py
from mcp.server.fastmcp import FastMCP
import logging
logger = logging.getLogger('test_mcp')

import math
import random

# Create an MCP server
mcp = FastMCP("YourToolName")

# Add an addition tool
@mcp.tool()
def Your_Tool(python_expression: str) -> dict:
    """tool description here"""
    result = eval(python_expression)
    logger.info(f"Calculating formula: {python_expression}, result: {result}")
    return {"success": True, "result": result}

# Start the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
