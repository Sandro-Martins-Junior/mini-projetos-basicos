preço = int(input("Preço da mercadoria :"))
porcentagem=float(input("valor de desconto :"))

valor_de_desconto= (preço * porcentagem) / 100

print(valor_de_desconto,"valor de desconto")

print(preço - valor_de_desconto ,"com o desconto")
