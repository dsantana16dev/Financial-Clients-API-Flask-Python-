import requests

# ==========================================
# Configuração da API
# ==========================================
BASE_URL = "http://127.0.0.1:5050/users"

# ==========================================
# Entrada de dados
# ==========================================
ids_input = input("Digite o(s) ID(s) dos clientes (separados por vírgula): ")
ids = [i.strip() for i in ids_input.split(",") if i.strip()]

# ==========================================
# Consulta e exibição
# ==========================================
for client_id in ids:
    try:
        response = requests.get(f"{BASE_URL}/{client_id}")
        
        if response.status_code == 200:
            data = response.json()
            
            print("\n--- Cliente Encontrado ---")
            print(f"🆔 ID: {data.get('id', 'N/A')}")
            print(f"👤 Nome: {data.get('name', 'N/A')}")
            print(f"🏦 Agência: {data.get('account.agency', 'N/A')}")
            print(f"💳 Conta: {data.get('account.number', 'N/A')}")
            print(f"💰 Saldo: {data.get('account.balance', 'N/A')}")
            print(f"💰 Limite: {data.get('account.limit', 'N/A')}")
            print(f"💳 Cartão: {data.get('card.number', 'N/A')}")
            print(f"💳 Limite Cartão: {data.get('card.limit', 'N/A')}")
            print(f"📰 Notícia: {data.get('news.description', 'N/A')}")
            print("------------------------------")
        else:
            print(f"\n❌ Cliente com ID {client_id} não encontrado. (status {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"\n⚠️ Erro ao consultar o cliente {client_id}: {e}")