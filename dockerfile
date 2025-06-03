FROM python:3.10-slim

# Copia o requirements.txt antes para aproveitar cache do Docker
COPY requirements.txt /tmp/requirements.txt

# Instalar dependências Python
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# Instalar nginx e supervisord
RUN apt-get update && \
    apt-get install -y nginx supervisor && \
    rm -rf /var/lib/apt/lists/*

# Cria diretório para o modelo
RUN mkdir -p /models/classificador-produto/

# Copia arquivos do modelo
COPY model-settings.json /models/classificador-produto/
COPY model.pkl /models/classificador-produto/

# Copiar index.html para servir
COPY index.html /usr/share/nginx/html/index.html

# Copiar config do supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expor portas
EXPOSE 5000
EXPOSE 80

# Comando para iniciar ambos
CMD ["/usr/bin/supervisord"]
