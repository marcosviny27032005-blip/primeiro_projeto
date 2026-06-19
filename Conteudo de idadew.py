idade = int(input("Digite o ano do seu nascimento: "))
ANO_ATUAL = 2026

if (ANO_ATUAL - idade) >= 16:
    print("acesso ao filme está liberado")
else:
    print("Acesso bloqueado: Conteúdo não recomendado para menores de 16 anos.")