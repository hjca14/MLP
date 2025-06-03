import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups

# Carrega dataset
categories = ['rec.autos', 'comp.sys.mac.hardware', 'sci.space']
newsgroups = fetch_20newsgroups(subset='train', categories=categories, remove=('headers', 'footers', 'quotes'))

# Cria pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB()),
])

# Treina modelo
pipeline.fit(newsgroups.data, newsgroups.target)

# Salva modelo
joblib.dump(pipeline, 'model.pkl')

print("Modelo treinado e salvo como model.pkl")
