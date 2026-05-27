"""Simulação de telemetria do satélite EnviroSat."""

import random


def gerar_telemetria():
    """
    Gera dados simulados do satélite.
    """

    telemetria = {
        "temperatura_sensor": random.randint(30, 95),

        "energia": random.randint(10, 100),

        "buffer_imagens": random.randint(20, 100),

        "sinal_comunicacao": random.randint(40, 100),

        "precisao_geolocalizacao": random.randint(70, 100),

        "sensor_optico_rgb_nir": random.choice([
            "OPERACIONAL",
            "CALIBRANDO",
            "INSTÁVEL"
        "focos_incendio": random.randint(0, 15)
        ])
}

    return telemetria