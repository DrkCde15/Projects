from random import randint

def gera_cpf():
    def calcula_digito(cpf):
        soma = 0
        for i, j in enumerate(range(len(cpf)+1, 1, -1)):
            soma += int(cpf[i]) * j
        digito = 11 - soma % 11
        return digito if digito < 10 else 0

    cpf = [randint(0, 9) for _ in range(9)]
    primeiro_digito = calcula_digito(cpf)
    cpf.append(primeiro_digito)
    segundo_digito = calcula_digito(cpf)
    cpf.append(segundo_digito)

    return ''.join(map(str, cpf))

def formata_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def gera_cpfs_em_lote(quantidade):
    cpfs = []
    for _ in range(quantidade):
        cpf = gera_cpf()
        cpfs.append(formata_cpf(cpf))
    return cpfs

# Pedindo ao usuário a quantidade desejada de CPFs
quantidade_desejada = int(input("Digite a quantidade de CPFs que deseja gerar: "))
cpfs_gerados = gera_cpfs_em_lote(quantidade_desejada)

# Exibindo os CPFs gerados
for cpf in cpfs_gerados:
    print(cpf)