import numpy as np

notas = np.array([
    [85, 92, 78],
    [70, 88, 91],
    [62, 75, 80]
])

#media de cada aluno
medias_alunos = np.mean(notas, axis=1) #axis=1 = média por linha
print("Média por aluno: ", medias_alunos)

#media de cada avaliação
medias_avaliacoes = np.mean(notas, axis=0) #axis=0  =  média por linha
print("Média por avaliação: ", medias_avaliacoes)