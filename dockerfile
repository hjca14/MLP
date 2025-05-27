# Usamos uma imagem oficial do Jupyter com várias libs de Data Science já instaladas
FROM jupyter/scipy-notebook:latest

# Mantemos a autoria da personalização
LABEL maintainer="seuemail@example.com"

# Atualizamos o sistema e instalamos o XGBoost
# - Aproveitamos que o scipy-notebook já vem com miniconda
# - Instalamos xgboost via conda para evitar conflitos
RUN conda install --yes xgboost

# Criamos um diretório adicional para organizar nossos notebooks
RUN mkdir -p /home/jovyan/my_notebooks

# Definimos o diretório de trabalho padrão
WORKDIR /home/jovyan/my_notebooks

# Expondo a porta padrão do Jupyter
EXPOSE 8888

# O comando de entrada permanece o padrão da imagem
