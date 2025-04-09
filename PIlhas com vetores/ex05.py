class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None

def pilha_push(pilha, valor):
    novo_no = Lista(valor)
    novo_no.prox = pilha.topo
    pilha.topo = novo_no

def pilha_pop(pilha):
    if pilha.topo is None:
        print("a pilha esta vazia!")
        return None
    valor_removido = pilha.topo.info
    pilha.topo = pilha.topo.prox
    return valor_removido

class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None

def pilha_push(pilha, valor):
    novo_no = Lista(valor)
    novo_no.prox = pilha.topo
    pilha.topo = novo_no

def pilha_pop(pilha):
    if pilha.topo is None:
        print("a pilha esta vazia!")
        return None
    valor_removido = pilha.topo.info
    pilha.topo = pilha.topo.prox
    return valor_removido


def remover_item_meio(pilha, valor_remover):
    aux = Pilha()
    removido = False

    while pilha.topo is not None:
        topo_valor = pilha_pop(pilha)
        if topo_valor == valor_remover and not removido:
            removido = True
            continue  
        pilha_push(aux, topo_valor)

    while aux.topo is not None:
        pilha_push(pilha, pilha_pop(aux))

    if removido:
        print(f"Elemento {valor_remover} removido.")
    else:
        print(f"Elemento {valor_remover} não encontrado.")

pilha5 = Pilha()
for i in [1, 2, 3, 4, 5]:
    pilha_push(pilha5, i)

remover_item_meio(pilha5, 3)

print("Elementos restantes:")
while pilha5.topo is not None:
    print(pilha_pop(pilha5))
