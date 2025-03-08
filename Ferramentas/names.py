import random

nomes_masculinos = ['João', 'Pedro', 'Lucas', 'Mateus', 'Rafael']
nomes_femininos = ['Maria', 'Ana', 'Carla', 'Beatriz', 'Júlia']
sobrenomes = ['Silva', 'Souza', 'Oliveira', 'Pereira', 'Santos']

def gerar_nomes_falsos(quantidade, genero):
    nomes_falsos = []
    for _ in range(quantidade):
        if genero == 'M':
            nome = random.choice(nomes_masculinos)
        else:
            nome = random.choice(nomes_femininos)
        sobrenome = random.choice(sobrenomes)
        nomes_falsos.append(f"{nome} {sobrenome}")
    return nomes_falsos

# Solicita a quantidade de nomes e o gênero
quantidade = int(input("Quantos nomes falsos você quer gerar? "))
genero = input("Os nomes serão masculinos (M) ou femininos (F)? ").upper()

# Gera os nomes
nomes = gerar_nomes_falsos(quantidade, genero)
for nome in nomes:
    print(nome)