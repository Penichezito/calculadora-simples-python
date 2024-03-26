def bem_vindo ():
    print("Calculadora Simples em Python")
    print("#############################")
    calculator()

def calculator():
    
    print("\nQual operação deseja executar? (1) Soma (2) Subtração (3) Multiplicação (4) Divisão (5) Outra")
    operation = int(input("Digite a operação a ser realizada: "))

    if(operation != 1 and operation != 2 and operation != 3 and operation != 4 ):
        print ("Desculpe esta calculadora ainda não suporta outras operaçãoes. Por favor, execute o programa novamente.")
        return

    first_number = int(input("Digite o primeiro número: "))
    second_number = int(input("Digite o segundo número: "))

    if (operation == 1):
        print("O resultado é", first_number + second_number)
    elif(operation == 2):
        print("O resultado é", first_number - second_number)    
    elif(operation == 3):
        print("O resultado é", first_number * second_number)
    else:
        print("O resultado é", first_number / second_number)

        calculator_again()

def calculator_again():
    calc_again = input("Deseja realizar outra operação? Por favor, Digite [S] para SIM e [N] para NÂO: ")

    if calc_again.upper() == "S":
        calculator()
    elif calc_again.upper() == "N":
        print("Até a próxima!")
    else:
        print("Opção inválida.")
        calc_again()



          
