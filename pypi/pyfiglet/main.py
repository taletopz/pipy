import pyfiglet
texto = input("Digite uma palavra ou frase: ")
nome = pyfiglet.figlet_format(texto, font="slant")
print(nome)