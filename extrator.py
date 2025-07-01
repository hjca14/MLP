import requests
import sqlite3
from pathlib import Path
import time
from datetime import timedelta


# Caminhos
URLS_PATH = Path("data/urls.txt")
DB_PATH = "database.db"

# Criar tabela
def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            tipo_principal TEXT NOT NULL,
            tipo_secundario TEXT,
            altura INTEGER,
            peso INTEGER,
            qtd_movimentos INTEGER
        )
    """)
    conn.commit()

# Extrair dados de uma URL
def extrair_info(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro na URL: {url}")
        return None

    data = response.json()
    tipos = [t["type"]["name"] for t in data["types"]]
    tipo_principal = tipos[0]
    tipo_secundario = tipos[1] if len(tipos) > 1 else None

    return (
        data["id"],
        data["name"],
        tipo_principal,
        tipo_secundario,
        data["height"],
        data["weight"],
        len(data["moves"])
    )

# Salvar no banco
def salvar_pokemon(conn, dados):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO pokemon (
            id, nome, tipo_principal, tipo_secundario, altura, peso, qtd_movimentos
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, dados)
    conn.commit()

# Execução principal
def main():
    start = time.time()

    conn = sqlite3.connect(DB_PATH)
    criar_tabela(conn)

    with open(URLS_PATH, "r") as file:
        urls = [line.strip() for line in file.readlines() if line.strip()]

    for i, url in enumerate(urls, 1):
        dados = extrair_info(url)
        if dados:
            salvar_pokemon(conn, dados)
            #print(f"[{i}] Pokémon salvo: {dados[1]}")

    conn.close()

    end = time.time()
    elapsed = timedelta(seconds=end - start)
    print("Concluído!")
    print(f"Tempo de execução: {elapsed}")

if __name__ == "__main__":
    main()
