
# Entrega Contínua (CD)
- Build automático de imagem Docker.

- Publicação no Docker Hub após push para os branches principais.

---

### Pipeline no GitHub Actions

O pipeline roda automaticamente em cada push ou pull request no branch `EML2.2`.

- A imagem Docker é automaticamente:
  - Buildada.
  - Publicada no Docker Hub como:
    - docker pull hjca14/classificacao-produto:latest

--------------------------------------------------------------------------------------------------

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

### Rodar com Docker *atualizado com CD*:
```bash
    docker pull hjca14/classificacao-produto:latest
    docker run -p 5000:5000 hjca14/classificacao-produto:latest
```
#### A API estará disponível em:
 http://localhost:5000


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