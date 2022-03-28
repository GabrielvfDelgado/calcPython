import os
from switch import switch

    
if __name__ == "__main__":
    
    while True:
        os.system('cls')
        print("========================= Bem-vindo a Calculadora =========================")
        print("0 - Soma")
        print("1 - Subtracao")
        print("2 - Divisao")
        print("3 - Multiplicacao")
        print("S - Sair")
        opcao = input("Escolha uma das opcoes: ").upper()
        switch(opcao)
        if opcao == 'S':
            break;

