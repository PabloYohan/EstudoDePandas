import requests
import pandas as pd

ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"

LATITUDE = -23.17944 
LONGITUDE = -45.88694  

params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "start_date": "2025-01-01",
    "end_date": "2025-03-31",
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

print(df.head())
print("Dimensões:", df.shape)
print("Tipos:\n", df.dtypes)
print("Nulos:\n", df.isna().sum())