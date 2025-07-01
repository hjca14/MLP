# Projeto: Coleta de Dados da API Pokémon
## Descrição
Este projeto tem como objetivo coletar, processar e armazenar informações da PokéAPI, utilizando um processo automatizado para ingestão de dados. Os dados extraídos são salvos em um banco de dados local (SQLite), com suporte para escalabilidade e armazenamento de longo prazo em nuvem.

## Funcionalidades
Lê URLs da API Pokémon a partir de um arquivo .txt

Extrai informações relevantes:

- ID
- Nome
- Tipo principal e secundário
- Altura
- Peso
- Quantidade de movimentos

Armazena os dados estruturados em uma base SQLite

## Organização
```graphql
MLP/
│
├── data/                      # Pasta de dados
│   └── urls.txt               # Arquivo com as URLs da PokéAPI
├── extrator.py                # Script principal de extração e persistência
├── database.db                # Banco de dados SQLite com os dados salvos
├── arquitetura.png            # Diagrama da arquitetura proposta
├── estimativa_aws.pdf         # Estimativa de custo anual detalhada (AWS Calculator)
└── README.md                  # Este arquivo
```
## Tecnologias utilizadas
Python 3.10

SQLite (via sqlite3)

requests para chamadas HTTP

AWS S3 + Glacier (estimativa teórica)

AWS Lambda (simulado no cálculo de custo)

# Execução
Instale as dependências:

```nginx
pip install -r requirements.txt
Execute o script:
```

```nginx
python extrator.py
```
O banco de dados database.db será criado na raiz do projeto com todos os dados estruturados.

## Armazenamento e Escalabilidade
A aplicação foi pensada para rodar cem vezes ao dia (volumetria aumentada em 100x), podendo ser escalada via AWS Lambda.

Os dados são armazenados por 1 ano, sendo acessados somente nos primeiros 6 meses.

Os dados antigos são transferidos para S3 Glacier Deep Archive para reduzir custos.

### Arquitetura
Veja o arquivo arquitetura.png para entender como o processo está estruturado.

### Estimativa de Custo (AWS)
O cálculo de custo com volumetria aumentada em 100x está disponível em estimativa_aws.pdf.

🟢 Custo anual estimado: ~$13.59 USD