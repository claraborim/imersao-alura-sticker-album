import os
import glob

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Cria instância FastAPI
app = FastAPI()

# CORS: Libera o acesso da API para qualquer origem, permitindo que o frontend consiga consumir os endpoints
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define o path para a pasta "figurinhas"
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# imagem_url aponta para o endpoint dedicado que entrega a imagem de cada figurinha (/figurinhas/{id}/imagem), em vez de expor a pasta de imagens diretamente via StaticFiles.
figurinhas = [
    {
        "id": "1",
        "nome": "Cowboy Bebop",
        "categoria": "TV",
        "imagem_url": "/figurinhas/1/imagem"
    },
    {
        "id": "2",
        "nome": "Dorohedoro",
        "categoria": "TV",
        "imagem_url": "/figurinhas/2/imagem"
    },
    {
        "id": "3",
        "nome": "Sociedade dos Poetas Mortos",
        "categoria": "TV",
        "imagem_url": "/figurinhas/3/imagem"
    },
    {
        "id": "4",
        "nome": "Serial Experiments Lain",
        "categoria": "TV",
        "imagem_url": "/figurinhas/4/imagem"
    },
    {
        "id": "5",
        "nome": "Friends",
        "categoria": "TV",
        "imagem_url": "/figurinhas/5/imagem"
    },
    {
        "id": "6",
        "nome": "Tibia",
        "categoria": "Jogos",
        "imagem_url": "/figurinhas/6/imagem"
    },
    {
        "id": "7",
        "nome": "Need for Speed: Underground 2",
        "categoria": "Jogos",
        "imagem_url": "/figurinhas/7/imagem"
    },
    {
        "id": "8",
        "nome": "Stardew Valley",
        "categoria": "Jogos",
        "imagem_url": "/figurinhas/8/imagem"
    },
    {
        "id": "9",
        "nome": "Club Penguin",
        "categoria": "Jogos",
        "imagem_url": "/figurinhas/9/imagem"
    },
    {
        "id": "10",
        "nome": "Pokémon FireRed",
        "categoria": "Jogos",
        "imagem_url": "/figurinhas/10/imagem"
    },
    {
        "id": "11",
        "nome": "Floral Green",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/figurinhas/11/imagem"
    },
    {
        "id": "12",
        "nome": "Arthur Verocai",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/figurinhas/12/imagem"
    },
    {
        "id": "13",
        "nome": "Igor",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/figurinhas/13/imagem"
    },
    {
        "id": "14",
        "nome": "MM..Food",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/figurinhas/14/imagem"
    },
    {
        "id": "15",
        "nome": "I Let It In And It Took Everything",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/figurinhas/15/imagem"
    },
    {
        "id": "16",
        "nome": "Maus",
        "categoria": "Livros",
        "imagem_url": "/figurinhas/16/imagem"
    },
    {
        "id": "17",
        "nome": "A Menina do Outro Lado",
        "categoria": "Livros",
        "imagem_url": "/figurinhas/17/imagem"
    },
    {
        "id": "18",
        "nome": "Modernidade Líquida",
        "categoria": "Livros",
        "imagem_url": "/figurinhas/18/imagem"
    },
    {
        "id": "19",
        "nome": "Meu Ano de Descanso e Relaxamento",
        "categoria": "Livros",
        "imagem_url": "/figurinhas/19/imagem"
    },
    {
        "id": "20",
        "nome": "Matéria Escura",
        "categoria": "Livros",
        "imagem_url": "/figurinhas/20/imagem"
    },
    {
        "id": "21",
        "nome": "Stratocaster Giannini G-101",
        "categoria": "Inventário",
        "imagem_url": "/figurinhas/21/imagem"
    },
    {
        "id": "22",
        "nome": "ThinkPad T480",
        "categoria": "Inventário",
        "imagem_url": "/figurinhas/22/imagem"
    },
    {
        "id": "23",
        "nome": "PSP 1000",
        "categoria": "Inventário",
        "imagem_url": "/figurinhas/23/imagem"
    },
    {
        "id": "24",
        "nome": "Edifier W800BT Plus",
        "categoria": "Inventário",
        "imagem_url": "/figurinhas/24/imagem"
    },
    {
        "id": "25",
        "nome": "Agatha Christie",
        "categoria": "Inventário",
        "imagem_url": "/figurinhas/25/imagem"
    },
    {
        "id": "26",
        "nome": "Xanim",
        "categoria": "Animais",
        "imagem_url": "/figurinhas/26/imagem"
    },
    {
        "id": "27",
        "nome": "Pietrovisk",
        "categoria": "Animais",
        "imagem_url": "/figurinhas/27/imagem"
    },
    {
        "id": "28",
        "nome": "Dogo Bartolo Zika",
        "categoria": "Animais",
        "imagem_url": "/figurinhas/28/imagem"
    },
    {
        "id": "29",
        "nome": "Loro José",
        "categoria": "Animais",
        "imagem_url": "/figurinhas/29/imagem"
    },
    {
        "id": "30",
        "nome": "Gatos Urbanos",
        "categoria": "Animais",
        "imagem_url": "/figurinhas/30/imagem"
    },
]

# Define endpoint para listar figurinhas cadastradas
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# Define endpoint para entregar a imagem de uma figurinha específica
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos_encontrados = glob.glob(padrao)

    if not arquivos_encontrados:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    return FileResponse(arquivos_encontrados[0])