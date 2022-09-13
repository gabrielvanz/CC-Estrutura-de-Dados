class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __str__(self):
        return str(self.dado)

# ##############################
# Lista Simplesmente Encadeada
# [NODO] => [NODO] => None
class LSE:
    def __init__(self):
        self.head = None # cabeca | inicio
        self.tail = None # cauda  | fim
        self.tam = 0     # quantidade de elementos

    def is_empty(self): # retorna se a lista esta vazia
        if (self.head is None and self.tail is None) or self.tam == 0:
            return True
        return False
        
    def inserirFim(self, novo): # similar ao append da List
        self.tam += 1        
        if self.is_empty():
            # lista vazia
            self.head = novo
            self.tail = novo            
        else:
            # ja possui itens
            ## o tail atual deve apontar para o novo
            ## o tail sera atribuido para o novo
            ultimo = self.tail
            ultimo.proximo = novo
            self.tail = novo            

    def inserirInicio(self, novo): # similar ao insert(0,item) da List
        self.tam += 1
        if self.is_empty():
            self.head = novo
            self.tail = novo
        else:
            # obtem o atual head
            # refaz apontamentos
            novo.proximo = self.head
            self.head = novo
                  
        
    def removerInicio(self):
        if self.is_empty():
            print('Lista Vazia!')
            return

        self.tam -= 1 # diminui o contador de itens
        removido = None
        item = self.head

        ## quando temos apenas 1 item
        if (self.head == self.tail):
            removido = self.head
            self.head = None
            self.tail = None
            return item

        # lista possui + de 1 item               
        else:            
            removido = self.head
            self.head = self.head.proximo
            removido.proximo = None

        return removido
            
    
    def removerFim(self):
        if self.is_empty():
            print('Lista Vazia!')
            
        ## precisamos descobrir quem eh o penultimo da lista!!
        removido = None
        item = self.head
        while (item != None):
            # quando tem apenas 1 item
            if (item == self.tail and item == self.head):
                self.head = None
                self.tail = None
                self.tam -= 1
                return item

            # quando tem mais de 1
            if (item.proximo != None and item.proximo == self.tail):
                removido = self.tail
                self.tail = item
                item.proximo = None
                self.tam -= 1
                return removido
            
            item = item.proximo
            
    def buscar(self, valor):
        if self.is_empty():
            print('Lista Vazia')
            return

        item = self.head
        while(item != None):
            if valor.dado == item.dado:
                return valor
                
            item = item.proximo

    def getPosicao(self,pos):
        #obtem um nodo que esta em determinada posição da lista
        if self.is_empty():
            print("Lista Vazia")
            return
        
        if (pos < self.tam-1 or pos > self):
            

        item = self.head
        contador = 0
        while(item != None):


            item = item.proximo
            contador += 1

    def imprimir(self):
        if (self.head is None and self.tail is None):
            print('Lista Vazia')
            return
            
        item = self.head
        while (item != None):
            print(item)
            item = item.proximo

    def imprimirLadoALado(self):
        saida = ''
        item = self.head
        while (item != None):
            if item == self.head:
                saida += '[' + str(item) + ']'
            else:
                saida += ' => ' + '[' + str(item) + ']'
            item = item.proximo
        print(saida)


## TESTES ##

lista = LSE()
lista.inserirFim( Nodo("ABC") )
lista.inserirFim( Nodo("DEF") )
lista.inserirFim( Nodo("GHI") )
lista.inserirFim( Nodo("JKL") )
lista.inserirInicio( Nodo("123") )
lista.inserirInicio( Nodo("456") )

achou = lista.buscar( Nodo("DEF") )
achou.proximo = None
print(achou)

lista.imprimirLadoALado()
