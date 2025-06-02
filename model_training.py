from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Dataset de exemplo
descricoes = [
    'Tênis esportivo confortável',
    'Calça jeans masculina',
    'Notebook gamer potente',
    'Blusa de lã feminina',
    'Smartphone de última geração'
]

categorias = [
    'Calçados',
    'Roupas',
    'Eletrônicos',
    'Roupas',
    'Eletrônicos'
]

# Vetorização
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(descricoes)

# Modelo
modelo = LogisticRegression()
modelo.fit(X, categorias)

# Salva o modelo e o vetor
joblib.dump((modelo, vectorizer), 'modelo.pkl')

print("Modelo treinado e salvo com sucesso!")
