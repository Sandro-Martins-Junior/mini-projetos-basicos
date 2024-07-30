import sys

nome = input("digite um nome:")
print(f"Óla {nome}, tdo bem ?")
print(f"{nome}, Aqui vc vai poder calcular sua comissão ")
print("bora la !!!!")




vendas = int(input("Digite qunato voce vendeu esse mes : "))
porcentagem = float(input("Agora a porcentagem da sua comissão :"))
comissão = (vendas * porcentagem) / 100

print(f"vc recebera esse mes R${comissão:5.2f}")


resposta  = input(f"{nome} ficou feliz com o valor da sua comissão? ")

if resposta.lower()=="sim":
      print("Que otimo, voce merece cada centavo desse dinheiro :)")
else:
      print("Que pena , pelo menos voce tem uma familia que te ama MTOOOO ")


print(f"Ate a proxima {nome}, saiba que eu te amo mto , sempre estarei do seu lado S2")


while True:
  respostaa = input("digite 'sair' para encerrar a sessão: ")

  if resposta.lower() == 'sair':
      print("Encerrando o programa...")
      sys.exit()

  print(f"Voce digitou: {respostaa}")
