#Aula 01 - Python básico
print("Hello, world!!!")
nome = "Tatiana Alves"
print("Seja bem-vindo ",nome,end="\n-----\n")
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


a = 10500.99999
b = a
print(a)
print(b)
b=15
print(f"{'Seja bem-vindo' : ^50}") 
print('-----'*5)
print(f'O valor é r$ {a:.2f}')

print("este é o valor de a %d e este o de b %d"%(a,b))