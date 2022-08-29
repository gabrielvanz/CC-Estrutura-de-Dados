import os

class Pilha:
    def __init__(self):
        self.vet = [] # lista interna

    def peek(self): # retorna qual item esta no topo
        return self.vet[len(self.vet)-1]

    def push(self, item): # metodo de inserir item
        self.vet.append(item)

    def pop(self): # remover o topo e retornar item para usuario
        # tratar caso de underflow
        return self.vet.pop()
        
    def is_empty(self): # teste se é vazia
        return self.vet == []

    def insert(self,index,valor):
        self.vet.insert(index,valor)
        
    def __len__(self): # retorna o total de itens
        return len(self.vet)

    def __str__(self): # representacao da pilha como string
        return str(self.vet)

if __name__ == "__main__":
    def validador(expressao):
        x = 0
        pilha = Pilha()

        while x < len(expressao):
            #Verifica as Chaves -> {}
            if expressao[x] == "{":
                pilha.push("{")
            if expressao[x] == "}":
                if (pilha.is_empty() == False) and (pilha.peek() == '{'):
                    pilha.pop()
                else:
                    pilha.push("}")

            #Verifica os Colchetes -> []
            if expressao[x] == "[":
                pilha.push("[")
            if expressao[x] == "]":
                if (pilha.is_empty() == False) and (pilha.peek() == '['):
                    pilha.pop()
                else:
                    pilha.push("]")

            #Verifica os Parenteses -> ()
            if expressao[x] == "(":
                pilha.push("(")
            if expressao[x] == ")":
                if (pilha.is_empty() == False) and (pilha.peek() == '('):
                    pilha.pop()
                else:
                    pilha.push(")")
            
            x += 1
            
        if pilha.is_empty() == True:
            print('\n'+expressao)
            print("Expressão válida\n")
        else:
            print('\n'+expressao)
            print("Expressão inválida\n")
            
    os.system('cls')
    expressao = input("Digite a sequência de parênteses a validar:")
    validador(expressao)
        
    
