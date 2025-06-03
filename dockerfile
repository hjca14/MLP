FROM python:3.10-slim

# Copia o requirements.txt antes para aproveitar cache do Docker
COPY requirements.txt /tmp/requirements.txt

# Instalar dependências Python
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# Cria diretório para o modelo
RUN mkdir -p /models/classificador-produto/

# Copia arquivos do modelo
COPY model-settings.json /models/classificador-produto/
COPY model.pkl /models/classificador-produto/

# Expõe a porta padrão do MLServer
EXPOSE 8080

# Comando para iniciar o MLServer
CMD ["mlserver", "start", "/models/classificador-produto"]
