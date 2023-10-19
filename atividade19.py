# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
print("sua situação escolar")
nota1 = float(input("Digite a nota do aluno:"))
nota2 = float(input("Digite a nota do aluno:"))
med = (nota1+nota2)/2
if med<5:
    print(f"REPROVADO, sua média foi {med}.")
elif med<5 or med<6.9:
    print(f"RECUPERAÇÃO, sua média foi {med}.")
else: 
    print(f"APROVADO, sua média foi {med}.")