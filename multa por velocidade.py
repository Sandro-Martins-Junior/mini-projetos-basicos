velocidade = int(input("velocidade do carro"))

multa = 5

multa_por_km= (velocidade - 80)* multa

resulta = multa_por_km

if resulta > 0:
  print( f"voce foi multado em {resulta:6.2f}")
else:
    print("voce nao foi multado")