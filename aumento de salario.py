usuario = int(input("qual seu salario atualmente"))
porcentagem = float(input("quantos porcentos gostaria de aumento ?"))

aumento = (usuario * porcentagem) / 100
resultado = usuario + aumento
print("seu salario será",resultado, "com o novo aumento ")