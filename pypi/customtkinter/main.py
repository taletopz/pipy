import customtkinter as ctk
import random

# Configuração
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("VALORANT Assistant")
app.geometry("700x650")
app.resizable(False, False)

# Todos os agentes atuais
agentes = [
    "Astra",
    "Breach",
    "Brimstone",
    "Chamber",
    "Clove",
    "Cypher",
    "Deadlock",
    "Fade",
    "Gekko",
    "Harbor",
    "Iso",
    "Jett",
    "KAY/O",
    "Killjoy",
    "Miks",
    "Neon",
    "Omen",
    "Phoenix",
    "Raze",
    "Reyna",
    "Sage",
    "Skye",
    "Sova",
    "Tejo",
    "Veto",
    "Viper",
    "Vyse",
    "Waylay",
    "Yoru"
]

mapas = [
    "Ascent",
    "Bind",
    "Breeze",
    "Fracture",
    "Haven",
    "Icebox",
    "Lotus",
    "Pearl",
    "Split",
    "Sunset",
    "Abyss",
    "Corrode",
    "District",
    "Kasbah",
    "Piazza",
    "Drift",
    "Glimmer"
]

def sortear_agente():
    agente = random.choice(agentes)

    resultado.configure(
        text=f"AGENTE SORTEADO\n\n{agente}"
    )


def sortear_mapa():
    mapa = random.choice(mapas)

    resultado.configure(
        text=f"MAPA SORTEADO\n\n{mapa}"
    )


def sortear_tudo():
    agente = random.choice(agentes)
    mapa = random.choice(mapas)

    resultado.configure(
        text=f"SUA PARTIDA\n\n"
             f"Agente: {agente}\n"
             f"Mapa: {mapa}"
    )


def dica():
    dicas = [
        "Confira o minimapa constantemente.",
        "Não tenha pressa para entrar no bomb.",
        "Comunique a posição dos inimigos.",
        "Use suas habilidades junto com o time.",
        "Não faça sempre a mesma estratégia.",
        "Economize créditos quando necessário.",
        "Preste atenção aos sons dos inimigos.",
        "Às vezes, recuar é a melhor decisão.",
        "Tente jogar com o seu time.",
        "Não fique olhando apenas para um lugar."
    ]

    resultado.configure(
        text=f"DICA\n\n{random.choice(dicas)}"
    )


def mostrar_agentes():
    texto = "AGENTES DISPONÍVEIS\n\n"

    for i, agente in enumerate(agentes, 1):
        texto += f"{i:02d}. {agente}\n"

    resultado.configure(text=texto)


def limpar():
    resultado.configure(
        text="Aguardando uma ação..."
    )


# Título
titulo = ctk.CTkLabel(
    app,
    text="VALORANT",
    font=("Arial", 40, "bold")
)

titulo.pack(pady=(25, 5))


subtitulo = ctk.CTkLabel(
    app,
    text="ASSISTENTE DE PARTIDA",
    font=("Arial", 15)
)

subtitulo.pack()


# Área dos botões
frame = ctk.CTkFrame(app)
frame.pack(
    pady=25,
    padx=50,
    fill="x"
)


botao_agente = ctk.CTkButton(
    frame,
    text="Sortear Agente",
    command=sortear_agente
)

botao_agente.pack(
    pady=7
)


botao_mapa = ctk.CTkButton(
    frame,
    text="Sortear Mapa",
    command=sortear_mapa
)

botao_mapa.pack(
    pady=7
)


botao_tudo = ctk.CTkButton(
    frame,
    text="Sortear Partida",
    command=sortear_tudo
)

botao_tudo.pack(
    pady=7
)


botao_dica = ctk.CTkButton(
    frame,
    text="Receber Dica",
    command=dica
)

botao_dica.pack(
    pady=7
)


botao_agentes = ctk.CTkButton(
    frame,
    text="Ver Todos os Agentes",
    command=mostrar_agentes
)

botao_agentes.pack(
    pady=7
)


# Resultado
resultado = ctk.CTkLabel(
    app,
    text="Aguardando uma ação...",
    font=("Arial", 18),
    wraplength=550,
    justify="center"
)

resultado.pack(
    pady=20,
    padx=30
)


# Botão limpar
botao_limpar = ctk.CTkButton(
    app,
    text="Limpar",
    command=limpar
)

botao_limpar.pack(
    pady=5
)


# Iniciar
app.mainloop()