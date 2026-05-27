"""Motor principal do EnviroSat."""

from src.telemetria import gerar_telemetria
from src.alertas import (
    analisar_alertas,
    resposta_automatica
)

from dotenv import load_dotenv
from ollama import Client

import os


load_dotenv()


class MissionEngine:

    def __init__(self):

        self.trilha = "EnviroSat"

        # Memória dos últimos ciclos
        self.historico_missao = []

        self.client = Client(
            host="https://ollama.com",
            headers={
                "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
            }
        )

    def is_ready(self):
        return True

    def gerar_estado_missao(self):

        dados = gerar_telemetria()

        alertas = analisar_alertas(dados)

        respostas = resposta_automatica(dados)

        return dados, alertas, respostas

    def atualizar_historico(self, dados):

        self.historico_missao.append(dados)

        # Mantém apenas os últimos 5 ciclos
        if len(self.historico_missao) > 5:
            self.historico_missao.pop(0)

    def status_snapshot(self):

        dados, alertas, respostas = self.gerar_estado_missao()

        texto = (
            f"🌳 STATUS DO ENVIROSAT\n\n"
            f"🌡 Temperatura: {dados['temperatura_sensor']}°C\n"
            f"🔋 Energia: {dados['energia']}%\n"
            f"💾 Buffer de imagens: {dados['buffer_imagens']}%\n"
            f"📡 Comunicação: {dados['sinal_comunicacao']}%\n"
            f"🛰 Precisão geolocalização: {dados['precisao_geolocalizacao']}%\n"
            f"📷 Sensor RGB+NIR: {dados['sensor_optico_rgb_nir']}\n"
            f"🔥 Focos detectados: {dados['focos_incendio']}\n"
        )

        if alertas:

            texto += "\n⚠ ALERTAS DETECTADOS:\n"

            for alerta in alertas:
                texto += f"- {alerta}\n"

        if respostas:

            texto += "\n🤖 RESPOSTAS AUTOMÁTICAS:\n"

            for resposta in respostas:
                texto += f"- {resposta}\n"

        return texto

    def carregar_prompt(self):

        with open(
            "prompts/system_prompt.md",
            "r",
            encoding="utf-8"
        ) as arquivo:

            return arquivo.read()

    def escolher_persona(self, dados, alertas):

        # Falhas críticas → Engenheiro
        if (
            dados["temperatura_sensor"] > 85
            or dados["energia"] < 20
            or dados["sinal_comunicacao"] < 45
        ):

            return "ENGENHEIRO ESPACIAL"

        # Muitos alertas → Especialista ambiental
        if len(alertas) >= 2:

            return "ESPECIALISTA AMBIENTAL"

        # Operação normal
        return "OPERADOR DE MISSÃO"

    def analyze(self, pergunta_usuario):

        dados, alertas, respostas = self.gerar_estado_missao()

        # Atualiza memória temporal
        self.atualizar_historico(dados)

        prompt_sistema = self.carregar_prompt()

        persona = self.escolher_persona(
            dados,
            alertas
        )

        contexto = f"""
PERSONA ATIVA:
{persona}

HISTÓRICO DOS ÚLTIMOS CICLOS:
{self.historico_missao}

TELEMETRIA ATUAL:

Temperatura: {dados['temperatura_sensor']}°C
Energia: {dados['energia']}%
Buffer: {dados['buffer_imagens']}%
Comunicação: {dados['sinal_comunicacao']}%
Precisão geolocalização: {dados['precisao_geolocalizacao']}%
Sensor RGB+NIR: {dados['sensor_optico_rgb_nir']}
Focos de incêndio: {dados['focos_incendio']}
ALERTAS:
{alertas}

RESPOSTAS AUTOMÁTICAS:
{respostas}

PERGUNTA DO OPERADOR:
{pergunta_usuario}
"""

        resposta = self.client.chat(
            model="gpt-oss:120b",
            messages=[
                {
                    "role": "system",
                    "content": prompt_sistema
                },
                {
                    "role": "user",
                    "content": contexto
                }
            ]
        )

        return resposta["message"]["content"]