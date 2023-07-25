import os

#DEF chama uma função
#SOMA é o nome da função
#A,B é o argumento
#S = A + B é a lógica da função
#RETURN é retorno (resultado) da função 
def soma (x,y):
    s = x+y

    if s > 0:
        v = True
    else:
        v = False
    return v

a = int(input("Informe um valor:"))
b = int(input("Informe um valor:"))


print(soma(a,b))

def ola():
    s = "ola senai"
    return s

print(ola())

os.system("pause")