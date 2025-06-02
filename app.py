from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Carregar modelo
modelo, vectorizer = joblib.load('modelo.pkl')


@app.route('/predizer_categoria', methods=['POST'])
def predizer_categoria():
    data = request.json
    descricao = data.get('descricao', '')

    X = vectorizer.transform([descricao])
    categoria = modelo.predict(X)[0]

    return jsonify({'categoria': categoria})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
