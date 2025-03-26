import random

class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.inicio = None
    
    def inserir(self, nome):
        novo = No(nome)
        if not self.inicio:
            self.inicio = novo
            novo.proximo = self.inicio
        else:
            atual = self.inicio
            while atual.proximo != self.inicio:
                atual = atual.proximo
            atual.proximo = novo
            novo.proximo = self.inicio
    
    def buscar(self, nome):
        if not self.inicio:
            return False
        atual = self.inicio
        while True:
            if atual.nome == nome:
                return True
            atual = atual.proximo
            if atual == self.inicio:
                break
        return False
    
    def remover(self, nome):
        if not self.inicio:
            return
        atual = self.inicio
        anterior = None
        while True:
            if atual.nome == nome:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    ultimo = self.inicio
                    while ultimo.proximo != self.inicio:
                        ultimo = ultimo.proximo
                    self.inicio = atual.proximo
                    ultimo.proximo = self.inicio
                return
            anterior = atual
            atual = atual.proximo
            if atual == self.inicio:
                break
    
    def contar(self):
        if not self.inicio:
            return 0
        contador = 0
        atual = self.inicio
        while True:
            contador += 1
            atual = atual.proximo
            if atual == self.inicio:
                break
        return contador

class BatataQuente:
    def __init__(self, jogadores):
        self.lista = ListaCircular()
        for jogador in jogadores:
            self.lista.inserir(jogador)
    
    def jogar(self):
        atual = self.lista.inicio
        while self.lista.contar() > 1:
            k = random.randint(1, 10)
            for _ in range(k - 1):
                atual = atual.proximo
            print(f"{atual.nome} foi eliminado!")
            self.lista.remover(atual.nome)
            atual = atual.proximo
        print(f"O vencedor é {self.lista.inicio.nome}!")

class ArenaCavaleiros:
    def __init__(self, cavaleiros):
        self.lista = ListaCircular()
        self.hp = {}
        for cavaleiro in cavaleiros:
            self.lista.inserir(cavaleiro)
            self.hp[cavaleiro] = random.randint(50, 100)
    
    def batalhar(self):
        atual = self.lista.inicio
        while self.lista.contar() > 1:
            dano = random.randint(5, 10)
            alvo = atual.proximo.nome
            self.hp[alvo] -= dano
            print(f"{atual.nome} atacou {alvo} causando {dano} de dano! {alvo} agora tem {self.hp[alvo]} de HP.")
            if self.hp[alvo] <= 0:
                print(f"{alvo} foi eliminado!")
                self.lista.remover(alvo)
                del self.hp[alvo]
            atual = atual.proximo
        print(f"O campeão é {self.lista.inicio.nome}!")

jogadores = ["Lucio", "Carlos", "Almir", "Isadora", "Daniela"]
jogo_batata = BatataQuente(jogadores)
jogo_batata.jogar()

cavaleiros = ["Arthur", "Gabriel", "Bernardo", "Eduardo", "Pedro"]
arena = ArenaCavaleiros(cavaleiros)
arena.batalhar()
