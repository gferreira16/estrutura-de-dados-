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


pilha3 = Pilha()
for i in range(5):
    num = int(input(f"digite o {i+1}º numero: "))
    pilha_push(pilha3, num)

print("numeros na ordem inversa:")
while pilha3.topo is not None:
    print(pilha_pop(pilha3))
