'''
4. Implemente uma função que receba como parâmetro uma lista encadeada
e inverta o encadeamento de seus nós, retornando a lista resultante. Após a
execução desta função, cada nó da lista vai estar referenciando (prox) o nó
que originalmente era seu antecessor, e o último nó da lista passará a ser o
primeiro nó da lista invertida, conforme ilustrado a seguir:

Esta função deve obedecer ao protótipo:
def inverte(lst):
'''


class No:
    def __init__(self, valor):
        self.valor = valor  
        self.prox = None  

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  

    def adicionar(self, valor):
        novo_no = No(valor)
        if not self.cabeca:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.prox:
                atual = atual.prox
            atual.prox = novo_no

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.prox
        print("None")

    def inverter(self):
        anterior = None
        atual = self.cabeca
        while atual:
            proximo = atual.prox  
            atual.prox = anterior  
            anterior = atual  
            atual = proximo  
        self.cabeca = anterior  


lista = ListaEncadeada()
lista.adicionar(2.1)
lista.adicionar(4.5)
lista.adicionar(1.0)
lista.adicionar(7.2)
lista.adicionar(9.8)

print("Lista Original:")
lista.exibir()

lista.inverter()

print("Lista Invertida:")
lista.exibir()

