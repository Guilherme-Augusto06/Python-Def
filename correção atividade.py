import os
atletas = {}
s = 0
def Menu(x):
    if x == 1:
        Registrar()
        s = 0
    elif x == 2:
        Alterar()
        s = 0
    elif x == 3:
        Listar()
        s = 0
    elif x == 4:
        Sair()
        s = 1
    else:
        print("opção inválida") 

    return 1
def Registrar():
    nome = input("Nome do atleta: ")
    saltos = []
    for i in range(5):
        salto = float(input(f"Digite o valor do salto {i+1}: "))
        saltos.append(salto)
        atletas[nome] = saltos
        print("Registro concluído.")
        s == 0


def Alterar():
        nome = input("Nome do atleta: ")
        if nome in atletas:
            saltos = atletas[nome]
            print(f"Saltos registrados: {saltos}")
            num_salto = int(input("Digite o número do salto que deseja alterar (1 a 5): "))
            if 1 <= num_salto <= 5:
                novo_salto = float(input("Digite o novo valor do salto: "))
                saltos[num_salto-1] = novo_salto
                atletas[nome] = saltos
                print("Alteração concluída.")
                s = 0
            else:
                print("Número de salto inválido.")
        else:
            print("Atleta não registrado.")
            s = 0

def Listar():
            if len(atletas) == 0:
                print("Nenhum atleta registrado.")
            else:
                print("Médias dos atletas:")
                s = 0
            for nome, saltos in atletas.items():
                media = sum(saltos) / 5
                print(f"{nome}: {media:.2f}")
def Sair (): 




while s == 0:
    op = int(input(" informe o valor desejado \n 1 - Registrar \n 2 - Alterar \n 3 - Listar \n 4 - Sair"))
    s = Menu(op)
    print(s)
    os.system("pause")
