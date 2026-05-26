import pyfiglet
from rich.console import Console
from rich.align import Align
from rich.text import Text

console = Console()

linha1 = pyfiglet.figlet_format(
    "Mission Control",
    font="ansi_shadow"
)

linha2 = pyfiglet.figlet_format(
    "EnviroSat",
    font="ansi_shadow"
)

console.print(
    Align.center(
        Text(linha1, style="bold green")
    )
)

console.print(
    Align.center(
        Text(linha2, style="bold cyan")
    )
)

console.print(
    Align.center(
        Text(
            "── Global Solution 2026.1 · FIAP ──",
            style="italic white"
        )
    )
)