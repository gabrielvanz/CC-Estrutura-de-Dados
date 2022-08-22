import csv
import os 

tabela_periodica = {}
estados = {'l': 'Líquido', 'g': 'Gasoso', 's':'Sólido', 'd':'Desconhecido'} ## exemplo de dicionario

def limparTela():
    os.system('cls')

arquivo = csv.reader(open('tabela.csv'), delimiter=';')
for i,dado_linha in enumerate(arquivo):
    if i == 0: # pula primeira linha do arquivo
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0] # simbolo
    dados['nome'] = dado_linha[1] # nome
    dados['atomico'] = dado_linha[2] # n° atômico
    dados['linha'] = dado_linha[3] # linha
    dados['coluna'] = dado_linha[4] # coluna
    dados['estado'] = dado_linha[5] # estado

    
    # insere os dados na tabela periodica
    tabela_periodica[dados['simbolo']] = dados

while True:
    print("Tabela Periódica\n")
    print("Escolha uma das opções:")
    print("1 -> Dados existentes")
    print("2 -> Características existentes")
    print("3 -> Características do elemento")
    print("4 -> Sair")

    option = str(input())
    limparTela()

    if option == '1':
        
        print("\nElementos existentes no banco de dados:")
        for name in tabela_periodica.keys():
            print("-> "+ name)
        print()
    
    elif option == '2':
        print("\nCaracterísticas existentes no banco de dados:")
        for name in tabela_periodica['Ti'].keys():
            print("-> "+name)
        print()

    elif option == '3':
        
        elemento = input('\nInsira o símbolo do elemento para ver suas caracteristicas: ')
        if elemento in tabela_periodica:
            carac = input("\nInsira qual característica deseja ver: ")
            while carac not in tabela_periodica[elemento]:
                print("Caracteristica " + carac + " não encontrado no banco de dados")
                carac = input("\nInsira qual característica deseja ver: ")
            print()
            print(tabela_periodica[elemento][carac])
            print()
        else:
            print("Elemento " + elemento + " não encontrado no banco de dados")

    elif option == '4':
        break

