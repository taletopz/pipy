import streamlit as st
import json
import os
import hashlib

ARQUIVO = "cadastros.json"


def carregar_cadastros():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return []


def salvar_cadastros(cadastros):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)


def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


# Configuração da página
st.set_page_config(
    page_title="NEXUS - Cadastro",
    layout="centered"
)

# Tema visual
st.markdown("""
<style>

.stApp {
    background-color: #0b0b12;
    color: #eeeeee;
}

h1 {
    text-align: center;
    color: #9b5cff;
    font-size: 42px;
    margin-bottom: 5px;
}

.subtitulo {
    text-align: center;
    color: #888899;
    margin-bottom: 35px;
}

.caixa {
    background-color: #12121c;
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #29293d;
    box-shadow: 0px 0px 25px rgba(155, 92, 255, 0.08);
}

.stTextInput label {
    color: #bbbbcc;
}

.stTextInput input {
    background-color: #181824;
    color: white;
    border: 1px solid #333348;
    border-radius: 7px;
}

.stTextInput input:focus {
    border-color: #9b5cff;
}

.stButton button {
    width: 100%;
    background-color: #7b3fe4;
    color: white;
    border: none;
    border-radius: 7px;
    padding: 10px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #9b5cff;
    color: white;
}

.rodape {
    text-align: center;
    color: #555566;
    margin-top: 30px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# Cabeçalho
st.markdown("# NEXUS")
st.markdown(
    '<p class="subtitulo">Sistema de criação de conta</p>',
    unsafe_allow_html=True
)

# Área do cadastro
st.markdown('<div class="caixa">', unsafe_allow_html=True)

nome = st.text_input("Nome completo")
usuario = st.text_input("Nome de usuário")
email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")
confirmar = st.text_input("Confirmar senha", type="password")

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

if st.button("CRIAR CONTA"):

    if not nome or not usuario or not email or not senha:
        st.warning("Preencha todos os campos.")

    elif senha != confirmar:
        st.error("As senhas não são iguais.")

    else:

        cadastros = carregar_cadastros()

        usuario_existe = any(
            pessoa["usuario"] == usuario
            for pessoa in cadastros
        )

        if usuario_existe:
            st.error("Esse nome de usuário já está cadastrado.")

        else:

            novo_cadastro = {
                "nome": nome,
                "usuario": usuario,
                "email": email,
                "senha": gerar_hash(senha)
            }

            cadastros.append(novo_cadastro)

            salvar_cadastros(cadastros)

            st.success("Conta criada com sucesso.")

st.markdown(
    '<p class="rodape">NEXUS SYSTEM — Cadastro de usuários</p>',
    unsafe_allow_html=True
)