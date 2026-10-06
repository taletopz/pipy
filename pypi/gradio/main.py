import gradio as gr
import random

nomes = [
    "Kael", "Luna", "Raven", "Akira", "Dante",
    "Mika", "Zero", "Nox", "Yuki", "Kira"
]

classes = [
    "Guerreiro", "Mago", "Arqueiro",
    "Assassino", "Curandeiro", "Cavaleiro"
]

armas = [
    "Espada", "Arco", "Katana",
    "Machado", "Cajado", "Adagas"
]

habilidades = [
    "Fúria Sombria",
    "Raio de Gelo",
    "Explosão Arcana",
    "Corte Fantasma",
    "Cura Divina",
    "Tempestade de Fogo"
]


def gerar_personagem():
    nome = random.choice(nomes)
    classe = random.choice(classes)
    arma = random.choice(armas)
    habilidade = random.choice(habilidades)
    nivel = random.randint(1, 100)

    resultado = f"""
# Personagem Sorteado

Nome: {nome}

Classe: {classe}

Arma: {arma}

Habilidade: {habilidade}

Nível: {nivel}
"""

    return resultado


interface = gr.Interface(
    fn=gerar_personagem,
    inputs=[],
    outputs=gr.Markdown(),
    title="Gerador Aleatório de Personagem",
    description="Clique no botão para criar um personagem aleatório."
)

interface.launch()