from random import randint

computador = randint(0,10)
print("Sou seu computador .... Acabei de pensar em um numero entre  0 e 10")
print("Sera que voce consegue acertar qual numero é ? ")
acertou = False
palpites = 0

while not  acertou:
   jogador=int(input("qual seu palpite ?  "))
   palpites += 1
   if jogador == computador:
    acertou = True
   else:
     if jogador < computador:
        print("Mais... Tente outra vez. ")
     elif jogador > computador:
        print("Menos ... Tente outra vez. ")
if palpites >=4:
  print("Acertou com {} tentativas . Voce é muitoooo ruimm ".format(palpites))
elif palpites >=3:
    print("Voce acertou com {} tentativas , não esta nem bom nem ruim...".format(palpites))
elif palpites < 3:
  print("Voce mandou muitooo bem ,Acertou como {} tentativas . Parabens".format(palpites))


print(input("fim de jogo"))
