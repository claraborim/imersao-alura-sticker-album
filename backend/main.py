from fastapi import FastAPI

# Cria instância FastAPI
app = FastAPI()

# Define endpoint para o método GET
@app.get("/")
def hello_world():
    return {"mensagem": "Olá, mundo! 🌍"}