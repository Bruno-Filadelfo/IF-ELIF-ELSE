#Crie um programa que pede a idade de duas pessoas e informa qual delas é mais velha.

idade1 = int (input("Digite a idade da primeira pessoa: "))
idade2 = int (input("Digite a idade da segunda pessoa: "))

if idade1 > idade2:
    print("A primeira pessoa é mais velha.")
elif idade2 > idade1:
    print("A segunda pessoa é mais velha.")
else:
    print("As duas pessoas têm a mesma idade.")                                                               
