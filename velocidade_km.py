from selectors import SelectSelector
from xml.dom.minidom import ProcessingInstruction

velocidade = int(input("Digite a velocidade do carro: "))
if velocidade < 80:
    print(f"Boa viagem, sua velocidade é de {velocidade}km/h dirija com segurança!")
else:
    print(f"Você foi multado pois a sua velocidade é de {velocidade}km/h ")
