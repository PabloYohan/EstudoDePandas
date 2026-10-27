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

No Windows, ative com `.venv\\\Scripts\\\activate` (PowerShell: `.venv\\\Scripts\\\Activate.ps1`).

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

## 7. Material de referência

- Pandas — primeiros passos: https://pandas.pydata.org/docs/getting_started/index.html
- Pandas — guia do usuário: https://pandas.pydata.org/docs/user_guide/index.html
- Requests — documentação: https://requests.readthedocs.io/en/latest/
- Open-Meteo Geocoding: https://open-meteo.com/en/docs/geocoding-api
- Open-Meteo Historical Weather: https://open-meteo.com/en/docs/historical-weather-api
- Pytest: https://docs.pytest.org/

**Próximo passo:** execute a Parte A e a Parte B da Aula 1; depois resolva o Exercício 1 sem consultar gabarito. Envie seu código para revisão antes de avançarmos.
