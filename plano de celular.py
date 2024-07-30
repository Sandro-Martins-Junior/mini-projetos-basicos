minutos = int(input("quantos minutos vc usou esses mes ?  "))
if minutos <200:
  preço = 0.20
elif minutos< 400:
  preço = 0.18
else:
  preço = 0.15
print(f"voce vai pagar este mes: R${minutos * preço:6.2f}")