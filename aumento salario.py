salario = float(input("qual seu salario"))

aumento1 = 10
aumento2 = 15

if salario > 1250:
    a = (salario * aumento1) / 100
    print(f"voce tera um aumento  de {a:5.2f}")
if salario <= 1250:
    b = (salario* aumento2) / 100
    print(f"seu aumento sera de {b:5.2f}")