#Peça ao usuário para inserir seu peso e altura e calcule o IMC = Índice de massa corporal, informando a categoria.

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}, você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"Seu IMC é {imc:.2f}, você está com peso normal.")
elif 25 <= imc < 30:
    print(f"Seu IMC é {imc:.2f}, você está com sobrepeso.")
else:
    print(f"Seu IMC é {imc:.2f}, você está obeso.")

