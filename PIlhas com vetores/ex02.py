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


def esvaziar_pilha(p):
    while p.topo is not None:
        pilha_pop(p)
    print("Pilha esvaziada.")

pilha2 = Pilha()
for i in range(1, 6):
    pilha_push(pilha2, i)
esvaziar_pilha(pilha2)
