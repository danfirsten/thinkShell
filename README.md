# thinkShell

An AI-powered command-line interface (CLI) tool that helps developers understand, debug, and optimize their code using OpenAI's GPT models.

## Tech Stack

- **Python 3.x**: Core programming language
- **Typer**: Modern CLI framework for building command-line applications
- **OpenAI API**: GPT-4 integration for code analysis
- **python-dotenv**: Environment variable management
- **OpenAI Python SDK**: Official Python client for OpenAI API

## Project Structure

```
thinkShell/
├── src/
│   └── thinkshell/
│       ├── __init__.py
│       ├── cli.py          # Main CLI application setup
│       ├── explain.py      # Code explanation functionality
│       ├── debug.py        # Code debugging functionality
│       ├── optimize.py     # Code optimization functionality
│       └── utils.py        # Shared utilities and OpenAI integration
├── tests/
│   └── test_utils.py      # Unit tests
├── .env.example           # Template for environment variables
├── .gitignore            # Git ignore rules
├── main.py               # Entry point
├── pyproject.toml        # Project metadata and dependencies
├── requirements.txt      # Python package dependencies
└── setup.py             # Package installation script
```

## Features

### 1. Code Explanation
```bash
python main.py explain <file_path>
```
- Reads the specified file
- Sends the code to GPT-4 for analysis
- Returns a detailed explanation of the code's functionality
- Includes debug prints to track progress

### 2. Code Debugging
```bash
python main.py debug <file_path>
```
- Analyzes the code for potential bugs
- Provides explanations for any issues found
- Returns "No bugs found" if the code appears to be bug-free
- Includes detailed error messages and suggestions

### 3. Code Optimization
```bash
python main.py optimize <file_path>
```
- Reviews the code for optimization opportunities
- Suggests improvements for performance, readability, and best practices
- Provides detailed explanations for each suggestion
- Focuses on both code quality and performance

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/thinkShell.git
   cd thinkShell
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up OpenAI API Key**
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - Or set it as an environment variable:
     ```bash
     # Windows PowerShell
     $env:OPENAI_API_KEY = "your_api_key_here"
     
     # Linux/macOS
     export OPENAI_API_KEY="your_api_key_here"
     ```

## Usage Examples

1. **Explain a Python File**
   ```bash
   python main.py explain src/thinkshell/utils.py
   ```

2. **Debug Your Code**
   ```bash
   python main.py debug your_script.py
   ```

3. **Get Optimization Suggestions**
   ```bash
   python main.py optimize your_script.py
   ```

## How It Works

1. **Command Processing**
   - The CLI framework (Typer) processes user commands
   - Commands are routed to the appropriate module (explain/debug/optimize)

2. **File Reading**
   - The specified file is read using the `read_code_file` utility
   - File existence and readability are verified

3. **AI Analysis**
   - The code is sent to OpenAI's GPT-4 model
   - A specific prompt is crafted based on the command type
   - The model analyzes the code and provides insights

4. **Response Handling**
   - The AI response is processed and formatted
   - Results are displayed to the user in a readable format

## Error Handling

The tool includes comprehensive error handling for:
- Missing files
- Invalid API keys
- API request failures
- File reading errors

