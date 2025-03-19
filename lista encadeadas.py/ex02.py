'''
2. Considere listas de valores inteiros e implemente uma função que receba
como parâmetro uma lista encadeada e um valor inteiro n e divida a lista em
duas, de forma a segunda lista começar no primeiro nó logo após a
ocorrência de n na lista original. A figura a seguir ilustra esta separação:
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

    def imprimir_lista(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=' -> ')
            atual = atual.proximo
        print('None')

def retira_n(lista, n):
    if not lista.cabeca:
        return lista

    while lista.cabeca and lista.cabeca.dado == n:
        lista.cabeca = lista.cabeca.proximo
    
    atual = lista.cabeca
    while atual and atual.proximo:
        if atual.proximo.dado == n:
            atual.proximo = atual.proximo.proximo
        else:
            atual = atual.proximo
    
    return lista

def separa(lista, n):
    if not lista.cabeca:
        return None
    
    atual = lista.cabeca
    while atual and atual.proximo:
        if atual.dado == n:
            nova_lista = ListaEncadeada()
            nova_lista.cabeca = atual.proximo
            atual.proximo = None
            return nova_lista
        atual = atual.proximo
    
    return None

lista = ListaEncadeada()
valores = [3, 17, 5, 12, 1]
for v in valores:
    lista.adicionar(v)

print("lista original:")
lista.imprimir_lista()

n = 5
novalista = separa(lista, n)

print("lista original apos a separaçao:")
lista.imprimir_lista()

if novalista:
    print("nova lista:")
    novalista.imprimir_lista()
