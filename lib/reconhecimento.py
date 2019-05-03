import re
import os
from unidecode import unidecode

class Reconhecimento:
    def __init__(self, frases):
        self.frases = frases
        
    def reconhece(self, frase):
        exato = self.buscaExata(frase)
        l = len(exato)
        if(l > 0):
            #print("Resultado(s) exato(s) encontrados(s):")
            self.executaOrdem(exato)
        else:
            print("Resultados exatos não encontrados.")
            print("Fazendo buscas semelhantes...")
            aproximado = self.buscaAproximada(frase)
            print("Os 5 primeiros resultados:")
            return aproximado[0:5]

    def executaOrdem(self, resultado):
        for linha in resultado:
            os.system(linha[1])

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
        return self.buscaNaoRegex(resultado, repeticao)

    def buscaNaoRegex(self, valor, repeticao):
        aux = []
        for i in range(len(self.frases)):
            palavras = self.separaRepeticoes(self.simplificaArrayStr(self.frases[i][0].split(' ')))
            mesma = 0
            maior = 0
            menor = 0
            erro = 0
            qtdErro = 0
            mediaErro = 0
            palavraNaoEncontrada = 0
            for j in range(len(valor)):
                encontrou = 0
                for p in range(len(palavras[0])):
                    pal = palavras[0][p]
                    rep = palavras[1][p]
                    if(pal == valor[j]):
                        encontrou = 1
                        if(repeticao[j] == rep):
                            mesma+=1
                        elif(repeticao[j] > rep):
                            maior += 1
                            erro += (repeticao[j] - rep)
                            qtdErro += 1
                        elif(repeticao[j] < rep):
                            menor+=1
                            erro += (rep - repeticao[j])
                            qtdErro += 1
                if(encontrou == 0):
                    palavraNaoEncontrada += 1
                
            if(qtdErro > 0):
                mediaErro = erro / qtdErro

            palavraEncontrada = mesma+maior+menor
            porcentagemEncontrada = (palavraEncontrada/(palavraEncontrada+palavraNaoEncontrada))*100
            #print("")
            #print("Frase: "+self.frases[i][0])
            #print("Autor: "+self.frases[i][1])
            #print("Frase digitada:", valor)
            #print("Média de erro: "+str(mediaErro))
            #print("Quantidade de palavras encontradas:"+str(palavraEncontrada))
            #print("Quantidade de palavras NÃO encontradas:"+str(palavraNaoEncontrada))
            #print('Porcentagem encontrada: '+str(porcentagemEncontrada))
                #print('Frase: '+self.frases[i][0]+'; Palavra: '+pal+'; Media de erro: '+str(mediaErro)+'; % Acertos: '+str((acerto/len(valor))*100))

            aux.append([self.frases[i][0], self.frases[i][1], porcentagemEncontrada, mediaErro, len(palavras[0])])
        return(self.ordenaBuscaNaoRegex(aux))
    
    def ordenaBuscaNaoRegex(self, vetor):
        total = len(vetor)
        for count in range(total): #contar cada verificação
            for i in range(total): #percorre todo o vetor
                comparador = vetor[count][2]
                if(comparador > vetor[i][2]):
                    aux = vetor[count]
                    vetor[count] = vetor[i]
                    vetor[i] = aux
                elif(comparador == vetor[i][2]):
                    if(vetor[count][3] < vetor[i][3]):
                        aux = vetor[count]
                        vetor[count] = vetor[i]
                        vetor[i] = aux
                    elif(vetor[count][3] == vetor[i][3]):
                        if(vetor[count][4] < vetor[i][4]):
                            aux = vetor[count]
                            vetor[count] = vetor[i]
                            vetor[i] = aux
        return vetor            

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