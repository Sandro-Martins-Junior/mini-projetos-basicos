from random import randint
itens = ("Pedra", "Papel","Tesoura")
computador = randint(0,2)
print("""suas escolhas são 
[0] Pedra
[1] Papel
[2] Tesoura""")
jogador = int(input("qual é sua jogada? "))
print("-="*10)
print("computador jogou {}".format(itens[computador]))
print("o jogador escolheu {}".format(itens[jogador]))
print("-="*10)
if computador == 0:
    if jogador == 0:
        print("empate")
    elif jogador == 1:
        print("jogador ganhou")
    elif jogador == 2:
        print("computador venceu")
    else:
        print("opção invalida")
elif computador == 1:
    if jogador == 0:
        print("computador venceu")
    elif jogador == 1:
        print("empate")
    elif jogador == 2:
        print("jogador ganhou")
    else:
        print("jogada invalida")
elif computador ==2:
   if jogador == 0:
       print("jogador ganhou")
   elif jogador == 1:
       print("computador ganhou")
   elif jogador==2:
       print("empate")
   else:
        print("jogada invalida")

print(input("fim de jogo"))