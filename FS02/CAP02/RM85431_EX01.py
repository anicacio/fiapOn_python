peso = int(input("Digito o peso: "))
altura = float(input("Digite a altura: "))

imc = peso/(altura*altura)

if imc < 16:
    print("Baixo peso Grau III")
elif imc < 17:
    print("Baixo peso Grau II")
elif imc < 18.5:
    print("Baixo peso Grau I")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II")
elif imc >= 40:
    print("Obesidade Grau III")