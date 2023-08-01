from datetime import datetime
#Aula 01 - Python básico
print("Hello, world!!!")
nome = "Tatiana Alves"
print("Seja bem-vindo ",nome,end="\n-----\n")
import math
print("O cruso de python contém ...")
# aluno = input("informe seu nome: ")
# print(type(aluno))
# idade = int(input("Informe sua idade:"))
# print(type(idade))
print("-"*50)
#mostrar o dobro da idade
# print(idade*2)
txt= """
    uis sed mi diam. Nulla facilisi. Duis iaculis dapibus libero, at pulvinar felis dapibus eu. Sed maximus lorem eu elit ullamcorper molestie. Aliquam vel blandit enim. Cras dolor arcu, scelerisque eget diam sit amet, cursus laoreet enim. 
    --Donec vel ultricies dui. Curabitur dapibus rutrum tortor non dictum. Ut sollicitudin rutrum mauris, a condimentum tellus condimentum sit amet. Vestibulum convallis ullamcorper nulla vitae pulvinar. Mauris fringilla, odio ac congue blandit, magna dui tempor ipsum, sed volutpat libero ipsum vel nisi.
"""
print(txt)
valor1 = 5
valor2 = 12.4569
print("Soma: ",valor1+valor2,"\n")
print("Subtração",valor1-valor2,"\n")
print("Multiplicação: ",valor1*valor2,"\n")
print("Divisão: ",valor1/valor2,"\n")
print("Divisão sem decimais ",valor1//valor2,"\n")

#alinhamentos
print(f"{'Seja bem-vindo':^50}")
print(f"{'Valor:':>20}{valor1:>20}")
#f strings do python
print(f"O 1º valor é {valor1:.2f} e o segundo valor é {math.trunc(valor2)}")
print(f"O 1º valor é {valor1:.2f} e o segundo valor é {valor2:.2f} e soma é {valor1+valor2:.2f}")
#usando marcadores
print("O valor 1 é %s e o valor2 é %s"%(valor1,valor2))
#Usando format
print("O 1º valor é {:d} e o segundo valor é {:.2f}".format(valor1,valor2),end="\n**********\n")
print(f"{'Todas as variáveis':^50}")
print(valor1,valor2,sep=" - ")
print(datetime.today())
print(math.sqrt(valor1))
prtc =0.25
print("O percentual é {:.2%}".format(prtc))