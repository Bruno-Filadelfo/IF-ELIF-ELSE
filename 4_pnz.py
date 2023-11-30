#Verificação de Número Positivo, Negativo ou Zero:
#Crie um programa que verifica se um número é positivo, negativo ou zero.
#PNZ = Positivo , Negativo , Zero
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
