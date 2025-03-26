sair = 1
while sair == 1:
    
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / (altura * altura)

    print(f"Seu IMC é: {imc:.2f}")
    
    sair = int(input("Deseja sair? (Não - 1) (Sim - 2): "))