# Rubber Duck MCP

## Description

**Rubber Duck MCP** is a Minimal Command Protocol (MCP) tool that brings the power of [rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging) to your AI development environment. Rubber duck debugging is a proven technique in software engineering, where articulating a problem in natural language—often to an inanimate object like a rubber duck—can illuminate solutions and clarify thought processes. This method, first popularized in _The Pragmatic Programmer_ (Hunt & Thomas, 1999), is widely recognized for its effectiveness in:

- Revealing hidden assumptions and logical errors
- Encouraging step-by-step reasoning
- Facilitating deeper understanding through explanation
- Reducing cognitive load by externalizing thought

> "In describing what the code is supposed to do and observing what it actually does, any incongruity between these two becomes apparent." — [Wikipedia: Rubber Duck Debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)

By integrating this method into an LLM-powered IDE, Rubber Duck MCP enables developers and AI agents to:

- **Debug more effectively** by explaining problems to a non-judgmental, always-available listener
- **Enhance LLM reasoning** by prompting the model to articulate and reflect on its own logic
- **Accelerate problem-solving** by surfacing solutions through structured self-explanation

For further reading:
- [Rubber Duck Debugging (rubberduckdebugging.com)](https://rubberduckdebugging.com/)
- [The Psychology Underlying the Power of Rubber Duck Debugging](https://pressupinc.com/blog/2014/06/psychology-underlying-power-rubber-duck-debugging/)

## Installation

### Prerequisites
- Python 3.8+
- [fastmcp](https://github.com/osadeh/fastmcp) (install via pip)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Omer-Sadeh/RubberDuckMCP.git
   cd RubberDuckMCP
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Add Rubber Duck MCP to Cursor (or another AI IDE supporting MCP):**
   - Open your `.cursor/mcp.json` file (or the equivalent configuration for your IDE).
   - Add an entry for Rubber Duck MCP, specifying the venv's Python executable and the path to `RubberMCP.py`. For example:
     ```json
     {
       "mcpServers": {
         "rubber-duck": {
           "command": "/absolute/path/to/RubberDuckMCP/.venv/bin/python",
           "args": [
             "/absolute/path/to/RubberDuckMCP/RubberMCP.py"
           ]
         }
       }
     }
     ```
   - Adjust the `command` and `args` fields to match your virtual environment's Python executable and the path to `RubberMCP.py` on your system.
   - Save the file and restart Cursor (or your IDE) to load the new MCP server.

## Usage

Once configured, use the `explain_to_duck` tool to articulate your problem or code issue. The Rubber Duck MCP will listen and respond, helping you clarify your thinking and uncover solutions.

## License

This project is licensed under the [MIT License](LICENSE). Everyone is welcome to contribute, fork, and copy this repository. Collaboration and open-source contributions are highly encouraged! 