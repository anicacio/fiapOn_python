print("Informar os votos de cada dia da semana...")
seg = int(input("Segunda-feira: "))
ter = int(input("Terça-feira: "))
qua = int(input("Quarta-feira: "))
qui = int(input("Quinta-feira: "))
sex = int(input("Sexta-feira: "))

if seg > ter and seg > qua and seg > qui and seg > sex:
    print("Dia mais votado Segunda-feira com {} votos.".format(seg))
elif ter > seg and ter > qua and ter > qui and ter > sex:
    print("Dia mais votado Terça-feira com {} votos.".format(ter))
elif qua > seg and qua > ter and qua > qui and qua > sex:
    print("Dia mais votado Quarta-feira com {} votos.".format(qua))
elif qui > seg and qui > ter and qui > qua and qui > sex:
    print("Dia mais votado Quinta-feira com {} votos.".format(qui))
elif sex > seg and sex > ter and sex > qua and sex > qui:
    print("Dia mais votado Sexta-feira com {} votos.".format(sex))
else:
    print("Empate em dois ou mais dias")