salario_bruto = float(input("Digite seu salario Bruto: "))
valor_parcela = float(input("Digite o valor da parcela: "))
porcentagem_salario = salario_bruto * 0.3
if valor_parcela <= porcentagem_salario:
    print("Crédito Aprovado")
else:
    print("Crédito Recusado")