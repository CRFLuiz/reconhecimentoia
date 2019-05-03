from lib.frases import Frases
import speech_recognition as sr

def main():
    frase = Frases()
    try:
        userFrase = input('Sim, mestre. O que deseja?  ')
        frase.buscaFrase(userFrase)
    except:
        print("\nBye")

def voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Diga algo!')
        audio = r.listen(source)
    
    try:
        print("Voce disse: " + r.recognize_google(audio, language="pt-BR"))
    except sr.UnknownValueError:
        print("Mariana não pode entender o audio")
    except sr.RequestError as e:
        print("Erro ao chamar Google Speech Recognition service; {0}".format(e))

voz()