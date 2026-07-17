import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Cria instância FastAPI
app = FastAPI()

# Define o path para a pasta "figurinhas"
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configura o staticfiles montando a pasta de imagens na rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

figurinhas = [
    {
        "id": "1",
        "nome": "Cowboy Bebop",
        "categoria": "TV",
        "imagem_url": "/imgs/01-cowboy-bebop.jpg"
    },
    {
        "id": "2",
        "nome": "Dorohedoro",
        "categoria": "TV",
        "imagem_url": "/imgs/02-dorohedoro.jpg"
    },
    {
        "id": "3",
        "nome": "Sociedade dos Poetas Mortos",
        "categoria": "TV",
        "imagem_url": "/imgs/03-sociedade-dos-poetas-mortos.jpg"
    },
    {
        "id": "4",
        "nome": "Serial Experiments Lain",
        "categoria": "TV",
        "imagem_url": "/imgs/04-serial-experiments-lain.jpg"
    },
    {
        "id": "5",
        "nome": "Friends",
        "categoria": "TV",
        "imagem_url": "/imgs/05-friends.jpg"
    },
    {
        "id": "6",
        "nome": "Tibia",
        "categoria": "Jogos",
        "imagem_url": "/imgs/06-tibia.jpg"
    },
    {
        "id": "7",
        "nome": "Need for Speed: Underground 2",
        "categoria": "Jogos",
        "imagem_url": "/imgs/07-need-for-speed-underground-2.jpg"
    },
    {
        "id": "8",
        "nome": "Stardew Valley",
        "categoria": "Jogos",
        "imagem_url": "/imgs/08-stardew-valley.png"
    },
    {
        "id": "9",
        "nome": "Club Penguin",
        "categoria": "Jogos",
        "imagem_url": "/imgs/09-club-penguin.jpg"
    },
    {
        "id": "10",
        "nome": "Pokémon FireRed",
        "categoria": "Jogos",
        "imagem_url": "/imgs/10-pokemon-fire-red.jpg"
    },
    {
        "id": "11",
        "nome": "Floral Green",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/imgs/11-floral-green.jpg"
    },
    {
        "id": "12",
        "nome": "Arthur Verocai",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/imgs/12-arthur-verocai.jpg"
    },
    {
        "id": "13",
        "nome": "Igor",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/imgs/13-igor.jpg"
    },
    {
        "id": "14",
        "nome": "MM..Food",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/imgs/14-mm-food.jpg"
    },
    {
        "id": "15",
        "nome": "I Let It In And It Took Everything",
        "categoria": "Álbuns Musicais",
        "imagem_url": "/imgs/15-i-let-it-in-and-it-took-everything.jpg"
    },
    {
        "id": "16",
        "nome": "Maus",
        "categoria": "Livros",
        "imagem_url": "/imgs/16-maus.jpg"
    },
    {
        "id": "17",
        "nome": "A Menina do Outro Lado",
        "categoria": "Livros",
        "imagem_url": "/imgs/17-a-menina-do-outro-lado.jpg"
    },
    {
        "id": "18",
        "nome": "Modernidade Líquida",
        "categoria": "Livros",
        "imagem_url": "/imgs/18-modernidade-liquida.png"
    },
    {
        "id": "19",
        "nome": "Meu Ano de Descanso e Relaxamento",
        "categoria": "Livros",
        "imagem_url": "/imgs/19-meu-ano-de-descanso-e-relaxamento.jpg"
    },
    {
        "id": "20",
        "nome": "Matéria Escura",
        "categoria": "Livros",
        "imagem_url": "/imgs/20-materia-escura.png"
    },
    {
        "id": "21",
        "nome": "Stratocaster Giannini G-101",
        "categoria": "Inventário",
        "imagem_url": "/imgs/21-stratocaster-giannini.PNG"
    },
    {
        "id": "22",
        "nome": "ThinkPad T480",
        "categoria": "Inventário",
        "imagem_url": "/imgs/22-thinkpad-t480.JPG"
    },
    {
        "id": "23",
        "nome": "PSP 1000",
        "categoria": "Inventário",
        "imagem_url": "/imgs/23-psp-1000.JPG"
    },
    {
        "id": "24",
        "nome": "Edifier W800BT Plus",
        "categoria": "Inventário",
        "imagem_url": "/imgs/24-edifier.jpg"
    },
    {
        "id": "25",
        "nome": "Agatha Christie",
        "categoria": "Inventário",
        "imagem_url": "/imgs/25-agatha-christie.jpg"
    },
    {
        "id": "26",
        "nome": "Xanim",
        "categoria": "Animais",
        "imagem_url": "/imgs/26-xanim.JPG"
    },
    {
        "id": "27",
        "nome": "Pietrovisk",
        "categoria": "Animais",
        "imagem_url": "/imgs/27-pietrovisk.JPG"
    },
    {
        "id": "28",
        "nome": "Dogo Bartolo Zika",
        "categoria": "Animais",
        "imagem_url": "/imgs/28-dogo-bartolo-zika.JPG"
    },
    {
        "id": "29",
        "nome": "Loro José",
        "categoria": "Animais",
        "imagem_url": "/imgs/29-loro-jose.JPG"
    },
    {
        "id": "30",
        "nome": "Gatos Urbanos",
        "categoria": "Animais",
        "imagem_url": "/imgs/30-gatos-urbanos.JPG"
    }
]

# Define endpoint para listar figurinhas cadastradas
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas