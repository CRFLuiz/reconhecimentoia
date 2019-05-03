from lib.frases import Frases

def main():
    frase = Frases()
    try:
        userFrase = input('Sim, mestre. O que deseja?  ')
        frase.buscaFrase(userFrase)
    except:
        print("\nBye")

main()