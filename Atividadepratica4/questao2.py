def media_turma():
    total_alunos = int(input("Quantos alunos há na turma? "))
    notas = []

    for i in range(total_alunos):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        notas.append(nota)

    media = sum(notas) / total_alunos
    print(f"A média da turma é: {media:.2f}")


media_turma()