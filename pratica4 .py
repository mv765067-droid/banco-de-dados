presenças=["ana", "bruno", "carla"]
aluno = "bruno"
if aluno in presenças:
    print("Aprovação")
else:
    print("Reprovação")
    print(" recupera")
    aluno = "ana"
for nome, notas in turma.items():
   media = sum(notas) / len(notas)
   medias.append(media)
if media >= 7:
   situacao = "Aprovado"
elif media >= 5:
   situacao = "Recuperação"
else:
   situacao = "Reprovado"
       