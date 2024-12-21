# Calculadora de IMC

peso = float(input("Quantos quilos você pesa? "))
altura = float(input("Quantos metros você mede? "))

imc = peso / (altura ** 2)

peso_ideal = (imc >= 18.5) and (imc <= 24.9)

print("Seu IMC é: ", imc)
print("Você está com o peso ideal? : ", peso_ideal)