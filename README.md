# BuscaDNA

## Descrição

### O projeto BuscaDNA é uma implementação do algoritmo Knuth-Morris-Pratt (KMP) com foco em busca de padrões em sequências de DNA. Este algoritmo é uma técnica eficiente para encontrar ocorrências de um padrão específico em uma sequência de texto, utilizando a ideia de evitar recomparações de caracteres que já foram correspondidos. O código foi desenvolvido com o objetivo de facilitar a busca por padrões genéticos em grandes sequências de DNA.

## Algoritmo KMP

### O algoritmo KMP é uma técnica de busca de subcadeias em strings que possui um tempo de execução linear em relação ao tamanho do texto de entrada. Ele utiliza um prefixo da subcadeia para evitar recomparações desnecessárias. Isso o torna especialmente eficiente em aplicações que envolvem grandes conjuntos de dados, como a análise de sequências genéticas.

## Funcionalidades

### - Busca eficiente de padrões em sequências de DNA.
### - Implementação do algoritmo KMP.
### - Suporte para busca de múltiplos padrões simultaneamente.

## Dependencias

### - Matplotlib
### - NetworkX
### - Tkinter

### Caso não tenha as dependências acima, siga os passos de instalação.

## Intalação

### - conda install matplotlib ou pip install matplotlib
### - pip install networkx
### - pip install tk

# Diretorios
```
.
├── Busca.py
├── GUI.py
├── main.py
└── README.md
```
 Busca.py Aqui está o código referente ao algoritmo KMP.
 main.py Código que faz a ligação entre o GUI.py e Busca.py.
 GUI.py Código que cria a interface de usuário.
 
 # Como Usar
 
 ### - Clone o repositório
 ### - Baixe as dependências se for preciso
 ### - Entre no diretório do código
 ### - Execute o comando python GUI.py
