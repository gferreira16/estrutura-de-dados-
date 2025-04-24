

class AvaliadorBooleano:
    def __init__(self):
        self.pilha_operadores = []  
        self.pilha_operandos = []   
      
    def precedencia(self, operador):
        """Retorna a precedência dos operadores lógicos."""
        if operador == 'not':
            return 3 
        elif operador == 'and':
            return 2
        elif operador == 'or':
            return 1
        return 0  

    def avaliar_operador(self):
        """Aplica o operador lógico no topo da pilha sobre os operandos correspondentes."""
        operador = self.pilha_operadores.pop()

        if operador == 'not':
            operando = self.pilha_operandos.pop()
            self.pilha_operandos.append(not operando)  
        else:
            operando_direito = self.pilha_operandos.pop()
            operando_esquerdo = self.pilha_operandos.pop()

            if operador == 'and':
                self.pilha_operandos.append(operando_esquerdo and operando_direito)
            elif operador == 'or':
                self.pilha_operandos.append(operando_esquerdo or operando_direito)

    def processar_expressao(self, expressao):
        """Converte a expressão em tokens e avalia a expressão booleana."""
        tokens = []
        i = 0
        while i < len(expressao):
            char = expressao[i]

            if char in '()':
                tokens.append(char)
                i += 1

            elif expressao[i:i+3] == 'and':
                tokens.append('and')
                i += 3

            elif expressao[i:i+2] == 'or':
                tokens.append('or')
                i += 2

            elif expressao[i:i+3] == 'not':
                tokens.append('not')
                i += 3

            elif expressao[i:i+4] == 'True':
                tokens.append('True')
                i += 4

            elif expressao[i:i+5] == 'False':
                tokens.append('False')
                i += 5

  
            elif char != ' ':
                raise ValueError(f"Caractere inválido encontrado: {char}")
            else:
                i += 1

        for token in tokens:
            if token in ['True', 'False']:
                self.pilha_operandos.append(token == 'True')  

            elif token in ['and', 'or', 'not']:
               
                while (self.pilha_operadores and
                       self.precedencia(self.pilha_operadores[-1]) >= self.precedencia(token)):
                    self.avaliar_operador()
                self.pilha_operadores.append(token)

            elif token == '(':
                self.pilha_operadores.append(token)  

            elif token == ')':
               
                while self.pilha_operadores and self.pilha_operadores[-1] != '(':
                    self.avaliar_operador()

                if not self.pilha_operadores:
                    raise ValueError("Parênteses desbalanceados na expressão.")
                self.pilha_operadores.pop()  

            else:
                raise ValueError(f"Token inválido encontrado: {token}")

        
        while self.pilha_operadores:
            self.avaliar_operador()

        if len(self.pilha_operandos) != 1:
            raise ValueError("Expressão malformada.")

        return self.pilha_operandos.pop() 
      
def main():
    print("=== Avaliador de Expressões Booleanas ===")
    print("Você pode usar: True, False, and, or, not, parênteses.")
    print("Exemplo: not (True and False) or False\n")

    while True:
        expressao = input("Digite a expressão (ou 'sair' para encerrar): ")
        if expressao.lower() == 'sair':
            print("Encerrando o avaliador.")
            break

        avaliador = AvaliadorBooleano()
        try:
            resultado = avaliador.processar_expressao(expressao)
            print(f"Resultado: {resultado}\n")
        except Exception as e:
            print(f"Erro: {e}\n")

if __name__ == "__main__":
    main()
