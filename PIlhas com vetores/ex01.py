class Pilha:
    def __init__(self, cap):
        self.cap = cap
        self.n = 0 
        self.vet = []

def pilha_push(pilha, valor):
    if pilha.n == pilha.cap:
        print("A pilha está cheia!")
        return pilha
        
    pilha.vet.append(valor)
    pilha.n += 1

def pilha_pop(pilha):
    if pilha.n == 0:
        print("A pilha já está vazia!")
        return None 
        
    valor = pilha.vet.pop()
    pilha.n -= 1
    return valor

pilha = Pilha(10)

for i in range(1, 6):
    pilha_push(pilha, i)

while pilha.n != 0:
    print(pilha_pop(pilha))
   
