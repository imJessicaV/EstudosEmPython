import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor_casa = float(input("Digite o valor da casa: "))
valor_salario = float(input("Digite o valor do seu salário: "))
meses_a_pagar = int(input("Digite a quantidade de meses a pagar: "))
entrada = input("Deseja dar uma entrada? (Sim/Não): ").strip().lower()

valor_parcela = 0
valor_com_entrada = 0
entrada_valor = 0
salario_maximo = valor_salario * 0.3

# Primeiro, calcula a parcela baseado na escolha de entrada
if entrada in ['sim', 's']:
    entrada_valor = float(input("Digite o valor da entrada: "))
    valor_com_entrada = valor_casa - entrada_valor
    valor_parcela = valor_com_entrada / meses_a_pagar
elif entrada in ['não', 'nao', 'n']:
    valor_parcela = valor_casa / meses_a_pagar
    valor_com_entrada = valor_casa
else:
    print("Resposta inválida. Digite 'Sim' ou 'Não'")
    exit()

# Depois, verifica se o financiamento pode ser aprovado
if valor_parcela > salario_maximo:
    print("\n--- FINANCIAMENTO RECUSADO ---")
    print("A parcela comprometerá mais de 30% do salário!")
    print(f"Valor da casa: {locale.currency(valor_casa, grouping=True)}")
    if entrada_valor > 0:
        print(f"Valor da entrada: {locale.currency(entrada_valor, grouping=True)}")
        print(f"Valor a financiar: {locale.currency(valor_com_entrada, grouping=True)}")
    print(f"Salário: {locale.currency(valor_salario, grouping=True)}")
    print(f"Valor máximo da parcela (30% do salário): {locale.currency(salario_maximo, grouping=True)}")
    print(f"Valor da parcela calculada: {locale.currency(valor_parcela, grouping=True)}")
else:
    print("\n--- FINANCIAMENTO APROVADO ---")
    print(f"Valor da casa: {locale.currency(valor_casa, grouping=True)}")
    if entrada_valor > 0:
        print(f"Valor da entrada: {locale.currency(entrada_valor, grouping=True)}")
        print(f"Valor a financiar: {locale.currency(valor_com_entrada, grouping=True)}")
    print(f"Parcela mensal: {locale.currency(valor_parcela, grouping=True)}")
    print(f"Quantidade de parcelas: {meses_a_pagar}")
    print(f"Salário: {locale.currency(valor_salario, grouping=True)}")
    print(f"Valor máximo da parcela (30% do salário): {locale.currency(salario_maximo, grouping=True)}")
    print(f"Comprometimento do salário: {locale.currency(valor_parcela, grouping=True)} ({(valor_parcela/valor_salario)*100:.1f}%)")