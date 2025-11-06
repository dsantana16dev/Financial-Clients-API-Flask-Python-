import pandas as pd
from flask import Flask, jsonify, request

# Inicializa o app Flask
app = Flask(__name__)

# Carrega o CSV com os dados dos clientes
df = pd.read_csv("clientes_financeiros.csv")

# 🏠 Rota inicial (teste)
@app.route('/')
def home():
    return "🚀 API Flask rodando! Use /users/<id> ou /users?ids=<lista>."

# 🔎 Buscar UM cliente pelo ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = df[df['id'] == user_id]
    if user.empty:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    return jsonify(user.to_dict(orient='records')[0])

# 🔁 Buscar VÁRIOS clientes (por lista de IDs)
@app.route('/users', methods=['GET'])
def get_users():
    ids_param = request.args.get('ids')  # exemplo: ?ids=4,5,6,...
    if ids_param:
        ids = [int(x) for x in ids_param.split(',')]
        users = df[df['id'].isin(ids)]
        if users.empty:
            return jsonify({'error': 'Nenhum usuário encontrado'}), 404
        return jsonify(users.to_dict(orient='records'))
    else:
        return jsonify(df.to_dict(orient='records'))  # retorna todos

# Executa o app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)

# Comandos PowerShell para gerenciar o servidor Flask
#para encerrar: Get-Process | findstr python
#para encerrar: Stop-Process -Name python -Force