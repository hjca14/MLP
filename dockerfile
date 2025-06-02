# Imagem base oficial Python
FROM python:3.10

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos
COPY . .

# Instala dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Executa o treinamento na build
RUN python model_training.py

# Comando padrão
CMD ["python", "app.py"]
