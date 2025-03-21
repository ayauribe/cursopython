def verificar_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10, tente novamente!")
        except ValueError:
            print("A nota deve estar entre 0 e 10, tente novamente!")

nota1 = verificar_nota("Digite a nota do 1º bimestre: ")
nota2 = verificar_nota("Digite a nota do 2º bimestre: ")
nota3 = verificar_nota("Digite a nota do 3º bimestre: ")
nota4 = verificar_nota("Digite a nota do 4º bimestre: ")

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