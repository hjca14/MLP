# Usamos uma imagem oficial do Jupyter com várias libs de Data Science já instaladas
FROM jupyter/scipy-notebook:latest

# Mantemos a autoria da personalização
LABEL maintainer="hjca14@gmail.com"

# Atualizamos o sistema e instalamos o XGBoost
# - Aproveitamos que o scipy-notebook já vem com miniconda
# - Instalamos xgboost via conda para evitar conflitos
RUN conda install --yes --quiet -c conda-forge xgboost

# Criação de diretório para organização de notebooks
RUN mkdir -p /home/jovyan/my_notebooks

# Definimos o diretório de trabalho padrão
WORKDIR /home/jovyan/my_notebooks

# Expondo a porta padrão do Jupyter
EXPOSE 8888

# Comando padrão para iniciar o notebook
CMD ["start-notebook.sh"]
