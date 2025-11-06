# 🧩 Financial Clients API (Flask + Python)

## 🚀 Overview

This project implements a **REST API** built with **Flask** to manage and query financial client data, along with a **Python client script (`client.py`)** that consumes the API via HTTP requests.  

The solution allows users to search for clients by **ID or name**, displaying information about **accounts, cards, balances, limits**, and **personalized news** — simulating a simple banking data system.

---

## 🏗️ Project Structure

```
Pipeline ETL/
│
├── app.py                    # Flask API with endpoints
├── client.py                 # Python client to consume the API
├── clientes_financeiros.csv  # Simulated dataset
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Technologies Used

- 🐍 **Python 3.10+**
- 🌶️ **Flask** — Web framework for building APIs  
- 🌐 **Requests** — HTTP client for API consumption  
- 🧠 **Pandas** — Data handling and processing  
- 💻 **Threading** — Parallel server execution  

---

## 🔧 Setup & Execution

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/financial-clients-api.git
cd financial-clients-api
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # (Windows)
source .venv/bin/activate  # (Linux/Mac)
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask API

```bash
python app.py
```

Expected output:

```
Running on http://127.0.0.1:5050
```

### 5️⃣ Run the client script in another terminal

```bash
python client.py
```

---

## 📡 Available Endpoints

### 🔹 `GET /`
Health check endpoint — confirms the API is running.  
**Response:**
```
🚀 Flask API running! Use /users/<id> or /users?name=<name>.
```

### 🔹 `GET /users`
Returns all clients.

### 🔹 `GET /users?name=<name>`
Returns clients filtered by name (case-insensitive search).

### 🔹 `GET /users/<id>`
Returns detailed information about a specific client by ID.

---

## 🧠 Example Output

When running `client.py`, you’ll be prompted to enter one or more client IDs, and the results will be displayed with one client per line, for example:

```
Client ID: 7 | Name: Cliente_007 | Balance: 12.5
Client ID: 8 | Name: Cliente_008 | Balance: 250.0
Client ID: 9 | Name: Cliente_009 | Balance: 5.75
```

---

## 💬 Author

Developed by **Daniel Santana** — Data Analyst & Python Developer  
📧 your.email@example.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/your-link)
