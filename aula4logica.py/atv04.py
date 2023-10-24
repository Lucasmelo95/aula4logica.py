
import random
alunos = []
sorteio = 3
while True:
    aluno = str(input('Vamos descobrir quem é o aluno sorteado. (digite 0 para parar o sorteio). Digite o nome da pessoa: '))
    if aluno == '0':
        break
    else:
        alunos.append(aluno)
if alunos != '0':
    sorteio = random.choice(alunos)
    print(sorteio, 'é o sorteado!!!')


