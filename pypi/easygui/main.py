import easygui
import random

while True:

    opcao = easygui.buttonbox(
        "VERITY // ASSISTENTE PESSOAL\n\n"
        "Sistema online.\n"
        "Selecione uma função:",
        "VERITY",
        choices=[
            "Status do sistema",
            "Fazer uma pergunta",
            "Mensagem aleatória",
            "Sobre o Verity",
            "Desligar"
        ]
    )

    if opcao == "Status do sistema":
        easygui.msgbox(
            "VERITY STATUS\n\n"
            "Sistema: ONLINE\n"
            "Memória: OK\n"
            "Sensores: ATIVOS\n"
            "Conexão: ESTÁVEL\n"
            "Nível de ameaça: DESCONHECIDO",
            "VERITY // STATUS"
        )

    elif opcao == "Fazer uma pergunta":

        pergunta = easygui.enterbox(
            "Digite sua pergunta:",
            "VERITY"
        )

        if pergunta:
            respostas = [
                "Estou analisando sua pergunta...",
                "Não tenho informações suficientes.",
                "Interessante... vou registrar isso.",
                "Talvez seja melhor não saber.",
                "Essa informação não está disponível."
            ]

            easygui.msgbox(
                random.choice(respostas),
                "VERITY"
            )

    elif opcao == "Mensagem aleatória":

        mensagens = [
            "Você está sendo observado.",
            "Não confie em tudo que vê.",
            "O sistema está funcionando normalmente.",
            "Algo parece estar errado...",
            "Não há nada para se preocupar.",
            "Por enquanto."
        ]

        easygui.msgbox(
            random.choice(mensagens),
            "VERITY // ALERTA"
        )

    elif opcao == "Sobre o Verity":

        easygui.msgbox(
            "VERITY\n\n"
            "Assistente pessoal experimental.\n"
            "Função: auxiliar o usuário.\n"
            "Estado: ATIVO.\n\n"
            "Algumas funções podem apresentar "
            "comportamentos inesperados.",
            "VERITY // SYSTEM"
        )

    elif opcao == "Desligar":

        confirmar = easygui.ynbox(
            "Deseja desligar o VERITY?",
            "VERITY // SHUTDOWN",
            choices=["SIM", "NÃO"]
        )

        if confirmar:
            easygui.msgbox(
                "Encerrando sistema...\n\n"
                "VERITY OFFLINE.",
                "VERITY"
            )
            break