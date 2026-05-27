"""Sistema de alertas do EnviroSat."""


def analisar_alertas(telemetria):

    alertas = []

    # Temperatura crítica
    if telemetria["temperatura_sensor"] > 80:
        alertas.append(
            "🔥 ALERTA CRÍTICO: superaquecimento detectado."
        )

    # Energia crítica
    if telemetria["energia"] < 25:
        alertas.append(
            "🔋 ALERTA: nível de energia muito baixo."
        )

    # Comunicação ruim
    if telemetria["sinal_comunicacao"] < 50:
        alertas.append(
            "📡 ALERTA: sinal de comunicação instável."
        )

    # Buffer quase cheio
    if telemetria["buffer_imagens"] > 90:
        alertas.append(
            "💾 ALERTA: buffer de imagens próximo do limite."
        )
    if telemetria["precisao_geolocalizacao"] < 80:
        alertas.append(
            "🛰 ALERTA: precisão de geolocalização degradada."
        )
    if telemetria["sensor_optico_rgb_nir"] == "INSTÁVEL":
        alertas.append(
        "📷 ALERTA: sensor óptico RGB+NIR instável."
    )
    if telemetria["focos_incendio"] > 10:
    alertas.append(
        "🔥 ALERTA: múltiplos focos de incêndio detectados."
    )
    return alertas


def resposta_automatica(telemetria):

    respostas = []

    # Resposta automática para energia crítica
    if telemetria["energia"] < 20:
        respostas.append(
            "⚡ MODO ECONOMIA ativado automaticamente."
        )

    # Resposta automática para superaquecimento
    if telemetria["temperatura_sensor"] > 85:
        respostas.append(
            "🧊 Redução automática de processamento térmico."
        )

    return respostas