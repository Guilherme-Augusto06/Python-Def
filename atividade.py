import os 
re = 0
alt = 0
li = 0
sa = 0

atletas = {}

s = 0
while s == 0:
    os.system("cls")
    def Menu(x):
        if x == 1:
            Registrar()
        elif x == 2:
            Alterar()
        elif x == 3:
            Listar()
        elif x == 4:
            Sair()
            print("")
        else:
            print("opção inválida")

            x = input ()

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


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
            s == 0

    def Listar():
            if len(atletas) == 0:
                print("Nenhum atleta registrado.")
            else:
                print("Médias dos atletas:")
                s = 0
            for nome, saltos in atletas.items():
                media = sum(saltos) / 5
                print(f"{nome}: {media:.2f}")
                

    def Sair():

        s = 1


    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        

    op = int(input(" informe o valor desejado \n 1 - Registrar \n 2 - Alterar \n 3 - Listar \n 4 - Sair"))



    Menu(op)

    if op == 1:
        Registrar

    elif op == 2:
        Alterar

    elif op == 3:
        Listar

    elif op == 4 :
        Sair
        s = 1
     
