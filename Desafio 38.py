primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite outro numero: "))

if primeiro_numero > segundo_numero:
    print(f"O primeiro numero {primeiro_numero} é maior que o segundo numero {segundo_numero}")
elif segundo_numero > primeiro_numero:
    print(f"O segundo numero {segundo_numero} é maior que o primeiro numero {primeiro_numero}")
else:
    print(f"Os numeros {primeiro_numero} e {segundo_numero} são iguais")