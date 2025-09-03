numero = int(input("Digite um numero: "))
escolha = input("Digite a opção desejada: 1 - Binário | 2 - Octal | 3 - Hexadecimal: ")
if escolha == "1":
    binario = bin(numero)[2:]
    print(f"Binário: {binario}")
elif escolha == "2":
    octal = oct(numero)[2:]
    print(f"Hexadecimal: {octal}")
elif escolha == "3":
    hexadecimal = hex(numero)[2:]
    print(f"Hexadecimal: {hexadecimal}")
else:
    print("Opção inválida!")