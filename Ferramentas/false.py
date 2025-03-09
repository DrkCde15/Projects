import random
from datetime import datetime, timedelta

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

def gerar_numero_cartao():
    # Gerar os primeiros 15 dígitos do cartão de crédito aleatoriamente
    prefixo_cartao = [str(random.randint(0, 9)) for _ in range(15)]
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
        cartao = gerar_numero_cartao()
        cartoes.append(formata_cartao(cartao))
    return cartoes

def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
        cpf.append(11 - val if val > 1 else 0)
    return ''.join(map(str, cpf[:3])) + '.' + ''.join(map(str, cpf[3:6])) + '.' + ''.join(map(str, cpf[6:9])) + '-' + ''.join(map(str, cpf[9:]))

def gerar_rg():
    rg = [random.randint(0, 9) for _ in range(8)]
    return ''.join(map(str, rg[:2])) + '.' + ''.join(map(str, rg[2:5])) + '.' + ''.join(map(str, rg[5:8])) + '-' + str(random.randint(0, 9))

def gerar_data_nascimento():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2005, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%d/%m/%Y')

def gerar_telefone(estado):
    ddd = {
        'AC': ['68'], 'AL': ['82'], 'AP': ['96'], 'AM': ['92', '97'],
        'BA': ['71', '73', '74', '75', '77'], 'CE': ['85', '88'],
        'DF': ['61'], 'ES': ['27', '28'], 'GO': ['62', '64'],
        'MA': ['98', '99'], 'MT': ['65', '66'], 'MS': ['67'],
        'MG': ['31', '32', '33', '34', '35', '37', '38'],
        'PA': ['91', '93', '94'], 'PB': ['83'], 'PR': ['41', '42', '43', '44', '45', '46'],
        'PE': ['81', '87'], 'PI': ['86', '89'], 'RJ': ['21', '22', '24'],
        'RN': ['84'], 'RS': ['51', '53', '54', '55'],
        'RO': ['69'], 'RR': ['95'], 'SC': ['47', '48', '49'],
        'SP': ['11', '12', '13', '14', '15', '16', '17', '18', '19'],
        'SE': ['79'], 'TO': ['63']
    }.get(estado, ['11'])  # Default para SP
    return f"({random.choice(ddd)}) {random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

def gerar_dados():
    nomes = ["Rosa Pietra Sophia Fogaca", "João Silva", "Maria Oliveira", "Carlos Souza"]
    sexos = ["Feminino", "Masculino"]
    signos = ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]
    estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    cidades = {
        "AC": ["Rio Branco", "Cruzeiro do Sul"],
        "AL": ["Maceió", "Arapiraca"],
        "AP": ["Macapá", "Santana"],
        "AM": ["Manaus", "Parintins"],
        "BA": ["Salvador", "Feira de Santana"],
        "CE": ["Fortaleza", "Caucaia"],
        "DF": ["Brasília"],
        "ES": ["Vitória", "Cariacica"],
        "GO": ["Goiânia", "Anápolis"],
        "MA": ["São Luís", "Imperatriz"],
        "MT": ["Cuiabá", "Várzea Grande"],
        "MS": ["Campo Grande", "Dourados"],
        "MG": ["Belo Horizonte", "Uberlândia"],
        "PA": ["Belém", "Ananindeua"],
        "PB": ["João Pessoa", "Campina Grande"],
        "PR": ["Curitiba", "Londrina"],
        "PE": ["Recife", "Jaboatão dos Guararapes"],
        "PI": ["Teresina", "Parnaíba"],
        "RJ": ["Rio de Janeiro", "São Gonçalo"],
        "RN": ["Natal", "Mossoró"],
        "RS": ["Porto Alegre", "Caxias do Sul"],
        "RO": ["Porto Velho", "Ji-Paraná"],
        "RR": ["Boa Vista"],
        "SC": ["Florianópolis", "Joinville"],
        "SP": ["São Paulo", "Guarulhos"],
        "SE": ["Aracaju", "Nossa Senhora do Socorro"],
        "TO": ["Palmas", "Araguaína"]
    }
    bairros = ["Centro", "Jardim das Flores", "Vila Nova", "Maria Rachel"]
    enderecos = ["Rua João Patrício de Lima", "Avenida Paulista", "Rua das Flores", "Praça da Sé"]
    tipo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    estado = random.choice(estados)
    cidade = random.choice(cidades[estado])
    bairro = random.choice(bairros)
    endereco = random.choice(enderecos)
    cep = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"

    return {
        "Nome": random.choice(nomes),
        "CPF": gerar_cpf(),
        "RG": gerar_rg(),
        "Data de Nascimento": gerar_data_nascimento(),
        "Sexo": random.choice(sexos),
        "Signo": random.choice(signos),
        "Mãe": f"Rosângela {random.choice(['Antônia', 'Maria', 'Clara'])}",
        "Pai": f"Marcelo {random.choice(['Pedro', 'João', 'Carlos'])} Fogaca",
        "Email": f"{random.choice(nomes).lower().replace(' ', '.')}@example.com",
        "CEP": cep,
        "Endereço": endereco,
        "Bairro": bairro,
        "Cidade": cidade,
        "Estado": estado,
        "Telefone Fixo": gerar_telefone(estado),
        "Celular": gerar_telefone(estado),
        "Altura": f"1,{random.randint(50, 99)}",
        "Tipo Sanguíneo": random.choice(tipo_sanguineo)
    }

def verificar_bin(bin):
    print(f"Verificando BIN: {bin}")
    print("Banco: Banco Exemplo")
    print("País: Brasil")
    print("Tipo de Cartão: Crédito")

def testar_luhn(numero_cartao):
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        return checksum % 10
    
    valido = luhn_checksum(int(numero_cartao)) == 0
    print(f"O número do cartão {numero_cartao} é {'válido' if valido else 'inválido'}.")

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Gerar Cartão de Crédito")
        print("2. Verificar BIN")
        print("3. Testar Luhn")
        print("4. Gerar Dados")
        print("5. Gerar Cartões em Lote")
        print("6. Sair")
        opcao = input("Opção: ")
        
        if opcao == "1":
            cartao = gerar_numero_cartao()
            print(f"Cartão gerado: {formata_cartao(cartao)}")
        elif opcao == "2":
            bin = input("Digite os primeiros 6 dígitos (BIN): ")
            if len(bin) == 6 and bin.isdigit():
                verificar_bin(bin)
            else:
                print("BIN inválido. Deve conter exatamente 6 dígitos.")
        elif opcao == "3":
            numero_cartao = input("Digite o número do cartão: ")
            if numero_cartao.isdigit():
                testar_luhn(numero_cartao)
            else:
                print("Número do cartão inválido. Deve conter apenas dígitos.")
        elif opcao == "4":
            dados = gerar_dados()
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")
        elif opcao == "5":
            quantidade = int(input("Digite a quantidade de cartões de crédito que deseja gerar: "))
            cartoes = gera_cartoes_em_lote(quantidade)
            for cartao in cartoes:
                print(cartao)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()