nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média do aluno é: {media:.2f}")

if media <= 4:
    print("O aluno está reprovado.")
elif media <= 6:
    print("O aluno está de recuperação.")
else:
    print("O aluno está aprovado.")
