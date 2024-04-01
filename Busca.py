def PrefixoSufixo(palavra):
        listaSuf = []
        listaPref = []
        letra_anterior = ''
        if len(palavra) > 1:
            for i in range(len(palavra)):
                teste = palavra[(len(palavra)-1)-i]
                letra_anterior = teste+letra_anterior
                if letra_anterior != palavra:
                    listaSuf.append(letra_anterior)
            letra_anterior = ''
            for i in range(len(palavra)):
                teste = palavra[i]
                letra_anterior = letra_anterior+teste
                if letra_anterior != palavra:
                    listaPref.append(letra_anterior)
        intersecao = set(listaPref) & set(listaSuf)  # Encontrando a interseção dos elementos

        if len(intersecao) != 0:
            quantidade_letras = 0
            for elemento in intersecao:
                if len(elemento) > quantidade_letras:
                    quantidade_letras = len(elemento)
            return quantidade_letras
        else:
            return 0

class BuscaDNA:
    
    def GeraAltomato(chaveBusca):

        estados = {}

        for i in range(len(chaveBusca)+1):
            estado = 'S'+str(i)
            estados[estado] = []
        
        for i in range(len(chaveBusca)):
            estadoAtual = 'S'+str(i)
            lista = ['S'+str(i+1),chaveBusca[i]]
            estados[estadoAtual].append(lista)
        return estados
    def KMP(Letras,estados):

        palavra = ''
        for estado in estados:
            for letra in Letras:
                if len(estados[estado]) != 0:
                    if letra != estados[estado][0][1]:
                        palavraFinal = str(palavra+letra)
                        maxNumber = PrefixoSufixo(palavraFinal)
                        lista = ['S'+str(maxNumber),letra]
                        estados[estado].append(lista)
                else:
                    palavraFinal = str(palavra+letra)
                    maxNumber = PrefixoSufixo(palavraFinal)
                    lista = ['S'+str(maxNumber),letra]
                    estados[estado].append(lista)
            if len(estados[estado]) != 0:
                palavra = palavra+str(estados[estado][0][1])
        return estados

    def BuscaQTD(textoBusca,Letras,estados):
        estadoAtual = 'S0'
        estadoFinal = 'S'+str(len(estados)-1)
        qtdBusca = 0
        for letra in textoBusca:
            if letra == estados[estadoAtual][0][1]:
                estadoAtual = estados[estadoAtual][0][0]
            else:
                    if letra in Letras:
                        for i in range(len(estados[estadoAtual])):
                            if estados[estadoAtual][i][1] == letra:
                                estadoAtual = estados[estadoAtual][i][0]
                    else:
                        estadoAtual = 'S0'
            if estadoAtual == estadoFinal:
                qtdBusca += 1
        return qtdBusca