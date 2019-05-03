from lib.reconhecimento import Reconhecimento

class Frases:
    separador = ';'
    def __init__(self):
        f = open('/usr/local/Mariana/banco/frases', 'r')
        self.linhas = f.readlines()
        f.close()
        self.separaFrasesAutores()
    
    def separaFrasesAutores(self):
        self.frases = []
        for line in self.linhas:
            self.frases.append(line.split(self.separador))
        self.removeEnter()

    def removeEnter(self):
        l = len(self.frases)
        for i in range(0,l):
            self.frases[i][1] = self.frases[i][1].replace('\n', '')

    def buscaFrase(self, frase):
        rec = Reconhecimento(self.frases)
        rec.reconhece(frase)
