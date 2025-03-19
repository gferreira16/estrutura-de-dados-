
'''
6. Considere listas que armazenam cadeias de caracteres e implemente uma
função para criar uma cópia de uma lista encadeada. Essa função deve
obedecer ao protótipo:

def copia(lst):
'''


def igual(l1, l2):
    return l1 == l2

def copia(lst):
    return lst[:]


a = ["Gabriel", "Balsemao", "Ferreira"]
b = ["Gabriel", "Balsemao", "Ferreira"]
c = ["lista", "d"]

teste1 = igual(a, b) 
teste2 = igual(a, c)

copia_lista = copia(a)
print(teste1)  
print(teste2) 
print(copia_lista) 
