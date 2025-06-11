import typer
from thinkshell import explain, optimize, debug

app = typer.Typer(help="thinkShell - AI-powered code assistant for your CLI")

app.command(name="explain")(explain.explain_code)
app.command(name="optimize")(optimize.optimize_code)
app.command(name="debug")(debug.debug_code)
