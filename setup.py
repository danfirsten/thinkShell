from setuptools import setup, find_packages

setup(
    name="thinkshell",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "typer",
        "requests",
        "rich",
        "openai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "thinkshell=thinkshell.cli:app",
        ],
    },
)
