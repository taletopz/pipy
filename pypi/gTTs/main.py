from gtts import gTTS

texto = input("Digite o texto: ")

voz = gTTS(text=texto, lang="pt", tld="com.br")
voz.save("audio.mp3")