from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Vulnerabilidade proposital: chave secreta fixa no código (Bandit B105)
app.config['SECRET_KEY'] = 'supersecreta123'

DB_NAME = 'usuarios.db'


def get_db():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    return jsonify({'status': 'API de Cadastro rodando'})


@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    dados = request.json
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')

    conn = get_db()
    # Vulnerabilidade proposital: SQL Injection via f-string (Bandit B608)
    query = f"INSERT INTO usuarios (nome, email, senha) VALUES ('{nome}', '{email}', '{senha}')"
    conn.execute(query)
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Usuário cadastrado com sucesso'}), 201


@app.route('/usuarios/<usuario_id>', methods=['GET'])
def buscar_usuario(usuario_id):
    conn = get_db()
    # Vulnerabilidade proposital: SQL Injection via concatenação (Bandit B608)
    query = "SELECT id, nome, email FROM usuarios WHERE id = " + usuario_id
    resultado = conn.execute(query).fetchone()
    conn.close()

    if resultado:
        return jsonify({'id': resultado[0], 'nome': resultado[1], 'email': resultado[2]})
    return jsonify({'erro': 'Usuário não encontrado'}), 404


if __name__ == '__main__':
    init_db()
    # Vulnerabilidade proposital: modo debug ativo (Bandit B201)
    app.run(debug=True)
