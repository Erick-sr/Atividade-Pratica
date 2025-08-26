valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15


valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Valor em Reais: R$ {valor_reais}")
print(f"Valor em Dólares: $ {valor_dolar:.2f}")
print(f"Valor em Euros: € {valor_euro:.2f}")