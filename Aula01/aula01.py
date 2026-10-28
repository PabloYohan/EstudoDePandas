import pandas as pd
from requestArquive import obter_historico

LATITUDE = -23.17944 
LONGITUDE = -45.88694 

START_DATE = "2025-01-01"
END_DATE = "2025-03-31"

df = obter_historico(LATITUDE, LONGITUDE, START_DATE, END_DATE)

#print(df.head(7))
#print(df.tail(5))
#print(df.shape[0])
#print(df.shape[1])

#print(df[['time', 'temperature_2m_max']].head(10))
#print(df['precipitation_sum'])
print(df['temperature_2m_max'].max())
print(df['temperature_2m_min'].min())

print(df['temperature_2m_max'].mean())

print(df.nlargest(1, 'temperature_2m_max'))

print(df['precipitation_sum'].sum(min_count=1))
print(df['precipitation_sum'].isna().sum())

print(df['temperature_2m_max'].isnull().sum())
print(df['temperature_2m_min'].isnull().sum())


print(df['time'].isnull().sum())
print(df['precipitation_sum'].isnull().sum())
print(df['time'].duplicated().sum())

datas_esperadas = pd.date_range(start=START_DATE, end=END_DATE, freq='D')
datas_recebidas = pd.DatetimeIndex(df['time'].dropna().unique())
datas_faltantes = datas_esperadas.difference(datas_recebidas)
datas_fora_periodo = datas_recebidas.difference(datas_esperadas)

print("Quantidade esperada de dias:", len(datas_esperadas))
print("Quantidade de linhas:", len(df))
print("Datas faltantes:", len(datas_faltantes))
print("Datas fora do período:", len(datas_fora_periodo))