print("Bem -vindo à Calculadora de IMC!")

peso = float(input("Informe seu peso em kg: "))

altura = float(input("Informe sua altura em metros: "))

imc = peso / (altura**2)

print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com o peso normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
