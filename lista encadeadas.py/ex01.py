'''
1. Considere listas de valores inteiros e implemente uma função que receba
como parâmetros uma lista encadeada e um valor inteiro n, retire da lista
todas as ocorrências de n e retorne a lista resultante. Esta função deve
obedecer ao protótipo:

def retira_n(lst, n):
'''


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None 

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, dado):
        novo_no = No(dado)
        if not self.cabeca:
            self.cabeca = novo_no
            return 
        ultimo = self.cabeca 
        while ultimo.proximo:
            ultimo = ultimo.proximo  
        ultimo.proximo = novo_no

    def impirmirLista(self):
        atual = self.cabeca 
        while atual:
            print(atual.dado, end=' -> ')
            atual = atual.proximo 
        print('None')


def retira_n(lista, n):
    if not lista.cabeca:
        return lista 
    
    #removendo do inicio
    atual = lista.cabeca 
    while atual and atual.proximo:
        if atual.proximo.dado == n:
            atual.proximo = atual.proximo.proximo
        else:
            atual = atual.proximo 

    return lista 

lista = ListaEncadeada()
valores = [1, 2, 3, 3, 6, 8, 7]
for v in valores:
    lista.adicionar(v)

print("lista original")
lista.impirmirLista()

n = 2
retira_n(lista, n)

print(f"lista apos remover {n}:")
lista.impirmirLista()
