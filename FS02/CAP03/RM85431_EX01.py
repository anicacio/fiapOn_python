quantidadeDeAlimentos = int(input("Informe a quantidade de alimentos ingeridos: "))

contadorDeAlimentos = 0
somaCalorias = 0

while contadorDeAlimentos < quantidadeDeAlimentos:
    somaCalorias = somaCalorias + int(input("Informe a caloria do alimento: "))
    contadorDeAlimentos += 1

print("Você ingeriu {} alimentos e um total de calorias {}.".format(contadorDeAlimentos, somaCalorias))