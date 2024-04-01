import tkinter as tk
from main import main
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox

Inserido = False

def centralizar_janela(janela):
    largura_janela = 50
    altura_janela = 70

    # Obtenha as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcule as coordenadas x e y para centralizar a janela
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    # Defina a geometria da janela para as coordenadas calculadas
    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

def Dimencao(Janela):
    Janela.update_idletasks()
    Altura = Janela.winfo_height()
    Largura = Janela.winfo_width()
    return Largura,Altura

def UpdateGraph():

    global controle,estadoAtual,qtdBusca

    if chaveBuscaLabel.get() == '' or Inserido == False:
        messagebox.showinfo("Título da Mensagem", "Insira os dados")
        return 
    
    estadoFinal = 'S'+str(len(estados)-1)
    if (len(textoBusca)) != controle:
        LetraBusca.set(textoBusca[controle])
        for letra in textoBusca[controle]:
            if letra == estados[estadoAtual][0][1]:
                estadoAnterior = estadoAtual
                estadoAtual = estados[estadoAtual][0][0]
            else:
                    if letra in Letras:
                        for i in range(len(estados[estadoAtual])):
                            if estados[estadoAtual][i][1] == letra:
                                estadoAnterior = estadoAtual
                                estadoAtual = estados[estadoAtual][i][0]
                    else:
                        estadoAnterior = estadoAtual
                        estadoAtual = 'S0'
            if estadoAtual == estadoFinal:
                qtdBusca += 1
                valorBusca.set(qtdBusca)
        controle+=1
        GeraGrafo(estadoAtual,estados,estadoAnterior)
    else:
        messagebox.showinfo("Aviso", f"Processo Finalizado")
        estadoAtual = 'S0'
        controle = 0

def GeraGrafo(estadoAtual,estados,estadoAnterior):
    figure.clear()

    caminho = (estadoAnterior,estadoAtual)

    G = nx.DiGraph()

    nodes = [chave for chave in estados]
    edges = []
    edge_labels = {}
    
    for estado in estados:
        for i in range(len(estados[estado])):
            lista = (estado,estados[estado][i][0])
            edge_labels[lista] = estados[estado][i][1]
            edges.append(lista)

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    ax = figure.add_subplot()
    pos = nx.circular_layout(G)
    edge_colors = ['blue' if edge == caminho else 'black' for edge in G.edges()]
    nx.draw(G,ax=ax,pos=pos,with_labels=True, node_color='skyblue',edge_color=edge_colors, node_size=1000)
    nx.draw_networkx_edge_labels(G,ax=ax,pos=pos,edge_labels=edge_labels)

    canvas.draw()

def Inserir():
    global estados,textoBusca,Letras,numeroPalavras,estadoAtual,controle,qtdBusca,Inserido
    Inserido = True
    estadoAtual = 'S0'
    controle = 0
    qtdBusca = 0

    estados,textoBusca,Letras,numeroPalavras = main(chaveBuscaLabel.get(),palavraBuscaLabel.get())
    messagebox.showinfo("Aviso", "Dados Inseridos")
    valorBusca.set(qtdBusca)

Janela = tk.Tk()


valorBusca = tk.StringVar()
LetraBusca = tk.StringVar()

Janela.title('Janela')

Janela.config(bg="#808080")

Janela.attributes('-zoomed', True)
Janela.resizable(False, False)

button_frame = tk.Frame(Janela)
button_frame.pack(side='right', fill='y')
button_frame.config(bg='#797979', borderwidth=70)

Largura,Altura = Dimencao(Janela)

chaveBuscaLabel = tk.Entry(button_frame)
chaveBuscaLabel.place(x=100,y=350)

chaveBuscaTxt = tk.Label(button_frame,text='Chave Busca:',background='#797979',fg='white',font=("Arial", 12, "bold"))
chaveBuscaTxt.place(x=100,y=320)

qtdBuscaLabel = tk.Label(Janela,text='Sentenças encontradas:',background='#808080',fg='white',font=("Arial", 12, "bold"))
qtdBuscaLabel.place(x=10,y=10)

qtdBuscaTxt = tk.Label(Janela,textvariable=valorBusca,background='#808080',fg='white',font=("Arial", 12, "bold"))
qtdBuscaTxt.place(x=200,y=10)

LetraBuscaLabel = tk.Label(Janela,text='Buscando:',background='#808080',fg='white',font=("Arial", 12, "bold"))
LetraBuscaLabel.place(x=10,y=40)

LetraBuscaTxt = tk.Label(Janela,textvariable=LetraBusca,background='#808080',fg='white',font=("Arial", 12, "bold"))
LetraBuscaTxt.place(x=110,y=40)

palavraBuscaLabel = tk.Entry(button_frame)
palavraBuscaLabel.place(x=100,y=260)

palavraBuscaTxt = tk.Label(button_frame,text='Palavra De Busca:',background='#797979',fg='white',font=("Arial", 12, "bold"))
palavraBuscaTxt.place(x=100,y=230)

botaoDireito = tk.Button(button_frame,text='Proximo',command=UpdateGraph,width=10,height=3)
botaoDireito.pack(side=tk.RIGHT,padx=30,pady=20)

botaoEsquerdo = tk.Button(button_frame,text='Inserir Dados',command=Inserir,width=10,height=3)
botaoEsquerdo.pack(side=tk.RIGHT,padx=30,pady=20)

figureFrame = tk.Frame(Janela,width=500,height=500)
figureFrame.pack(expand=True)

figure = Figure(figsize=(10, 8), dpi=100)

canvas = FigureCanvasTkAgg(figure, master=figureFrame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

Janela.mainloop()