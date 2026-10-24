# Curso prático de Pandas + APIs REST — do intermediário ao avançado

**Perfil:** Python intermediário  
**Objetivo:** domínio geral de Pandas aplicado a dados reais  
**Duração sugerida:** 8 semanas, 24 aulas, 3 aulas por semana (60–90 min/aula), mais exercícios e projeto final  
**Estratégia:** obter dados reais por APIs públicas, entender JSON, transformar em DataFrames, analisar, validar e persistir resultados.

> **Regra didática:** os exercícios e desafios não possuem soluções neste material. Primeiro execute e envie seu código para revisão; peça dicas graduais quando necessário.

## 1. Stack e ambiente

- Python 3.11+ (sugestão, não exigência rígida)
- `requests`: chamadas HTTP e tratamento de respostas
- `pandas`: processamento de dados
- `openpyxl`: leitura e escrita de Excel
- `matplotlib`: gráficos
- `sqlalchemy` e `psycopg`: integração com PostgreSQL
- `pytest`: testes de transformação
- Opcional: JupyterLab para exploração interativa

Crie um projeto e ambiente virtual:

```bash
mkdir pandas-apis && cd pandas-apis
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
python -m pip install pandas requests openpyxl matplotlib sqlalchemy 'psycopg[binary]' pytest jupyterlab
mkdir -p src data/raw data/processed reports tests
```

No Windows, ative com `.venv\\Scripts\\activate` (PowerShell: `.venv\\Scripts\\Activate.ps1`).

### Estrutura sugerida

```text
pandas-apis/
├── .venv/
├── src/
│   ├── aula01.py
│   ├── api_client.py
│   ├── transformations.py
│   └── pipeline.py
├── data/
│   ├── raw/
│   └── processed/
├── reports/
├── tests/
└── README.md
```

## 2. API principal e proposta de projeto

### API principal: Open-Meteo

