from operator import and_

temperatura = int(input("Digite a temperatura da cidade: "))
if temperatura <15:
    print(f"Esta muito frio pois esta {temperatura}°C")
elif temperatura >=15 and temperatura <=25:
    print(f"Clima esta otimo pois esta {temperatura}°C")
else:
    print(f"Ta quente pra caramba ta {temperatura}°C")