listaAprovados = []

with open(file="data/estudantes/lista_notas.txt") as alunosFile:
    for line in alunosFile:
        student_grade = line
        student_grade = student_grade.split(" ")
        if int(student_grade[1]) < 6:
            listaAprovados.append(student_grade[0] + "\n")

with open(file="data/estudantes/lista_aprovados.txt", mode="w") as aprovados:
    print(listaAprovados)
    aprovados.writelines(listaAprovados)
