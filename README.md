# Ambiente de Machine Learning com Jupyter - Docker

Este projeto cria um ambiente Docker para desenvolvimento em Machine Learning, baseado na imagem `jupyter/scipy-notebook`. Personalizamos a imagem para incluir a biblioteca `xgboost` e criamos um diretório padrão para armazenar notebooks.

## Personalizações realizadas

- Instalação da biblioteca `xgboost` via conda.
- Criação da pasta `/home/jovyan/my_notebooks` para organização de arquivos.
- Exposição da porta 8888 para acesso ao Jupyter Notebook.

## Como executar

### 1. Clone este repositório

```bash
git clone https://github.com/hjca14/MLP.git
cd MLP
git checkout EML1.1
``` 

### 2. Construa a imagem Docker
```bash
docker build -t hjca14/ml-jupyter:latest .
```

### 3. Execute o container
```bash
docker run -p 8888:8888 hjca14/ml-jupyter:latest
```

### 4. Acesse o Jupyter Notebook
Abra no navegador: http://localhost:8888 e use o token que aparecer no terminal do container.

Ou use direto o link que aparece no terminal.

## Link para a imagem no Docker Hub
https://hub.docker.com/r/hjca14/ml-jupyter

## Link para esta branch do projeto no GitHub
https://github.com/hjca14/MLP/tree/EML1.1