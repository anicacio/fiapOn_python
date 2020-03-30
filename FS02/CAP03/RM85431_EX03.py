minutoAtual = int(input("Digite o minuto atual: "))

resultado = 1

for i in range(2, minutoAtual + 1):
    resultado = resultado * i

print("Senha para desbloqueio: LIBERDADE{}".format(resultado))