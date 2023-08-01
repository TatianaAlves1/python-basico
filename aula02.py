
valor1 = 10
valor2 = 77
#continuação de operadores aritméticos
print(f"{'Verificação de Operadores Aritméticos'}")
print(f"{'Exponenciação: '} {valor1**3:.2f}")
print(f"Divisão: {valor1/valor2:.2f}")
print("Divisão sem decimais: ",valor1//valor2)
print("Módulo(Resto) da divisão", valor1%3)
#Operadores comparação (relacionais)
print("Maior valor 1 maior do que Valor2: ",valor1>valor2)
print("Maior valor 1 maior ou igual ao Valor2: ",valor1>=valor2)
print("Maior valor 1 menor do que Valor2: ",valor1<valor2)
print("Maior valor 1 menor ou igual ao Valor2: ",valor1<=valor2)
print("Maior valor 1 é igual ao Valor2: ",valor1==valor2)
print("Maior valor 1 é diferente do Valor2: ",valor1!=valor2)

try:
    valor = float(input("Informe um número:"))
    if valor>0:
        print("Valor positivo")
    elif valor == 0:
        print("Valor neutro")
    else:
        print("Valor negativo")
except:
    print("valor incorreto!!!\nPor favor, verifique o número informado!!!")