Usaremos duas rotas da [Open-Meteo](https://open-meteo.com/):

1. [Geocoding API](https://open-meteo.com/en/docs/geocoding-api): obtém latitude e longitude de uma cidade a partir do nome.
2. [Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api): obtém séries históricas por coordenada e período.

O serviço permite experimentos não comerciais sem chave de API, observados seus termos e limites. Os dados históricos são modelados/reanalisados e podem sofrer revisões; portanto não são sinônimo de medições diretas de estação.

**Projeto contínuo:** construir um analisador de clima histórico capaz de coletar dados de múltiplas cidades, checar a qualidade, comparar padrões, gerar séries temporais e publicar relatórios. Em módulos posteriores serão incorporadas fontes públicas com estruturas diferentes para ampliar a prática de integração.

### Modelo da rotina

**HTTP GET → validação de status → JSON → DataFrame → limpeza → análise → exportação → banco → testes.**

## 3. Plano completo de estudos — 24 aulas

### Semana 1 — Consumo de API e fundamentos

**Aula 1. API REST → JSON → DataFrame**  
Conteúdo: `requests.get`, `params`, `timeout`, `raise_for_status`, `.json`, dicionários/listas, `pd.DataFrame`, `head`, `shape`, `dtypes`.  
Prática: consultar a geocodificação e obter histórico meteorológico.  
Entrega: script que obtém dados reais de uma cidade e imprime resumo estrutural.

**Aula 2. Diagnóstico e inspeção dos dados**  
Conteúdo: `info`, `describe`, `columns`, `index`, `sample`, `isna`, tipos, unidades e metadados.  
Prática: auditar temperaturas e precipitação de um período.  
Entrega: relatório rápido de integridade da coleta.

**Aula 3. Seleção de linhas e colunas**  
Conteúdo: `loc`, `iloc`, Series versus DataFrame, índices, atribuição correta, `copy`.  
Prática: consultar intervalos e variáveis selecionadas.  
Entrega: seleção parametrizada por coluna e período.

**Checkpoint:** explicar a diferença entre JSON aninhado, Series e DataFrame, além de identificar tipos incorretos antes de analisar.

### Semana 2 — Consultas e transformação

**Aula 4. Filtros eficientes**  
Conteúdo: máscaras booleanas, `query`, `between`, `isin`, `&`, `|`, `sort_values`.  
Prática: listar dias mais quentes, mais frios e chuvosos.  
Entrega: funções de filtragem com parâmetros.

**Aula 5. Colunas derivadas e vetorização**  
Conteúdo: atribuição, `assign`, operações entre colunas, condições com `where`, `mask`, `np.select` (opcional).  
Prática: amplitude térmica e classificação de dias.  
Entrega: conjunto de indicadores derivados sem loops por linha.

**Aula 6. Tipos e conversões**  
Conteúdo: `astype`, `to_numeric`, `to_datetime`, tipos anuláveis, coerção segura.  
Prática: padronizar datas e medidas de diferentes respostas.  
Entrega: função reutilizável de tipagem.

**Checkpoint:** construir consultas parametrizadas e justificar escolhas de tipos.

### Semana 3 — Qualidade de dados

**Aula 7. Valores ausentes e consistência**  
Conteúdo: `isna`, `dropna`, `fillna`, cobertura, validação de faixa e a diferença entre dado ausente e zero.  
Prática: auditar períodos incompletos.  
Entrega: relatório de qualidade com percentual de nulos por coluna.

**Aula 8. Duplicatas e chaves**  
Conteúdo: `duplicated`, `drop_duplicates`, chaves compostas, cardinalidade e unicidade.  
Prática: consolidar duas coletas parcialmente sobrepostas.  
Entrega: dataset com chave `(cidade, data)` validada.

**Aula 9. Strings e normalização**  
Conteúdo: `.str`, `strip`, `lower`, `replace`, regex, tratamento de nomes e códigos.  
Prática: normalizar metadados de cidades e países.  
Entrega: tabela padronizada de localidades.

### Semana 4 — Datas e projeto intermediário

**Aula 10. Datas e séries temporais**  
Conteúdo: `.dt`, fuso horário, ordenação, índices temporais, períodos, `resample`.  
Prática: produzir indicadores mensais de um histórico diário.  
Entrega: relatório mensal com série temporal consistente.

**Aula 11. Coleta de múltiplas cidades**  
Conteúdo: funções, composição de requests, respostas heterogêneas, `concat`, logs de erros, rate limiting responsável.  
Prática: consultar 3 a 5 cidades e identificar localidades inequivocamente.  
Entrega: dataset unificado de localidades.

**Aula 12. Mini-projeto 1: comparativo climático**  
Conteúdo: revisão aplicada de filtros, tipos, validação, concatenação e datas.  
Prática: construir comparação histórica entre cidades.  
Entrega: CSV limpo, relatório Markdown e explicação dos critérios de qualidade.

### Semana 5 — Agregações analíticas

**Aula 13. GroupBy**  
Conteúdo: `groupby`, `sum`, `mean`, `median`, `count`, `size`, `nunique`.  
Prática: estatísticas por cidade e mês.  
Entrega: tabela comparativa.

**Aula 14. Agregações avançadas**  
Conteúdo: `agg` nomeado, `transform`, `rank`, acumulados e rolling windows.  
Prática: anomalias relativas à média local e médias móveis.  
Entrega: indicadores calculados vetorialmente.

**Aula 15. Tabelas dinâmicas e visualização**  
Conteúdo: `pivot_table`, `crosstab`, tabelas por período e gráficos com Pandas/Matplotlib.  
Prática: heatmap simples (opcional) ou gráficos de comparações mensais.  
Entrega: gráficos reproduzíveis com explicações.

### Semana 6 — Integração de fontes

**Aula 16. Merge e joins**  
Conteúdo: `merge`, tipos de join, `validate`, `indicator`, cardinalidade e perdas por chave.  
Prática: unir dados meteorológicos com metadados de localidades.  
Entrega: merge auditável sem multiplicações de linhas indevidas.

**Aula 17. Reformatação e concatenação**  
Conteúdo: `concat`, `melt`, `pivot`, `stack`, `explode`, normalização de JSON.  
Prática: padronizar saídas de múltiplas APIs.  
Entrega: dados em formato tidy (cada observação em uma linha).

**Aula 18. Entrada e saída de arquivos**  
Conteúdo: `read_csv`, `read_excel`, `to_csv`, `to_excel`, Parquet (opcional), codificação, precisão e preservação de tipos.  
Prática: construir exportações por cidade e período.  
Entrega: relatório Excel com abas de base e agregados.

### Semana 7 — Persistência e arquitetura

**Aula 19. Pandas + PostgreSQL**  
Conteúdo: SQLAlchemy, conexão, `read_sql`, `to_sql`, tipos SQL, carga incremental e idempotência.  
Prática: armazenar dados históricos coletados.  
Entrega: tabela SQL sem duplicatas e consultas verificáveis.

**Aula 20. Pipeline ETL modular**  
Conteúdo: separar extração, transformação e carga; configuração; logs; `try/except`; tentativas com limites e tratamento de falhas HTTP.  
Prática: encapsular a coleta em módulos e funções.  
Entrega: `pipeline.py` executável por CLI.

**Aula 21. Testes e validação**  
Conteúdo: `pytest`, fixtures, validação de esquema, asserções de unicidade, valores esperados, mocks de API.  
Prática: testar o processamento sem depender da rede.  
Entrega: suíte mínima de testes.

### Semana 8 — Performance e conclusão

**Aula 22. Desempenho e memória**  
Conteúdo: vetorização versus `apply` e `iterrows`, `.memory_usage`, tipos eficientes, medição simples de tempo, chunks para arquivos.  
Prática: comparar duas estratégias de processamento.  
Entrega: benchmark reproduzível e interpretação.

**Aula 23. Engenharia de relatórios**  
Conteúdo: métricas finais, organização de gráficos, interpretação, exportação, rastreabilidade de origem e período.  
Prática: gerar automaticamente um relatório analítico.  
Entrega: relatório e datasets finais.

**Aula 24. Projeto final: pipeline de dados completo**  
Objetivo: coletar dados de no mínimo 3 cidades e 12 meses, validar esquema e chaves, armazenar histórico, calcular estatísticas, gerar gráficos e exportar relatório.  
Entrega: projeto organizado no Git, documentação de execução, testes, CSV/Excel, consultas SQL e relatório final.

## 4. Método de estudo e avaliação

Ritmo de cada aula de 60–90 minutos:

1. **10–15 min — entendimento:** objetivo, formato dos dados, documentação da API e conceito do Pandas.
2. **15–20 min — código guiado:** executar um exemplo curto e explicar cada transformação.
3. **25–35 min — exercícios:** construir sem olhar solução.
4. **10–15 min — desafio:** combinar conceitos e lidar com casos de borda.
5. **5 min — registro:** escrever o que aprendeu, dúvidas, comandos novos e decisões.

Rubrica: resultados corretos (40%), uso apropriado de Pandas (25%), clareza e organização (20%), explicação das decisões (15%). Avançar preferencialmente após atingir 8/10, sem rigidez artificial.

## 5. AULA 1 — Consumir uma API REST e criar DataFrames

### Objetivos

Ao final desta aula você deverá conseguir:

- executar uma requisição GET com parâmetros e timeout;
- verificar falhas HTTP antes de processar a resposta;
- localizar dados úteis em um JSON aninhado;
- construir um DataFrame com dados reais;
- identificar linhas, colunas, tipos e valores ausentes;
- explicar como separar responsabilidades entre coleta e análise.

### Parte A — Geocoding: nome de cidade → coordenadas

Crie `src/aula01.py`:

```python
import requests
import pandas as pd

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name": "São José dos Campos",
    "count": 10,
    "language": "pt",
    "countryCode": "BR",
}

response = requests.get(GEOCODING_URL, params=params, timeout=20)
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
```

**Atenção:** o retorno pode oferecer mais de uma localidade; confira estado e país antes de escolher coordenadas. O código acima demonstra descoberta e inspeção, não confirma automaticamente qual registro selecionar. Se quiser usar outra cidade, altere `name`.

### Parte B — Historical Weather: coordenadas → registros diários

Depois de inspecionar e confirmar a localidade correta, preencha `LATITUDE` e `LONGITUDE` com os valores obtidos na parte A. Na primeira execução, **não copie cegamente o primeiro resultado**.

```python
import requests
import pandas as pd

ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"

LATITUDE = -23.19   # exemplo aproximado; substitua pela resposta conferida
LONGITUDE = -45.88  # exemplo aproximado; substitua pela resposta conferida

params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "start_date": "2025-01-01",
    "end_date": "2025-03-31",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Sao_Paulo",
}

response = requests.get(ARCHIVE_URL, params=params, timeout=30)
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
```

**Nota de modelagem:** as datas do exemplo referem-se a 2025 para garantir um período histórico completo; os valores são obtidos dinamicamente na execução. O retorno pode diferir conforme revisões da fonte, e nulos devem ser investigados antes de calcular métricas.

### Parte C — Entenda os objetos antes de resolver

- `response`: objeto de resposta HTTP de `requests`.
- `payload`: dicionário Python recebido após decodificar JSON.
- `payload["daily"]`: dicionário que contém arrays por variável, inclusive datas.
- `df`: DataFrame criado a partir desse conjunto de arrays.
- `df["time"]`: Series com datas após conversão.
- `df.shape`: tupla `(linhas, colunas)`.
- `df.dtypes`: tipos das colunas.

### Exercícios — sem gabarito

**Exercício 1 — Exploração (fácil)**

1. Mostre as primeiras 7 linhas do histórico.
2. Mostre as últimas 5 linhas.
3. Informe quantidade de linhas e colunas.
4. Imprima apenas nomes e tipos de colunas.
5. Explique por que a coluna `time` deve ser convertida.

**Exercício 2 — Seleção (fácil/médio)**

1. Selecione apenas as colunas `time` e `temperature_2m_max`.
2. Exiba apenas as 10 primeiras observações dessas duas colunas.
3. Extraia a coluna `precipitation_sum` como Series.
4. Confirme em código a diferença entre Series e DataFrame.

**Exercício 3 — Análise (médio)**

1. Calcule a temperatura máxima e mínima do período.
2. Calcule a média das temperaturas máximas.
3. Calcule a precipitação acumulada, tratando eventuais nulos conscientemente.
4. Identifique a data com a maior temperatura máxima.
5. Explique quais cálculos poderiam ser distorcidos por valores ausentes.

**Exercício 4 — Qualidade dos dados (médio)**

1. Conte valores ausentes em cada coluna.
2. Verifique se a coluna `time` tem datas duplicadas.
3. Confira a quantidade de dias esperados no período solicitado.
4. Verifique se o número de registros corresponde ao esperado, sem assumir que a API sempre entrega uma série perfeita.

**Desafio 5 — Reutilização (difícil)**

Crie uma função `obter_historico(latitude, longitude, data_inicio, data_fim)` que:

- consulta a API;
- verifica os erros de requisição;
- retorna um DataFrame com as datas convertidas;
- detecta ausência da chave `daily`;
- não mistura impressão com retorno de dados;
- permite consultar outras cidades sem alterar a lógica principal.

**Desafio extra — Raciocínio técnico**

Compare conceitualmente:

```python
coluna = df["temperature_2m_max"]
coluna = coluna + 1
```

versus

```python
df["temperature_2m_max"] = df["temperature_2m_max"] + 1
```

O DataFrame original é alterado em ambos os casos? Explique e valide por execução. Considere também as implicações de unidades meteorológicas ao alterar um dado.

### Como entregar a Aula 1

Envie `src/aula01.py` e, se quiser, um pequeno `README.md` respondendo:

1. Qual endpoint foi consultado?
2. Qual cidade e qual período?
3. Quais colunas vieram na resposta?
4. Que problemas de qualidade encontrou?
5. Que parte foi mais difícil e por quê?

O código será revisado em correção, uso idiomático do Pandas, modularidade, validação e legibilidade. **Não há gabarito neste arquivo de propósito.**

## 6. Projetos progressivos e definição de pronto

### Projeto 1 — Comparador de clima (fim da semana 4)

- Coleta real de 3 cidades em período configurável;
- dataset único com cidade e data;
- eliminação de duplicatas justificadas;
- tipos e nulos auditados;
- exportação CSV e relatório com explicação.

### Projeto 2 — Relatório analítico automático (fim da semana 6)

- Médias, medianas, extremos, totais e agregações por mês;
- tabelas dinâmicas e gráficos;
- integração com metadados;
- Excel final com abas e cabeçalhos legíveis.

### Projeto 3 — Pipeline de produção (fim da semana 8)

- Requisições com validação e falhas explícitas;
- carga incremental e idempotente em PostgreSQL;
- funções separadas por responsabilidade;
- testes automatizados sem necessidade de internet;
- métricas, gráficos, relatório e instruções de execução.

## 7. Material de referência

- Pandas — primeiros passos: https://pandas.pydata.org/docs/getting_started/index.html
- Pandas — guia do usuário: https://pandas.pydata.org/docs/user_guide/index.html
- Requests — documentação: https://requests.readthedocs.io/en/latest/
- Open-Meteo Geocoding: https://open-meteo.com/en/docs/geocoding-api
- Open-Meteo Historical Weather: https://open-meteo.com/en/docs/historical-weather-api
- Pytest: https://docs.pytest.org/

**Próximo passo:** execute a Parte A e a Parte B da Aula 1; depois resolva o Exercício 1 sem consultar gabarito. Envie seu código para revisão antes de avançarmos.
