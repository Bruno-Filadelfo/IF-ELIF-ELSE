# Solicite dois números do usuário
num1 = float (input("Digite o primeiro número: "))
num2 = float (input("Digite o segundo número: "))


# Verifique e imprima qual número é maior
if num1 > num2:
    print(f'{num1} é maior que {num2}.')
elif num1 < num2:
    print(f"{num1} é menor que {num2}.")
else:
    print("Os números são iguais")    

