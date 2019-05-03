from lib.frases import Frases

def main():
    frase = Frases()
    userFrase = input('Digite a frase: ')
    frase.buscaFrase(userFrase)

def frases():
    frase = Frases()
    print(frase.frases[0:5])

main()