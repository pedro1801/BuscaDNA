from Busca import BuscaDNA

def main(chave,texto):
    chaveBusca = chave
    chaveBusca = chaveBusca.upper()
    chaveBusca = [char for char in chaveBusca]

    textoBusca = texto
    textoBusca = textoBusca.upper()

    Letras = sorted(list(set(chaveBusca)))

    estados = BuscaDNA.GeraAltomato(chaveBusca)

    estados = BuscaDNA.KMP(Letras,estados)
    #print(estados)

    numeroPalavras = BuscaDNA.BuscaQTD(textoBusca,Letras,estados)
    return estados,textoBusca,Letras,numeroPalavras