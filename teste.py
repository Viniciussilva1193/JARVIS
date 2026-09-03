from datetime import datetime
import webbrowser
import pyttsx3
import subprocess


def falar(texto):
    print("JARVIS:", texto)

    voz = pyttsx3.init()
    voz.say(texto)
    voz.runAndWait()
    voz.stop()


# Início do JARVIS
nome = input("Qual é o seu nome? ")

falar("Olá, " + nome)
falar("JARVIS está online!")


# Comandos
while True:

    comando = input("Você: ").lower().strip()

    # Olá
    if comando == "ola" or comando == "olá":
        falar("Olá! Como posso ajudar?")

    # Hora
    elif comando == "hora":
        hora = datetime.now().strftime("%H:%M")
        falar("Agora são " + hora)

    # Data
    elif comando == "que dia é hoje" or comando == "que dia e hoje":
        data = datetime.now().strftime("%d/%m/%Y")
        falar("Hoje é " + data)

    # Quem é você?
    elif comando in [
        "quem e voce",
        "quem é você",
        "quem voce e",
        "quem você é"
    ]:
        falar("Sou o JARVIS, seu assistente virtual.")

    # Abrir navegador
    elif comando == "abrir navegador":
        falar("Abrindo o navegador.")
        webbrowser.open("https://www.google.com")

    # Abrir YouTube
    elif comando == "abrir youtube" or comando == "abrir o youtube":
        falar("Abrindo o YouTube.")
        webbrowser.open("https://www.youtube.com")

    # Abrir calculadora
    elif comando == "abrir calculadora":
        falar("Abrindo a calculadora.")
        subprocess.Popen("calc.exe")

    # Fazer cálculo
    elif comando.startswith("calcular "):
        conta = comando.replace("calcular ", "", 1)

        try:
            resultado = eval(conta, {"__builtins__": {}}, {})
            falar("O resultado é " + str(resultado))

        except:
            falar("Não consegui realizar esse cálculo.")

    # Sair
    elif comando == "sair":
        falar("Até logo!")
        break

    # Comando desconhecido
    else:
        falar("Ainda não conheço esse comando.")