import os
from dotenv import load_dotenv
import typer
from openai import OpenAI

load_dotenv()  # Load from .env file

client = OpenAI()  # This will automatically use OPENAI_API_KEY from environment

def read_code_file(filepath: str) -> str:
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        typer.echo(f"Error: File '{filepath}' not found.")
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"Error reading file: {str(e)}")
        raise typer.Exit(1)

def call_openai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Using gpt-4 instead of gpt-4.1
            messages=[
                {"role": "system", "content": "You are a helpful programming assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        typer.echo(f"Error calling OpenAI API: {str(e)}")
        raise typer.Exit(1)
