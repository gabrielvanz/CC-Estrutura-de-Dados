import os

def limpaTela():
    os.system("cls")

class Fila:    
    def __init__(self):
        self._vet = []
    
    def enqueue(self, item): # enfileirar
        self._vet.append(item)
    
    def dequeue(self): # desenfileirar
        if not self.is_empty():
            return self._vet.pop(0)

    def front(self): # mostrar o 1o da fila, sem remover!
        return self._vet[0]
                
    def is_empty(self): # retorna se a fila esta vazia
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self): # representacao da fila como string
        return str(self._vet)


if __name__ == "__main__":
    limpaTela()
    senhas = Fila()
    senhasChamadas = Fila()
    contador = 0
    while True:
        print("1) Obter nova senha\n2) Chamar próxima senha\n3) Mostrar senhas chamadas\n4) Sair\n")
        escolha = str(input("Escolha uma opção:"))
        if escolha == "1":
            pass
        elif escolha == "2":
            pass
        elif escolha == "3":
            pass
        elif escolha == "4":
            limpaTela()
            print("Você escolheu sair")
            break
        else:
            limpaTela()
            print("Escolha uma opção válida!\n")


    