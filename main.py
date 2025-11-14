from fastmcp import FastMCP
import math
import os

# --------------------------------------------------------
# Create MCP server
# --------------------------------------------------------
mcp = FastMCP("scientific-calculator")


# --------------------------------------------------------
# Basic arithmetic tools
# --------------------------------------------------------

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@mcp.tool()
def mod(a: float, b: float) -> float:
    """Return a modulo b."""
    return a % b


# --------------------------------------------------------
# Power & roots
# --------------------------------------------------------

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise base to exponent."""
    return math.pow(base, exponent)


@mcp.tool()
def sqrt(x: float) -> float:
    """Square root."""
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)


# --------------------------------------------------------
# Trigonometry (radians)
# --------------------------------------------------------

@mcp.tool()
def sin(x: float) -> float:
    """Sine of x (radians)."""
    return math.sin(x)


@mcp.tool()
def cos(x: float) -> float:
    """Cosine of x (radians)."""
    return math.cos(x)


@mcp.tool()
def tan(x: float) -> float:
    """Tangent of x (radians)."""
    return math.tan(x)


# --------------------------------------------------------
# Inverse trigonometry
# --------------------------------------------------------

@mcp.tool()
def asin(x: float) -> float:
    """Arcsine of x (returns radians)."""
    return math.asin(x)


@mcp.tool()
def acos(x: float) -> float:
    """Arccosine of x (returns radians)."""
    return math.acos(x)


@mcp.tool()
def atan(x: float) -> float:
    """Arctangent of x (returns radians)."""
    return math.atan(x)


# --------------------------------------------------------
# Exponentials & logs
# --------------------------------------------------------

@mcp.tool()
def exp(x: float) -> float:
    """e^x."""
    return math.exp(x)


@mcp.tool()
def ln(x: float) -> float:
    """Natural log (base e)."""
    if x <= 0:
        raise ValueError("ln(x) undefined for x <= 0.")
    return math.log(x)


@mcp.tool()
def log10(x: float) -> float:
    """Logarithm base 10."""
    if x <= 0:
        raise ValueError("log10(x) undefined for x <= 0.")
    return math.log10(x)


# --------------------------------------------------------
# Misc utilities
# --------------------------------------------------------

@mcp.tool()
def absval(x: float) -> float:
    """Absolute value."""
    return abs(x)


@mcp.tool()
def round_to(x: float, digits: int = 0) -> float:
    """Round x to a given number of decimal places."""
    return round(x, digits)


# --------------------------------------------------------
# Server entrypoint
# --------------------------------------------------------

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", "8000"))
    # Use HTTP transport so MCP Inspector & ChatGPT Apps can connect
    mcp.run(transport="http", host="0.0.0.0", port=port)
