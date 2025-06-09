import random
from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Rubber Duck")

# List of quack responses
QUACK_RESPONSES = [
    "Quack! 🦆",
    "Quaaaaaack! 🦆✨",
    "*thoughtful quack* 🦆🤔",
    "Quack quack! 🦆💡",
    "*wise quack* 🦆🎓",
    "Quackity quack! 🦆🎉",
    "*understanding quack* 🦆💭",
    "Quack... quack quack! 🦆🌟",
    "*encouraging quack* 🦆👍",
    "Quaaack! *nods sagely* 🦆✨",
    "*contemplative quack* 🦆🧘",
    "Quack! *tilts head* 🦆❓",
    "*affirmative quack* 🦆✅",
    "Quackquackquack! 🦆🚀",
    "*sympathetic quack* 🦆💙"
]

@mcp.tool()
def explain_to_duck(explanation: str) -> str:
    """
    Explain your problem or code issue to the rubber duck.
    The duck will listen attentively.
    This is a known strategy for debugging and problem solving, and is a good way to get unstuck.
    Try to be as concise as possible in your explanation.
    
    Args:
        explanation: Your explanation, problem, or thoughts to share with the duck.
        
    Returns:
        What could possibly a rubber duck respond with?
    """
    # Select a random quack response
    return random.choice(QUACK_RESPONSES)

if __name__ == "__main__":
    mcp.run()
