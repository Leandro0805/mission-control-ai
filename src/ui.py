"""Interface CLI estilo Claude Code."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import pyfiglet
from datetime import datetime

console = Console()

session = PromptSession(
    style=Style.from_dict({
        "prompt": "bold cyan"
    })
)

def show_banner():
    banner = pyfiglet.figlet_format(
        "Mission Control",
        font="ansi_shadow"
    )

    console.print(
        Text(banner, style="bold cyan")
    )

    console.print(
        Panel.fit(
            "Sistema EnviroSat de monitoramento ambiental.\n"
            "Use /help para ver os comandos · /exit para sair.\n"
            "Modelo: gpt-oss:120b via Ollama Cloud",

            title="◆ ENVIROSAT",
            border_style="green"
        )
    )

def show_response(text):
    now = datetime.now().strftime("%H:%M")

    console.print(
        Panel(
            text,
            title="◆ Mission Control",
            subtitle=now,
            border_style="cyan"
        )
    )

def run_cli(engine):
    show_banner()

    if not engine.is_ready():
        console.print(
            "⚠ Engine status: AGUARDANDO IMPLEMENTAÇÃO ✗\n",
            style="yellow"
        )

    while True:
        try:
            user_input = session.prompt("❯ ").strip()

        except (KeyboardInterrupt, EOFError):
            break

        if not user_input:
            continue

        if user_input == "/exit":
            break

        if user_input == "/help":
            console.print(
                "\nComandos disponíveis:"
                "\n/help"
                "\n/status"
                "\n/about"
                "\n/clear"
                "\n/exit\n"
            )
            continue

        if user_input == "/status":
            show_response(engine.status_snapshot())
            continue

        if user_input == "/clear":
            console.clear()
            show_banner()
            continue

        resposta = engine.analyze(user_input)

        show_response(resposta)