#Crie um programa que solicita a idade do usuário e verifica 
#se ele é um bebê (0 a 2 anos), uma criança (3 a 12 anos), 
#um adolescente (13 a 17 anos) ou um adulto (18 anos ou mais).

idade = int (input("Digite sua idade: "))

if idade <= 2:
    print("É um bebê!")
elif 3 <= idade <= 12:
    print("É uma criança!")
elif 13 <= idade <= 17:
    print("É um adolescente!")    
else:
    print("Você é um adulto!")

