quantidadeDeAlunos = 50

somaNotasAlunosPares = 0
somaNotasAlunosImpares = 0
contadorAlunos = 0

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
for numeroDoAluno in range(1, quantidadeDeAlunos):
    if numeroDoAluno % 2 == 0:
        somaNotasAlunosPares = somaNotasAlunosPares + int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(numeroDoAluno)))
        contadorAlunos += 1
mediaNotasAlunosPares = somaNotasAlunosPares / contadorAlunos

contadorAlunos = 0
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
for numeroDoAluno in range(1, quantidadeDeAlunos):
    if numeroDoAluno % 2 != 0:
        somaNotasAlunosImpares = somaNotasAlunosImpares + int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(numeroDoAluno)))
        contadorAlunos += 1
mediaNotasAlunosImpares = somaNotasAlunosImpares / contadorAlunos

if mediaNotasAlunosImpares > mediaNotasAlunosPares:
    print("Notas dos alunos impares maior: {}".format(mediaNotasAlunosImpares))
elif mediaNotasAlunosPares > mediaNotasAlunosImpares:
    print("Notas dos alunos pares maior: {}".format(mediaNotasAlunosPares))
else:
    print("Notas iguais: Pares: {} e Impares: {}".format(mediaNotasAlunosPares, mediaNotasAlunosImpares))