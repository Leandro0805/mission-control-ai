"""Motor principal do EnviroSat."""

from src.telemetria import gerar_telemetria
from src.alertas import (
    analisar_alertas,
    resposta_automatica
)


class MissionEngine:

    def __init__(self):
        self.trilha = "EnviroSat"

    def is_ready(self):
        return True

    def status_snapshot(self):

        dados = gerar_telemetria()

        alertas = analisar_alertas(dados)

        respostas = resposta_automatica(dados)

        texto = (
            f"🌳 STATUS DO ENVIROSAT\n\n"
            f"🌡 Temperatura: {dados['temperatura_sensor']}°C\n"
            f"🔋 Energia: {dados['energia']}%\n"
            f"💾 Buffer de imagens: {dados['buffer_imagens']}%\n"
            f"📡 Comunicação: {dados['sinal_comunicacao']}%\n"
        )

        # Exibir alertas
        if alertas:

            texto += "\n⚠ ALERTAS DETECTADOS:\n"

            for alerta in alertas:
                texto += f"- {alerta}\n"

        # Exibir respostas automáticas
        if respostas:

            texto += "\n🤖 RESPOSTAS AUTOMÁTICAS:\n"

            for resposta in respostas:
                texto += f"- {resposta}\n"

        return texto

    def analyze(self, pergunta_usuario):

        return (
            "🛰 EnviroSat operacional.\n\n"
            "Sistema de alertas funcionando corretamente."
        )