import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

item = input("Digite o nome do item: ")
valor = float(input("Digite o valor do item: "))
quantidade = int(input("Digite a quantidade de itens: "))

total = valor * quantidade
desconto = valor * 0.1
valor_final = total - desconto


print("Item: ", item)
print("Quantidade de itens: ", quantidade)
print(f"Valor total: R${locale.currency(total, grouping=True)}")
print(f"Desconto: R${locale.currency(desconto, grouping=True)}")
print(f"Valor final: R${locale.currency(valor_final, grouping=True)}")

