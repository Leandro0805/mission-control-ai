"""Interface CLI do EnviroSat."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.rule import Rule

from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

import pyfiglet

from datetime import datetime

console = Console()

session = PromptSession(
    style=Style.from_dict({
        "prompt": "bold ansigreen"
    })
)


def show_banner():

    banner = pyfiglet.figlet_format(
        "EnviroSat",
        font="slant"
    )

    console.print(
        Text(
            banner,
            style="bold bright_green"
        )
    )

    console.print(
        Panel.fit(
            "🛰 Sistema orbital de monitoramento ambiental\n"
            "🌳 Detecção de queimadas e desmatamento\n"
            "📡 Use /help para ver os comandos\n"
            "🤖 Modelo: gpt-oss:120b via Ollama Cloud",

            title="◆ ENVIROSAT CONTROL CENTER",
            border_style="bright_green"
        )
    )

    console.print(
        Rule(
            style="green"
        )
    )


def detectar_severidade(texto):

    texto = texto.lower()

    if (
        "crítico" in texto
        or "falha" in texto
        or "perigo" in texto
        or "incêndio" in texto
        or "degradada" in texto
    ):

        return "🔴 CRÍTICO", "red"

    if (
        "atenção" in texto
        or "alerta" in texto
        or "monitorar" in texto
    ):

        return "🟡 ATENÇÃO", "yellow"

    return "🟢 OPERACIONAL", "green"


def show_response(text):

    now = datetime.now().strftime("%d/%m %H:%M:%S")

    severidade, cor = detectar_severidade(text)

    titulo = (
        f"◆ ENVIROSAT MISSION TERMINAL • {severidade}"
    )

    console.print(
        Panel(
            text,
            title=titulo,
            subtitle=now,
            border_style=cor,
            padding=(1, 2)
        )
    )


def show_help():

    table = Table(
        title="COMANDOS DISPONÍVEIS",
        border_style="bright_green"
    )

    table.add_column(
        "Comando",
        style="bright_cyan"
    )

    table.add_column(
        "Descrição",
        style="white"
    )

    table.add_row(
        "/help",
        "Mostra os comandos disponíveis"
    )

    table.add_row(
        "/status",
        "Mostra snapshot rápido da missão"
    )

    table.add_row(
        "/clear",
        "Limpa o terminal"
    )

    table.add_row(
        "/logs",
        "Mostra logs simulados da missão"
    )

    table.add_row(
        "/alerts",
        "Mostra alertas ativos"
    )

    table.add_row(
        "/crise",
        "Simula cenário crítico"
    )

    table.add_row(
        "/exit",
        "Encerra o sistema"
    )

    console.print(table)


def show_logs():

    logs = (
        "[12:03] 🔄 Ciclo orbital iniciado\n"
        "[12:05] 📡 Downlink parcial concluído\n"
        "[12:06] 🌳 Monitoramento ambiental ativo\n"
        "[12:07] 🔥 Varredura térmica executada\n"
        "[12:08] 🛰 Telemetria sincronizada\n"
    )

    console.print(
        Panel(
            logs,
            title="◆ LOGS OPERACIONAIS",
            border_style="cyan"
        )
    )


def show_alerts():

    alertas = (
        "🟡 Nenhum alerta crítico ativo.\n"
        "📡 Comunicação estável.\n"
        "🌳 Monitoramento ambiental operacional."
    )

    console.print(
        Panel(
            alertas,
            title="◆ CENTRAL DE ALERTAS",
            border_style="yellow"
        )
    )


def show_crisis_mode():

    crise = (
        "🔴 MODO DE CRISE ATIVADO\n\n"
        "🔥 Múltiplos focos de incêndio detectados\n"
        "📡 Comunicação degradada\n"
        "🔋 Energia abaixo do limite ideal\n"
        "🛰 Geolocalização instável\n\n"
        "⚠ Brigadas terrestres foram notificadas.\n"
        "⚠ Sistema entrou em monitoramento intensivo."
    )

    console.print(
        Panel(
            crise,
            title="◆ CRISIS MODE",
            border_style="red",
            padding=(1, 2)
        )
    )


def run_cli(engine):

    show_banner()

    if not engine.is_ready():

        console.print(
            "🟡 Engine status: aguardando implementação\n",
            style="yellow"
        )

    while True:

        try:

            user_input = session.prompt(
                "[ENVIRONET] ❯ "
            ).strip()

        except (KeyboardInterrupt, EOFError):

            break

        if not user_input:

            continue

        if user_input == "/exit":

            console.print(
                "\n🛰 Encerrando EnviroSat...\n",
                style="bold red"
            )

            break

        if user_input == "/help":

            show_help()

            continue

        if user_input == "/status":

            show_response(
                engine.status_snapshot()
            )

            continue

        if user_input == "/clear":

            console.clear()

            show_banner()

            continue

        if user_input == "/logs":

            show_logs()

            continue

        if user_input == "/alerts":

            show_alerts()

            continue

        if user_input == "/crise":

            show_crisis_mode()

            continue

        resposta = engine.analyze(user_input)

        show_response(resposta)