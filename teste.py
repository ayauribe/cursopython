while True:
    nota1 = float(input("Digite a nota do 1º bimestre: "))
    if 0 <= nota1 <= 10:
        break
while True:
    nota2 = float(input("Digite a nota do 2º bimestre: "))
    if 0 <= nota2 <= 10:
        break
while True:
    nota3 = float(input("Digite a nota do 3º bimestre: "))
    if 0 <= nota3 <= 10:
        break
while True:
    nota4 = float(input("Digite a nota do 4º bimestre: "))
    if 0 <= nota4 <= 10:
        break

media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 5:
    print(f"A média das notas foi {media:.2f}, o aluno foi aprovado!")
elif 3 <= media <=5:
    print(f"A média das notas foi {media:.2f}, o aluno está de recuperação!")
else:
    print(f"A média das notas foi {media:.2f}, o aluno foi reprovado!")
    
print("----------------------------------------")
print("|          FIM DO ANO LETIVO!          |")
print("----------------------------------------")