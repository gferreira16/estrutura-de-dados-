import random

class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self.anterior = None
        self.proximo = None

class RoletaRussaCircular:
    def __init__(self, guerreiros):
        self.inicio = None
        self.criar_lista(guerreiros)
    
    def criar_lista(self, guerreiros):
        if not guerreiros:
            return
        
        primeiro = Guerreiro(guerreiros[0])
        self.inicio = primeiro
        atual = primeiro
        
        for nome in guerreiros[1:]:
            novo = Guerreiro(nome)
            atual.proximo = novo
            novo.anterior = atual
            atual = novo
        
        atual.proximo = primeiro 
        primeiro.anterior = atual

    def eliminar_guerreiro(self):
        if not self.inicio or self.inicio.proximo == self.inicio:
            return self.inicio
        
        atual = self.inicio
        guerreiros_vivos = self.obter_nomes()
        if not guerreiros_vivos:
            return
        
        escolhido = random.choice(guerreiros_vivos)
        while atual.nome != escolhido:
            atual = atual.proximo
        
        print(f"{atual.nome} foi eliminado.")
        
        atual.anterior.proximo = atual.proximo
        atual.proximo.anterior = atual.anterior
        
        if atual == self.inicio:
            self.inicio = atual.proximo
        
    def nomes(self):
        nomes = []
        atual = self.inicio
        if not atual:
            return nomes
        
        while True:
            nomes.append(atual.nome)
            atual = atual.proximo
            if atual == self.inicio:
                break
        return nomes

    def iniciar_jogo(self):
        while len(self.obter_nomes()) > 1:
            self.eliminar_guerreiro()
        print(f"O sobrevivente é {self.inicio.nome}!")


guerreiros = ["Thor", "Loki", "Ragnar", "Bjorn", "Ivar", "Kratos"]
jogo = RoletaRussaCircular(guerreiros)
jogo.iniciar_jogo()


