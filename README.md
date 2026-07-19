# Clara's Archive

Álbum de figurinhas interativo com efeito de virar páginas, inspirado na estética de terminais e monitores CRT antigos. O projeto simula um álbum físico organizado por categorias, onde cada figurinha representa uma referência pessoal: tv, jogos, álbuns musicais, livros, itens do dia a dia e animais de estimação.

## Sobre o projeto

O álbum é composto por uma capa, seis páginas de conteúdo divididas por categoria e uma contracapa. A navegação entre as páginas é feita por arraste, clique nas setas laterais ou pelas teclas direcionais do teclado, com efeito sonoro sintetizado via Web Audio API simulando o som de papel sendo virado.

As figurinhas exibidas na interface são carregadas dinamicamente a partir de uma API própria, que serve tanto os dados de cada item quanto as imagens correspondentes.

## Funcionalidades

- Efeito de álbum com virada de páginas realista, incluindo arraste pelo mouse ou toque
- Tema visual inspirado em terminais e monitores CRT, com efeitos de flicker, scanlines e glow
- Preenchimento automático dos slots do álbum com imagens vindas da API
- Controle de som ativado ou desativado pelo usuário
- Layout responsivo, com adaptações para telas menores
- API própria em FastAPI para servir os dados e as imagens das figurinhas

## Tecnologias utilizadas

**Backend**
- Python 3.12
- FastAPI
- Uvicorn

**Frontend**
- HTML5
- CSS3
- JavaScript (Vanilla)
- Page Flip (biblioteca para o efeito de virar páginas)
- Web Audio API

## Estrutura do projeto

```
.
├── backend/
│   ├── figurinhas/
│   │   └── (imagens das figurinhas)
│   └── main.py
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── style.css
├── .gitignore
├── README.md
└── requirements.txt
```


A estrutura acima reflete a organização esperada do projeto. Ajuste os caminhos conforme a disposição real de pastas no seu repositório.

## Como executar o projeto

### Pré-requisitos

- Python 3.12 ou superior
- Navegador atualizado com suporte a Web Audio API

### Backend

1. Acesse a pasta do backend:
   ```
   cd backend
   ```

2. Crie um ambiente virtual (recomendado):
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux ou macOS
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Inicie o servidor:
   ```
   uvicorn main:app --reload
   ```

O servidor ficará disponível em `http://localhost:8000`.

### Frontend

O frontend é composto por arquivos estáticos e não exige build. Basta abrir o arquivo `index.html` diretamente no navegador ou servi-lo por qualquer servidor HTTP simples, mantendo o backend em execução simultaneamente para que as figurinhas sejam carregadas corretamente.

## Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/figurinhas` | Retorna a lista completa de figurinhas cadastradas |
| GET | `/figurinhas/{id}/imagem` | Retorna a imagem correspondente à figurinha informada |

## Créditos

Projeto desenvolvido durante a Imersão Arquitetura Web com IA, promovida pela Alura, em julho de 2026.