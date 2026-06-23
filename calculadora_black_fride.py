valorcompra = float (input("Valor Total da Compra: "))
if  valorcompra <= 100.00:
    print("InfeliZmente não possui desconto")
elif valorcompra >= 100.01 and valorcompra <= 300.00:
    print("Possui 5% de Desconto")
    desconto = valorcompra * 0.05
    total = valorcompra - desconto
    print(f"o valor da sua compra sem o desconto é de {valorcompra} e o desconto é de {desconto:.2f} o valor total com o desconto é de {total:.2f}")
elif valorcompra >= 300.01 and valorcompra <= 500.00:
    print("Você tem 10% de desconto")
    desconto = valorcompra * 0.1
    total = valorcompra - desconto
    print(f"o valor da sua compra sem o desconto é de {valorcompra} e o desconto é de {desconto:.2f} o valor total com o desconto é de {total:.2f}")