🧩 Project: Financial Clients API (Flask + Python)
🚀 Overview

This project implements a REST API built with Flask to manage and query financial client data, along with a Python client script (client.py) that consumes the API via HTTP requests.
The solution allows users to search for clients by ID or name, displaying account, card, balance, limit, and personalized news information — simulating a simple banking data system.

🏗️ Project Structure
📂 Pipeline ETL/
│
├── app.py                   # Flask API with endpoints
├── client.py                # Python client to consume the API
├── clientes_financeiros.csv # Simulated dataset
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

⚙️ Technologies Used:
🐍 Python 3.10+
🌶️ Flask — web framework for building APIs
🌐 Requests — HTTP client for API consumption
🧠 Pandas — data handling and processing
💻 Threading — parallel server execution

🔧 Setup & Execution
Clone the repository
git clone https://github.com/your-username/financial-clients-api.git
cd financial-clients-api

Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate      # (Windows)
source .venv/bin/activate   # (Linux/Mac)

Install dependencies
pip install -r requirements.txt
Run the Flask API
python app.py

Expected output:
* Running on http://127.0.0.1:5050

Run the client script in another terminal
python client.py
📡 Available Endpoints
🔹 GET /

Health check endpoint — confirms the API is running.
Response:
🚀 Flask API running! Use /users/<id> or /users?name=<name>.
🔹 GET /users
Returns all clients.
🔹 GET /users?name=<name>
Returns clients filtered by name (case-insensitive search).
🔹 GET /users/<id>
Returns detailed information about a specific client by ID.
