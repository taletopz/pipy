import flet as ft
import json
import os

ARQUIVO = "pets.json"


def carregar_pets():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_pets(pets):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(pets, arquivo, indent=4, ensure_ascii=False)


def main(page: ft.Page):

    page.title = "Pet Shop"
    page.window_width = 500
    page.window_height = 700
    page.padding = 30

    titulo = ft.Text(
        "PET SHOP",
        size=32,
        weight=ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Cadastro e gerenciamento de pets",
        size=16
    )

    nome_pet = ft.TextField(
        label="Nome do pet",
        prefix_icon=ft.Icons.PETS
    )

    nome_dono = ft.TextField(
        label="Nome do dono",
        prefix_icon=ft.Icons.PERSON
    )

    especie = ft.Dropdown(
        label="Espécie",
        options=[
            ft.dropdown.Option("Cachorro"),
            ft.dropdown.Option("Gato"),
            ft.dropdown.Option("Coelho"),
            ft.dropdown.Option("Pássaro"),
            ft.dropdown.Option("Hamster"),
            ft.dropdown.Option("Outro")
        ]
    )

    servico = ft.Dropdown(
        label="Serviço",
        options=[
            ft.dropdown.Option("Banho"),
            ft.dropdown.Option("Tosa"),
            ft.dropdown.Option("Banho e Tosa"),
            ft.dropdown.Option("Consulta"),
            ft.dropdown.Option("Corte de unhas"),
            ft.dropdown.Option("Limpeza dentária")
        ]
    )

    mensagem = ft.Text()

    lista_pets = ft.Column()

    def atualizar_lista():

        pets = carregar_pets()

        lista_pets.controls.clear()

        if not pets:
            lista_pets.controls.append(
                ft.Text("Nenhum pet cadastrado.")
            )

        else:

            for pet in pets:

                lista_pets.controls.append(
                    ft.Card(
                        content=ft.Container(
                            padding=15,
                            content=ft.Column([
                                ft.Text(
                                    f"🐾 {pet['pet']}",
                                    size=20,
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(
                                    f"Dono: {pet['dono']}"
                                ),
                                ft.Text(
                                    f"Espécie: {pet['especie']}"
                                ),
                                ft.Text(
                                    f"Serviço: {pet['servico']}"
                                )
                            ])
                        )
                    )
                )

        page.update()

    def cadastrar(e):

        if not nome_pet.value or not nome_dono.value:
            mensagem.value = "Preencha o nome do pet e do dono."
            mensagem.color = "red"
            page.update()
            return

        if not especie.value or not servico.value:
            mensagem.value = "Escolha a espécie e o serviço."
            mensagem.color = "red"
            page.update()
            return

        pets = carregar_pets()

        novo_pet = {
            "pet": nome_pet.value,
            "dono": nome_dono.value,
            "especie": especie.value,
            "servico": servico.value
        }

        pets.append(novo_pet)

        salvar_pets(pets)

        mensagem.value = "Pet cadastrado com sucesso!"
        mensagem.color = "green"

        nome_pet.value = ""
        nome_dono.value = ""
        especie.value = None
        servico.value = None

        atualizar_lista()

    botao_cadastrar = ft.Button(
        "Cadastrar Pet",
        icon=ft.Icons.ADD,
        on_click=cadastrar
    )

    page.add(
        titulo,
        subtitulo,
        ft.Divider(),

        nome_pet,
        nome_dono,
        especie,
        servico,

        ft.Container(height=10),

        botao_cadastrar,
        mensagem,

        ft.Divider(),

        ft.Text(
            "Pets cadastrados",
            size=22,
            weight=ft.FontWeight.BOLD
        ),

        lista_pets
    )

    atualizar_lista()


ft.run(main)