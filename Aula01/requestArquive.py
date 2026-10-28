import requests
import pandas as pd

ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"

def obter_historico(latitude: float, longitude: float, start_date: str, end_date: str) -> pd.DataFrame: 
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "America/Sao_Paulo",
    }

    response = requests.get(ARCHIVE_URL, params=params, timeout=10)
    response.raise_for_status()

    payload = response.json()
    if "daily" not in payload:
        raise ValueError(f"A API não retornou a chave 'daily': {payload}")

    df = pd.DataFrame(payload["daily"])
    df["time"] = pd.to_datetime(df["time"])

    return df