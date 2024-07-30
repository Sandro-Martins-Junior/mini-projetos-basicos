anos = int(input("escreva quantos anos tem :"))

meses = 12
dias = 365
horas = 24
min = 60
segundos = 60

dias = dias * anos
horas = horas * dias
min = min * horas

tempo_de_vida = segundos * min

print(tempo_de_vida, "segundos de vida")