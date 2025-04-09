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


texto = input("Digite um texto (use '#' para desfazer): ")
pilha4 = Pilha()

for char in texto:
    if char == "#":
        pilha_pop(pilha4)
    else:
        pilha_push(pilha4, char)

resultado = ""
while pilha4.topo is not None:
    resultado = pilha_pop(pilha4) + resultado  

print("Texto final:", resultado)
