# Verificando se um numero eh negativo ou 0

numero = float(input("Digite um número: "))

if numero > 0:
    print("O numero é positivo")
elif numero < 0:   
    print("O numero é negativo")
else:
    print("O numero é zero")