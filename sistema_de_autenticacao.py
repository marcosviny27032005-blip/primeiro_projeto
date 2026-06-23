from operator import and_

dados = input("Por favor Informe o seu nome: ")
senha = int(input("Por favor Digite a senha: "))
admin = "admin"
senha_correta = 9988
if dados == admin and senha == senha_correta:
    print("Acesso Perminito")
else:
    print("Acesso Negado!!")