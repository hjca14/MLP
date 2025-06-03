# Model Serving com MLServer - Classificador de Produto

## Descrição

Este projeto utiliza o **MLServer** para servir um modelo treinado com um dataset de categorias de produtos/notícias, utilizando `scikit-learn`.

---

## Como configurar e executar

### Pré-requisitos
- Docker instalado.

---

### Passos para rodar com Docker

1. Clone o repositório:
-- bash
git clone https://github.com/hjca14/MLP.git
cd MLP
git checkout EML3.1
--  

2. Gere o modelo (opcional, caso já exista o `model.pkl`):
-- bash
python model_training.py
--  

3. Construa a imagem Docker:
-- bash
docker build -t classificador-produto-mlserver .
--  

4. Execute o container:
-- bash
docker run -p 8080:8080 classificador-produto-mlserver
--  

---

## Como utilizar a API

A API REST do MLServer estará em:

> http://localhost:8080/v2/models/classificador-produto/infer

---

### Formato da requisição:

-- bash
curl -X POST http://localhost:8080/v2/models/classificador-produto/infer \
  -H "Content-Type: application/json" \
  -d '{
        "inputs": [
          {
            "name": "input-0",
            "shape": [1],
            "datatype": "BYTES",
            "data": ["Calça jeans masculina"]
          }
        ]
      }'
--  

---

### Resposta esperada:

-- json
{
  "model_name": "classificador-produto",
  "outputs": [
    {
      "name": "output-0",
      "shape": [1],
      "datatype": "BYTES",
      "data": ["Roupas"]
    }
  ]
}
--  

---

## Como usar via HTML

Abra `client.html` no navegador e envie a descrição do produto. A resposta aparecerá na tela.

---

## Observações importantes

- O modelo é baseado em `sklearn` e `TfidfVectorizer` + `MultinomialNB`.
- A API segue o padrão **V2 Dataplane** do **MLServer**.
- Pode-se trocar o modelo facilmente, bastando atualizar `model.pkl`.

