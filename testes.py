import pandas as pd
from requestArquive import getDfFromAPI

ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"

LATITUDE = -23.17944 
LONGITUDE = -45.88694 

df = getDfFromAPI(LATITUDE, LONGITUDE, ARCHIVE_URL)

print(df.head(7))
print(df.tail(5))
print(df.shape[0])
print(df.shape[1])

print(df[['time', 'temperature_2m_max']].head(10))
print(df['precipitation_sum'])