# API de Classificação de Categoria de Produto

## Descrição

Este software é uma **API de predição online** que, ao receber a descrição de um produto, responde com a categoria mais provável desse produto.  
O modelo foi treinado previamente utilizando técnicas de machine learning.

---

## Como configurar e executar

### Pré-requisitos:

- Docker instalado
- (Ou) Python 3.10 instalado com pip

---

### Rodar com Docker (Recomendado):

1. Clone o repositório:
```bash
    git clone https://github.com/hjca14/MLP.git
    cd MLP
    git checkout EML1.2
```

2. Construa a imagem Docker:
```bash
docker build -t classificacao-produto .
```

3. Execute o container:
```bash
docker run -p 5000:5000 classificacao-produto
```

### Rodar localmente (sem Docker):

1. Clone o repositório e acesse a pasta:
```bash
    git clone https://github.com/hjca14/MLP.git
    cd MLP
    git checkout EML1.2
```

2. Crie ambiente virtual (opcional mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Gere o modelo de machine learning:
```bash
python model_training.py
```

5. Execute a API:
```bash
python app.py
```

# Como utilizar a API
## Endpoint:
> POST /predizer_categoria

## Formato da requisição:
URL:
> http://localhost:5000/predizer_categoria

Headers:
> Content-Type: application/json

Body:

```json
{
  "descricao": "Calça jeans masculina"
}
```

### Resposta esperada:
```json
{
  "categoria": "Roupas"
}
```

## Exemplo usando Postman
![img.png](img.png)

## O que acontece na execução?
### Treinamento (model_training.py):
O modelo é treinado com descrições de produtos e salvo como modelo.pkl.

### Execução (app.py):
A API Flask é carregada e fica ouvindo na porta 5000.
Ao receber uma requisição POST no endpoint /predizer_categoria, ela retorna a categoria prevista.

## Serviços envolvidos
### Serviço de predição (API):
Único serviço rodando, exposto via HTTP na porta 5000.

## Entrada e saída detalhadas
| Tipo    | Formato       | Exemplo  |
| ------- | ---------- |---|
| Entrada | JSON  |  { "descricao": "Notebook gamer potente" } |
| Saída | JSON   | { "categoria": "Eletrônicos" }  |


## Para quem é este software?
Equipes de e-commerce que desejam automatizar a classificação de produtos.

Estudantes que querem entender como transformar um modelo de machine learning em uma API de produção.

## Observações importantes:
- O modelo foi treinado com um dataset simples de exemplo, podendo ser facilmente substituído por datasets reais.

- Não inclui persistência de dados (banco de dados) neste projeto.

- O foco foi a produtização do modelo como serviço.