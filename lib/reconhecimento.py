import re
from unidecode import unidecode

class Reconhecimento:
    def __init__(self, frases):
        self.frases = frases

    def reconhece(self, frase):
        exato = self.buscaExata(frase)
        l = len(exato)
        if(l > 0):
            print("Resultado(s) exato(s) encontrados(s):")
            for r in exato:
                print('Autor: '+r[1])
        else:
            print("Resultados exatos não encontrados.")
            print("Fazendo buscas semelhantes...")
            aproximado = self.buscaAproximada(frase)

    def buscaExata(self, frase):
        resultados = []
        for i in range(0,len(self.frases)):
            if(self.simplificaString(self.frases[i][0]) == self.simplificaString(frase)):
                resultados.append(self.frases[i])
        return resultados

    def buscaAproximada(self, frase):
        palavras = self.simplificaArrayStr(frase.split(' '))
        repeticoes = self.separaRepeticoes(palavras)
        resultado = repeticoes[0]
        repeticao = repeticoes[1]
        self.buscaNaoRegex(resultado, repeticao)

    def buscaNaoRegex(self, valor, repeticao):
        for i in range(len(self.frases)):
            palavras = self.separaRepeticoes(self.simplificaArrayStr(self.frases[i][0].split(' ')))
            for p in range(len(palavras[0])):
                pal = palavras[0][p]
                rep = palavras[1][p]
                mesma = 0
                maior = 0
                menor = 0
                erro = 0
                qtdErro = 0
                acerto = 0
                for j in range(len(valor)):
                    if(pal == valor[j]):
                        if(repeticao[j] == rep):
                            mesma+=1
                            acerto += 1
                        elif(repeticao[j] > rep):
                            maior += 1
                            erro += (repeticao[j] - rep)
                            qtdErro += 1
                        elif(repeticao[j] < rep):
                            menor+=1
                            erro += (rep - repeticao[j])
                            qtdErro += 1
                        else:
                            erro += repeticao[j]
                            qtdErro += 1
                if(qtdErro > 0):
                    mediaErro = erro / qtdErro
                else:
                    mediaErro = 0
                print('Frase: '+self.frases[i][0]+'; Palavra: '+pal+'; Media de erro: '+str(mediaErro)+'; % Acertos: '+str((acerto/len(valor))*100))

            #aux.append([i])
            

    def buscaRegex(self, valor, repeticao):
        frase = []
        for i in range(len(self.frases)):
            quantidadeEncontrada = 0
            for j in valor:
                quantidadeEncontrada += len(re.findall(j, self.simplificaString(self.frases[i][0])))
            if(quantidadeEncontrada > 0):
                frase.append([self.frases[i][0], self.frases[i][1], quantidadeEncontrada])
        novoVetor = self.ordenaMatrizDesc(frase, 2)
        print(novoVetor)

    def separaRepeticoes(self, vetor):
        resultado = []
        repeticao = []
        for i in vetor:
            if(resultado.count(i) == 0):
                resultado.append(i)
                repeticao.append(1)
            else:
                indice = resultado.index(i)
                repeticao[indice]+=1
        return ([resultado, repeticao])

    def simplificaString(self, string):
        return re.sub('[,.:;?!\[\]\/\\\'\"]', '', unidecode(string.upper()))

    def simplificaArrayStr(self, vetor):
        aux = []
        for i in vetor:
            aux.append(self.simplificaString(i))
        return aux

    def ordenaMatrizDesc(self, vetor, indiceDeOrdenacao):
        #count = 0
        total = len(vetor)
        for count in range(total): #contar cada verificação
            for i in range(total): #percorre todo o vetor
                comparador = vetor[count][indiceDeOrdenacao]
                if(comparador > vetor[i][indiceDeOrdenacao]):
                    aux = vetor[count]
                    vetor[count] = vetor[i]
                    vetor[i] = aux
        return vetor

    def ordenaMatrizAsc(self, vetor, indiceDeOrdenacao):
        return None

#ola luiz eu sou o luiz ola Luiz