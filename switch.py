import os
from calc import Calculadora
x = Calculadora()


def switch (case):
    os.system('cls')
    if case == '0':
        print(x.soma(float(input("Digte o primeiro numero: ")), float(input("Digte o primeiro numero: "))))
    elif case == '1':
        print(x.subtrai(float(input("Digte o primeiro numero: ")), float(input("Digte o primeiro numero: "))))
    elif case == '2':
        print(x.divide(float(input("Digte o primeiro numero: ")), float(input("Digte o primeiro numero: "))))
    elif case == '3':
        print(x.multiplica(float(input("Digte o primeiro numero: ")), float(input("Digte o primeiro numero: "))))
    elif case == 'S':
        print('Obrigado por usar nossa calculadora.')
    else:
        print("informe uma opção valida")
    os.system('pause')
