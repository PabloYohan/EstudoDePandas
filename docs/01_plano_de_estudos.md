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

### Principal — Banco Central do Brasil, SGS (API REST JSON)

- **SGS 433 — IPCA:** variação **mensal** em %, própria para diagnóstico e análise inicial.
- **SGS 432 — Meta Selic definida pelo Copom:** série **diária** de taxa expressa em **% ao ano**; não somar os valores diários.
- **SGS 11 — Selic efetiva:** série diária divulgada em **% ao dia**; opcional, para comparações posteriores. Não confundir com a SGS 432.

**URL base:** `https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados`

**Parâmetros:** `formato=json`, `dataInicial=dd/MM/yyyy` e `dataFinal=dd/MM/yyyy`. Exemplo (IPCA):
```text
https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2025
```

**Formato esperado:** lista JSON com campos `data` e `valor`. Confirme os tipos retornados (datas e valores podem vir como texto). Para séries diárias, respeite o limite de até 10 anos por consulta e os filtros obrigatórios publicados pelo BCB. Séries têm frequências diferentes; validar dados por frequência, e não assumir observação em todo dia do calendário.

### Complementar — Banco Central, PTAX (Olinda/OData)

- Cotações de compra e venda de moedas, incluindo USD/BRL, por data ou intervalo.
- Fonte usada nas aulas de integração (16–18) e projetos 2 e 3.
- **Formato:** resposta OData com coleção `value`; parâmetros e boletins devem ser verificados na documentação.
- **Documentação:** [https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/documentacao](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/documentacao)

### Complementar opcional — CVM, Dados Abertos

