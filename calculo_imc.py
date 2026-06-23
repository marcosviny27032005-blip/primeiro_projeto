peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso idela (parabéns)")
elif imc >= 25.0 and imc <= 29.9:
    print("Levemente acima do peso")
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade Grau I")
else:
    print("Obesidade Severa/Mórbida")