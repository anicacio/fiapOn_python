assinatura = input("Informe sua assinatura(Basic, Silver, Gold ou Platinum): ")
faturamento = float(input("Informe o faturamento anual: "))

if assinatura == "Basic":
    bonus = faturamento * 0.3
elif assinatura == "Silver":
    bonus = faturamento * 0.2
elif assinatura == "Gold":
    bonus = faturamento * 0.1
elif assinatura == "Platinum":
    bonus = faturamento * 0.05

print("Bonus a ser pago: {}".format(bonus))