from random import randint

def luhn(digits):
    """Calcula o dígito verificador pelo algoritmo de Luhn"""
    sum_ = 0
    reverse_digits = digits[::-1]
    for i, d in enumerate(reverse_digits):
        n = int(d)
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        sum_ += n
    return (10 - (sum_ % 10)) % 10

def gera_cartao():
    # Gerar os primeiros 15 dígitos do cartão de crédito aleatoriamente
    prefixo_cartao = [str(randint(0, 9)) for _ in range(15)]
    # Calcular o dígito verificador com base nos 15 dígitos gerados
    digito_verificador = luhn(prefixo_cartao)
    # Adicionar o dígito verificador ao número do cartão
    prefixo_cartao.append(str(digito_verificador))
    # Retornar o cartão no formato correto
    return ''.join(prefixo_cartao)

def formata_cartao(cartao):
    # Formatando o número do cartão no formato XXXX XXXX XXXX XXXX
    return f"{cartao[:4]} {cartao[4:8]} {cartao[8:12]} {cartao[12:16]}"

def gera_cartoes_em_lote(quantidade):
    cartoes = []
    for _ in range(quantidade):
        cartao = gera_cartao()
        cartoes.append(formata_cartao(cartao))
    return cartoes

# Pedindo ao usuário a quantidade desejada de cartões de crédito
quantidade_desejada = int(input("Digite a quantidade de cartões de crédito que deseja gerar: "))
cartoes_gerados = gera_cartoes_em_lote(quantidade_desejada)

# Exibindo os números de cartões de crédito gerados
for cartao in cartoes_gerados:
    print(cartao)