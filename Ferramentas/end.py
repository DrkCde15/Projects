import random

# Lista de ruas reais
ruas = ['Avenida Paulista', 'Rua Augusta', 'Avenida Atlântica', 'Rua Oscar Freire', 'Avenida Ipiranga']

# Lista de cidades e estados reais
cidades_estados = [
    ('São Paulo', 'SP'),
    ('Rio de Janeiro', 'RJ'),
    ('Belo Horizonte', 'MG'),
    ('Curitiba', 'PR'),
    ('Salvador', 'BA')
]

def gerar_enderecos_falsos(quantidade, tipo_residencia):
    enderecos_falsos = []
    for _ in range(quantidade):
        rua = random.choice(ruas)
        numero = random.randint(1, 9999)
        cidade, estado = random.choice(cidades_estados)
        cep = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"
        
        if tipo_residencia == 'A':
            apartamento = random.randint(1, 200)
            andar = random.randint(1, 20)
            endereco = f"{rua}, {numero}, Apt {apartamento}, Andar {andar}, {cidade} - {estado}, CEP {cep}"
        else:
            endereco = f"{rua}, {numero}, {cidade} - {estado}, CEP {cep}"
        
        enderecos_falsos.append(endereco)
    
    return enderecos_falsos

# Solicita a quantidade de endereços e o tipo de residência
quantidade = int(input("Quantos endereços falsos você quer gerar? "))
tipo_residencia = input("Os endereços serão de apartamentos (A) ou casas (C)? ").upper()

# Gera os endereços
enderecos = gerar_enderecos_falsos(quantidade, tipo_residencia)
for endereco in enderecos:
    print(endereco)