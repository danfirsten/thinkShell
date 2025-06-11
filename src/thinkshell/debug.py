import typer
from thinkshell.utils import read_code_file, call_openai

app = typer.Typer()

@app.command()
def debug_code(file: str):
    print(f"Reading file: {file}")  # Debug print
    code = read_code_file(file)
    print(f"Code read successfully, length: {len(code)}")  # Debug print
    prompt = f"Find and explain any bugs in the following code:\n\n{code} . If there are no bugs, just say 'No bugs found'."
    print("Calling OpenAI API...")  # Debug print
    response = call_openai(prompt)
    print("Got response from OpenAI")  # Debug print
    typer.echo(response)

if __name__ == "__main__":
    app()
