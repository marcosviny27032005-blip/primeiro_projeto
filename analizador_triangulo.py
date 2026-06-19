reta_triangulo1 = int(input("Digite o primeiro cumprimento"))
reta_triangulo2 = int(input("Digite o segundo cumprimento"))
reta_triangulo3= int(input("Digite o terceiro cumprimento"))
if reta_triangulo1 + reta_triangulo2 >= reta_triangulo3 and reta_triangulo1 + reta_triangulo3 >= reta_triangulo2 and reta_triangulo2 + reta_triangulo3 >= reta_triangulo1:
    print("Triangulop Valido")
    if reta_triangulo3 == reta_triangulo1 and reta_triangulo2 == reta_triangulo3:
        print("Equilátero")
    elif reta_triangulo3 == reta_triangulo2 or reta_triangulo2 == reta_triangulo1:
        print("Isósceles")
    else:
        print("escaleno")

else:
    print("Triangulo Invalido")

