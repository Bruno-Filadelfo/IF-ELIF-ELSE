#Verificação de Número Maior, Menor ou Igual:
#Crie um programa que pede dois números ao usuário e informa se o primeiro número é maior, menor ou igual ao segundo número.
#MMI = Maior , Menor e Igual  
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num1 < num2:
    print(f"{num1} é menor que {num2}.")
else:
    print(f"{num1} é igual a {num2}.")

