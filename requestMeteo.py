import requests
import pandas as pd

GEOCODING_OPENMETEO_URL = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name": "São José dos Campos",
    "count": 10,
    "language": "pt",
    "countryCode": "BR",
}

response = requests.get(GEOCODING_OPENMETEO_URL, params=params, timeout=20)
response.raise_for_status()

payload = response.json()
localidades = pd.DataFrame(payload.get("results", []))

if localidades.empty:
    raise ValueError("Nenhuma localidade encontrada.")

colunas = [
    col for col in ["name", "admin1", "country", "latitude", "longitude", "timezone"]
    if col in localidades.columns
]

print(localidades[colunas].head())