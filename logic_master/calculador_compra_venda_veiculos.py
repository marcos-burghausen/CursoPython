valor_pago = float(input("Digite o valor pago pelo veículo: "))
valor_investido = float(input("Digite o valor investido em melhorias: "))
valor_venda = float(input("Digite o valor de venda do veículo: "))

gastos_totais = valor_pago + valor_investido
lucro_prejuizo = valor_venda - gastos_totais

print(f"Gastos totais com o veículo: R$ {gastos_totais:.2f}")
if lucro_prejuizo > 0:
    print(f"Lucro obtido na venda: R$ {lucro_prejuizo:.2f}")
elif lucro_prejuizo < 0:
    print(f"Prejuízo na venda: R$ {abs(lucro_prejuizo):.2f}")
else:
    print("Nenhum lucro ou prejuízo na venda.")
