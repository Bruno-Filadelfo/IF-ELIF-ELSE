#Cálculo de Desconto:
#Crie um programa que solicita o preço de um produto e, com base nesse preço, aplica um desconto de acordo com a seguinte tabela:

#Preço <= 50: 5% de desconto
#50 < Preço <= 100: 10% de desconto
#Preço > 100: 15% de desconto

preco = float(input("Digite o preço do produto: "))

if preco <= 50:
    desconto = preco * 0.05
elif preco <= 100:
    desconto = preco * 0.1
else:
    desconto = preco * 0.15

preco_com_desconto = preco - desconto
print(f"Preço com desconto: R${preco_com_desconto:.2f}")
