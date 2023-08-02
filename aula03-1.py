#aposentadoria idade > 60 e tempo de serviço >30
idade = 68
tempo_servico = 10


if idade>=60 and tempo_servico>30:
    print("Apto para aposentadoria")
else:
    print("Continuar trabalhando")

#Quantidade de faltas maior do que 8 e media menor do que 6 o aluno está reprovado
faltas = 20
media  = 9

if media < 0 or media > 10:
    print("Valor da média informado incorretamente")
    print("****fim da verificação*****")
else:
    if faltas>8 or media<6:
        print("Você está reprovado")
        if faltas>8:
            print("Você excedeu o limite de faltas")
        if media<6:
            print("Você foi reprovado por nota")
    else:
        print("Você está aprovado")

