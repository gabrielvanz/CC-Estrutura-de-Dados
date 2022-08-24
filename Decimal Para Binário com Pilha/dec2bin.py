
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
    def dec2bin(valor):
        pilha = Pilha()
        while True:
            if valor <= 0:
                break
            resto = valor%2
            resultado = valor//2
            pilha.insert(0,resto)
            valor = valor//2
        return pilha.vet

    valor = int(input("Insira um número: "))
    
    valorT = dec2bin(valor)
    valorT = str(valorT).strip('[]').replace(',',' ')
    print("A conversão em binarios de",valor,"é -> ",valorT)