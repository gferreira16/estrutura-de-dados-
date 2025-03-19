'''
3. Implemente uma função que construa uma nova lista com a intercalação
dos nós de outras duas listas passadas como parâmetros. Esta função deve
retornar a lista resultante, conforme ilustrado a seguir:

Esta função deve obedecer ao protótipo:
def merge(l1, l2):
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

def mesclar(l1, l2):
    nova_lista = ListaEncadeada()
    atual1 = l1.cabeca
    atual2 = l2.cabeca
    
    while atual1 or atual2:
        if atual1:
            nova_lista.adicionar(atual1.dado)
            atual1 = atual1.proximo
        if atual2:
            nova_lista.adicionar(atual2.dado)
            atual2 = atual2.proximo
    
    return nova_lista

lista1 = ListaEncadeada()
valores1 = [2.1, 4.5, 1.0]
for v in valores1:
    lista1.adicionar(v)

lista2 = ListaEncadeada()
valores2 = [7.2, 3.1, 9.8]
for v in valores2:
    lista2.adicionar(v)

print("lista 1:")
lista1.imprimir_lista()
print("lista 2:")
lista2.imprimir_lista()

lista_mesclada = mesclar(lista1, lista2)
print("lista mesclada:")
lista_mesclada.imprimir_lista()
