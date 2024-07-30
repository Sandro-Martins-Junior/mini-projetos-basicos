km = int(input("quantos km foram rodados"))
dias = float(input("quantos dias ficou com o carro"))

dia = 60
km_rodado= 0.15

preco1 = km * km_rodado
preco2 = dias * dia
resultado = preco1 + preco2
print("devera pagar ",resultado)