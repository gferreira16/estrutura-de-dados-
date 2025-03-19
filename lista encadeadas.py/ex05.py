
'''
5. Considere listas que armazenam cadeias de caracteres e implemente uma
função para testar se duas listas passadas como parâmetros são iguais. Essa
função deve obedecer ao protótipo:

def igual(l1, l2):
'''


def igual(l1, l2):
    return l1 == l2


a = ["Gabriel", "Balsemao", "Ferreira"]
b = ["Gabriel", "Balsemao", "Ferreira"]
c = ["lista", "diferente"]

teste1 = igual(a, b)  # True
teste2 = igual(a, c)  # False

print(teste1)  # said: True
print(teste2)  # saida: False


