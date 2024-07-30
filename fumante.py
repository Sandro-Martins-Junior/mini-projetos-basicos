cigarros = int(input("qunatos cigarros vc fuma por dia ?"))
anos = float(input("quantos anos vc fuma ? "))

tempo_fumando_min = 10 * cigarros * 365
total = tempo_fumando_min * anos
horas = total / 60
resultado = horas / 24

print(resultado, "dias perdidos por conta do cigarro")