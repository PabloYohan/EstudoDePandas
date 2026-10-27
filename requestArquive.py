import requests
import pandas as pd

def getDfFromAPI(latitude: float, longitude: float, url: str) -> pd.DataFrame: 
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": "2025-01-01",
        "end_date": "2025-03-31",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "America/Sao_Paulo",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    payload = response.json()
    if "daily" not in payload:
        raise ValueError(f"A API não retornou a chave 'daily': {payload}")

    df = pd.DataFrame(payload["daily"])
    df["time"] = pd.to_datetime(df["time"])

    return df