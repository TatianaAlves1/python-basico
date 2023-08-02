#Operadores lógicos
salario1 = 1000
salario2 = 1200
salario3 = 5000
print("-"*25)
print(f"{'Operador and(e)':^30}")
print(f"{'--Trabalhando condições relacionadas--'}")
print("Testando salario1:",salario1>salario2 and salario1>salario3)
print("Testando salario2:",salario2>salario1 and salario2>salario3)
print("Testando salario3:",salario3>salario1 and salario3>salario2)
print("-"*25)
print(f"{'Operador or(ou)':^30}")
print(f"{'--Trabalhando condições alternativas--'}")
print("Testando operador or com salario2:",salario1>salario2 or salario1>salario3)
print("Testando operador or com salario2:",salario2>salario1 or salario2>salario3)
print("Testando operador or com salario2:",salario3>salario1 or salario3>salario2)
print("-"*25)
print(f"{'Operador not(não)':^23}")
print(f"{'--Trabalhando com negação de condições--'}")
print("Testando salario3:",not(salario3>salario1 and salario3>salario2))