- Informes diários de fundos em arquivos CSV/ZIP, para extensão após o curso; **não** é a API principal nem pré-requisito das 24 aulas.
- [https://dados.cvm.gov.br/dataset/fi-doc-inf_diario](https://dados.cvm.gov.br/dataset/fi-doc-inf_diario)

**Projeto contínuo:** monitor de indicadores macroeconômicos brasileiros (IPCA, Selic meta e, depois, PTAX), preservando unidades, frequência, fonte e períodos de publicação. O foco é engenharia e análise de dados, não recomendações de investimento.

**Fluxo:** HTTP GET → status/JSON → DataFrame → tipagem/qualidade → análise → integração → Excel/SQL → testes.

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

Prática: Consultar série SGS 433 (IPCA mensal); auditar estrutura, valores e competência.

Entrega: relatório rápido de integridade da coleta.

**Aula 3. Seleção de linhas e colunas**

Conteúdo: `loc`, `iloc`, Series versus DataFrame, índices, atribuição correta, `copy`.

Prática: consultar intervalos e variáveis selecionadas.

Entrega: seleção parametrizada por coluna e período.

**Checkpoint:** explicar a diferença entre JSON aninhado, Series e DataFrame, além de identificar tipos incorretos antes de analisar.

### Semana 2 — Consultas e transformação

**Aula 4. Filtros eficientes**

Conteúdo: máscaras booleanas, `query`, `between`, `isin`, `&`, `|`, `sort_values`.

Prática: Identificar meses de inflação mais alta/baixa e faixas de variação.

Entrega: funções de filtragem com parâmetros.

**Aula 5. Colunas derivadas e vetorização**

Conteúdo: atribuição, `assign`, operações entre colunas, condições com `where`, `mask`, `np.select` (opcional).

Prática: Criar faixas de inflação e diferenças em pontos percentuais.

Entrega: conjunto de indicadores derivados sem loops por linha.

**Aula 6. Tipos e conversões**

Conteúdo: `astype`, `to_numeric`, `to_datetime`, tipos anuláveis, coerção segura.

Prática: Converter datas dd/MM/yyyy e valores de texto da API SGS.

Entrega: função reutilizável de tipagem.

**Checkpoint:** construir consultas parametrizadas e justificar escolhas de tipos.

### Semana 3 — Qualidade de dados

**Aula 7. Valores ausentes e consistência**

Conteúdo: `isna`, `dropna`, `fillna`, cobertura, validação de faixa e a diferença entre dado ausente e zero.

Prática: Diferenciar mês não publicado, nulo e inflação efetivamente zero.

Entrega: relatório de qualidade com percentual de nulos por coluna.

**Aula 8. Duplicatas e chaves**

Conteúdo: `duplicated`, `drop_duplicates`, chaves compostas, cardinalidade e unicidade.

Prática: Consolidar extrações sobrepostas; validar chave (serie_sgs, data).

Entrega: dataset com chave `(cidade, data)` validada.

**Aula 9. Strings e normalização**

Conteúdo: `.str`, `strip`, `lower`, `replace`, regex, tratamento de nomes e códigos.

Prática: Padronizar nomes de indicadores, fontes e códigos SGS.

Entrega: tabela padronizada de localidades.

### Semana 4 — Datas e projeto intermediário

**Aula 10. Datas e séries temporais**

Conteúdo: `.dt`, fuso horário, ordenação, índices temporais, períodos, `resample`.

Prática: produzir indicadores mensais de um histórico diário.

Entrega: relatório mensal com série temporal consistente.

**Aula 11. Coleta de múltiplas cidades**

Conteúdo: funções, composição de requests, respostas heterogêneas, `concat`, logs de erros, rate limiting responsável.

Prática: Consultar SGS 433 (IPCA) e SGS 432 (Selic meta), preservando frequência e unidade.

Entrega: dataset unificado de localidades.

**Aula 12. Mini-projeto 1: monitor macroeconômico**

Conteúdo: filtros, tipos, validação, concatenação e datas.  

Prática: Publicar painel tabular de inflação e Selic com frequência explícita.  

Entrega: CSV limpo, relatório Markdown e qualidade da base.

### Semana 5 — Agregações analíticas

**Aula 13. GroupBy**

Conteúdo: `groupby`, `sum`, `mean`, `median`, `count`, `size`, `nunique`.

Prática: Indicadores por ano, série e mês — com agregações apropriadas.

Entrega: tabela comparativa.

**Aula 14. Agregações avançadas**

Conteúdo: `agg` nomeado, `transform`, `rank`, acumulados e rolling windows.

Prática: Construir inflação acumulada por composição e médias móveis contextualizadas.

Entrega: indicadores calculados vetorialmente.

**Aula 15. Tabelas dinâmicas e visualização**

Conteúdo: `pivot_table`, `crosstab`, tabelas por período e gráficos com Pandas/Matplotlib.

Prática: Gráficos de IPCA e Selic, com escala e unidade indicadas.

Entrega: gráficos reproduzíveis com explicações.

### Semana 6 — Integração de fontes

**Aula 16. Merge e joins**

Conteúdo: `merge`, tipos de join, `validate`, `indicator`, cardinalidade e perdas por chave.

Prática: Relacionar IPCA, Selic e PTAX por competência definida, sem join ingênuo de datas.

Entrega: merge auditável sem multiplicações de linhas indevidas.

**Aula 17. Reformatação e concatenação**

Conteúdo: `concat`, `melt`, `pivot`, `stack`, `explode`, normalização de JSON.

Prática: Normalizar retorno SGS (lista de registros) e PTAX (objeto com value).

Entrega: dados em formato tidy (cada observação em uma linha).

**Aula 18. Entrada e saída de arquivos**

Conteúdo: `read_csv`, `read_excel`, `to_csv`, `to_excel`, Parquet (opcional), codificação, precisão e preservação de tipos.

Prática: Exportar séries, metadados e indicadores para Excel.

Entrega: relatório Excel com abas de base e agregados.

### Semana 7 — Persistência e arquitetura

**Aula 19. Pandas + PostgreSQL**

Conteúdo: SQLAlchemy, conexão, `read_sql`, `to_sql`, tipos SQL, carga incremental e idempotência.

Prática: Persistir séries com chave (codigo_sgs, data) ou cotação com chave própria.

Entrega: tabela SQL sem duplicatas e consultas verificáveis.

**Aula 20. Pipeline ETL modular**

Conteúdo: separar extração, transformação e carga; configuração; logs; `try/except`; tentativas com limites e tratamento de falhas HTTP.

Prática: Pipeline BCB SGS e PTAX com tratamento de erros e limites.

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

Conteúdo: indicadores, gráficos, rastreabilidade e exportação.

Prática: Relatório macroeconômico reproduzível com atualização e cobertura.

Entrega: relatório e datasets finais.

**Aula 24. Projeto final: pipeline de dados completo**

Conteúdo: integração, qualidade, banco, testes e publicação.  

Prática: Coletar IPCA, Selic meta e PTAX em período definido; respeitar calendários e unidades. 
 
Entrega: Repositório documentado, PostgreSQL, Excel, gráficos e relatório.

## 4. Método de estudo e avaliação

Ritmo de cada aula de 60–90 minutos:

1. **10–15 min — entendimento:** objetivo, formato dos dados, documentação da API e conceito do Pandas.

2. **15–20 min — código guiado:** executar um exemplo curto e explicar cada transformação.

3. **25–35 min — exercícios:** construir sem olhar solução.

4. **10–15 min — desafio:** combinar conceitos e lidar com casos de borda.

5. **5 min — registro:** escrever o que aprendeu, dúvidas, comandos novos e decisões.

Rubrica: resultados corretos (40%), uso apropriado de Pandas (25%), clareza e organização (20%), explicação das decisões (15%). Avançar preferencialmente após atingir 8/10, sem rigidez artificial.

## 7. Material de referência

- [Pandas — primeiros passos](https://pandas.pydata.org/docs/getting_started/index.html)
- [Pandas — User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [BCB — SGS 432 / Meta Selic](https://dadosabertos.bcb.gov.br/dataset/432-taxa-de-juros---meta-selic-definida-pelo-copom)
- [BCB — SGS 11 / Selic efetiva](https://dadosabertos.bcb.gov.br/dataset/11-taxa-de-juros---selic)
- [BCB — catálogo de dados abertos](https://dadosabertos.bcb.gov.br/)
- [BCB — PTAX](https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios)
- [CVM — fundos](https://dados.cvm.gov.br/dataset/fi-doc-inf_diario)
- [Pytest](https://docs.pytest.org/)

**Próximo passo:** realizar a Aula 2 com SGS 433. Manter `03_aula_01.md` e `aula01.py` originais intactos.
