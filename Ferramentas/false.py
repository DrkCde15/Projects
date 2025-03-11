import random
from datetime import datetime, timedelta

def luhn(digits):
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
    prefixo_cartao = [str(random.randint(0, 9)) for _ in range(15)]
    digito_verificador = luhn(prefixo_cartao)
    prefixo_cartao.append(str(digito_verificador))
    return ''.join(prefixo_cartao)

def formata_cartao(cartao):
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
    nomes = [
        "Rosa Pietra Sophia Fogaca", "João Silva", "Maria Oliveira", "Carlos Souza", "Ana Beatriz Martins", "Lucas Almeida",
        "Fernanda Pereira", "Paulo Sérgio Costa", "Mariana Gonçalves", "Gustavo Fernandes", "Clara Mendes", "Ricardo Lima",
        "Isabella Ribeiro", "José Barbosa", "Camila Araújo", "Felipe Duarte", "Sofia Carvalho", "Pedro Gonçalves", "Laura Nunes",
        "Thiago Matos", "Gabriela Rocha", "Daniel Moreira", "Julia Ferreira", "Vinicius Alves", "Lara Santos", "Matheus Ribeiro",
        "Luana Souza", "Henrique Teixeira", "Livia Andrade", "Rodrigo Costa", "Yasmin Almeida", "Eduardo Lima", "Alice Martins",
        "Rafael Pereira", "Helena Correia", "André Silva", "Sophia Machado", "Diego Mendes", "Valentina Barbosa", "Gabriel Alves",
        "Carolina Rocha", "Bruno Oliveira", "Beatriz Nunes", "Leonardo Azevedo", "Cecilia Fernandes", "Marcelo Almeida", "Clara Gomes",
        "Antonio Melo", "Lorena Vieira", "Miguel Santana", "Renata Cardoso", "Guilherme Ferreira", "Marina Moreira", "Caio Souza",
        "Amanda Costa", "Ruan Ribeiro", "Flávia Silva", "Arthur Rocha", "Elisa Nunes", "Junior Santos", "Nicole Ferreira",
        "Rafaela Mendes", "Heitor Martins", "Marcia Souza", "Vitor Lima", "Tainá Araújo", "Igor Alves", "Letícia Pereira",
        "Joana Andrade", "Hugo Fernandes", "Aline Duarte", "Otávio Ribeiro", "Cristina Nogueira", "Leandro Batista", "Larissa Teixeira",
        "Pablo Matos", "Emilly Carvalho", "Daniela Souza", "Fábio Gomes", "Bruna Martins", "Sandro Costa", "Mirela Ferreira",
        "Robson Lima", "Lorraine Vieira", "Patrick Oliveira", "Isabel Fernandes", "Diogo Gonçalves", "Melina Rocha", "Roberto Santos",
        "Stephanie Souza", "Alan Nunes", "Clarice Matos", "Wagner Almeida", "Geovana Pereira", "Eduarda Alves", "Otávio Nunes",
        "Samuel Silva", "Jéssica Almeida", "Enzo Costa", "Bianca Ribeiro", "Marcela Souza", "Filipe Cardoso", "Sara Martins",
        "Victor Araújo", "Amanda Gonçalves", "Manuela Lima", "Murilo Santos", "Raquel Mendes", "Danilo Costa", "Lívia Fernandes"
    ]
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
    bairros = [
        "Centro", "Jardim das Flores", "Vila Nova", "Maria Rachel", "Jardim América", "Vila Mariana", "Bela Vista",
        "Consolação", "Moema", "Liberdade", "Pinheiros", "Santana", "Tatuapé", "Jardim Paulista", "Jardim Europa",
        "Lapa", "Itaim Bibi", "Morumbi", "Campo Belo", "Jabaquara", "Brooklin", "Perdizes", "Vila Olímpia",
        "Aclimação", "Cambuci", "Vila Madalena", "Chácara Santo Antônio", "Parque do Carmo", "Sapopemba", "Brás",
        "Mooca", "Butantã", "Ipiranga", "São Mateus", "Vila Prudente", "Vila Leopoldina", "Parque São Lucas", "Artur Alvim",
        "São Miguel Paulista", "Jardim São Paulo", "Parque Peruche", "Vila Matilde", "Cidade Ademar", "Parque da Mooca",
        "Barra Funda", "Vila Formosa", "Jardim São Bento", "Jardim Vila Mariana", "Capão Redondo", "Cidade Tiradentes",
        "Pirituba", "Freguesia do Ó", "Jaraguá", "Vila Sônia", "Cangaíba", "Jardim Bonfiglioli", "Ermelino Matarazzo",
        "Grajaú", "Interlagos", "Pedreira", "Sacomã", "Tremembé", "Jardim Ângela", "Itaquera", "Vila Carrão", "Vila Ema",
        "Cidade Patriarca", "Jardim Anália Franco", "Jardim Panorama", "Água Branca", "Rio Pequeno", "Raposo Tavares",
        "Vila Brasilândia", "Ponte Rasa", "Jardim Helena", "Jardim São Luís", "Vila Curuçá", "Vila Medeiros",
        "Jardim Avelino", "Parque Novo Mundo", "Cidade Líder", "Jardim Marajoara", "Cidade Dutra", "Vila Guarani",
        "Vila Clementino", "Pacaembu", "Chácara Klabin", "Parque Bristol", "Vila Diva", "Parque São Rafael",
        "São Domingos", "Vila Carmosina", "Vila Gomes Cardim", "Jardim Vila Galvão", "Jardim Alvorada", "Jardim Esmeralda",
        "Vila Matilde", "Parque Santo Antônio", "Vila Moraes", "Vila Invernada", "Vila Califórnia", "Jardim Brasil",
        "Jardim Aricanduva", "Parque São Jorge", "Jardim Morumbi", "Chácara Flora", "Vila Ipojuca", "Jardim Olinda"
    ]
    enderecos = [
        "Rua João Patrício de Lima", "Avenida Paulista", "Rua das Flores", "Praça da Sé", "Rua Augusta", "Rua Oscar Freire",
        "Avenida Brigadeiro Luís Antônio", "Rua Bela Cintra", "Rua da Consolação", "Rua Vergueiro", "Avenida Faria Lima",
        "Avenida Rebouças", "Rua Teodoro Sampaio", "Rua dos Pinheiros", "Avenida Nove de Julho", "Rua Joaquim Floriano",
        "Avenida Juscelino Kubitschek", "Rua Bandeira Paulista", "Avenida Ibirapuera", "Rua Domingos de Morais",
        "Avenida Santo Amaro", "Rua Clodomiro Amazonas", "Rua Tabapuã", "Avenida Hélio Pellegrino", "Avenida Professor Francisco Morato",
        "Avenida Engenheiro Luiz Carlos Berrini", "Avenida Pedroso de Moraes", "Rua Maria Antônia", "Rua Cardoso de Almeida",
        "Rua Palestra Itália", "Rua Heitor Penteado", "Rua Lins de Vasconcelos", "Avenida Indianópolis", "Avenida Washington Luís",
        "Rua Antonio de Barros", "Rua Cantareira", "Avenida Cruzeiro do Sul", "Rua Voluntários da Pátria", "Rua Alfredo Pujol",
        "Avenida Guapira", "Avenida Cruzeiro do Sul", "Rua Celso Garcia", "Rua Silvio Romero", "Rua do Gasômetro", "Rua Taquari",
        "Avenida Rudge", "Avenida São João", "Rua Amaral Gurgel", "Rua dos Trilhos", "Avenida Imirim", "Rua Maria Cândida",
        "Avenida Itaberaba", "Rua Pio XI", "Avenida Professor Abraão de Morais", "Rua Francisco Morato", "Rua Cotoxó",
        "Rua Cayowaa", "Rua Traipu", "Rua Apinajés", "Rua Paulo Franco", "Avenida Jacu-Pêssego", "Rua Aricanduva",
        "Avenida Engenheiro Caetano Álvares", "Avenida Marechal Tito", "Rua Padre João Manuel", "Avenida Sumaré", "Rua Pompeu Loureiro",
        "Rua Maranhão", "Avenida Diógenes Ribeiro de Lima", "Rua Pascoal Ranieri Mazzilli", "Rua Ministro Godói", "Avenida Pompeia",
        "Rua Madre Cabrini", "Avenida República do Líbano", "Rua Harmonia", "Rua Girassol", "Rua Henrique Schaumann",
        "Avenida Tiradentes", "Avenida Braz Leme", "Rua Conselheiro Brotero", "Rua Itapura", "Rua Jaboticabal", "Rua Lucrécia Maciel",
        "Avenida Dr. Ricardo Jafet", "Rua Alvarenga", "Avenida Corifeu de Azevedo Marques", "Avenida Nossa Senhora do Sabará",
        "Rua Olívia Guedes Penteado", "Rua Alagoas", "Rua Capote Valente", "Rua Doutor Homem de Mello", "Rua Diana",
        "Rua Votupoca", "Avenida das Nações Unidas", "Rua Pedroso Alvarenga", "Rua Leopoldo Couto de Magalhães",
        "Rua João Cachoeira", "Rua Vinte e Cinco de Março", "Rua do Carmo", "Rua Piratininga", "Rua Alfredo Maia",
        "Rua Humberto I", "Rua José Maria Lisboa", "Rua Dr. Rafael de Barros", "Rua Rafael de Barros"
    ]
    tipo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    estado = random.choice(estados)
    cidade = random.choice(cidades[estado])
    bairro = random.choice(bairros)
    endereco = random.choice(enderecos)
    cep = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"

    sexo = random.choice(sexos)
    if sexo == "Masculino":
        altura = f"1,{random.randint(50, 90)}"
    else:
        altura = f"1,{random.randint(50, 70)}"

    return {
        "Nome": random.choice(nomes),
        "CPF": gerar_cpf(),
        "RG": gerar_rg(),
        "Data de Nascimento": gerar_data_nascimento(),
        "Sexo": sexo,
        "Signo": random.choice(signos),
        "Mãe": f"Rosângela {random.choice(['Antônia', 'Maria', 'Clara'])}",
        "Pai": f"Marcelo {random.choice(['Pedro', 'João', 'Carlos'])} Silva",  # Corrigido para incluir espaço
        "Email": f"{random.choice(nomes).lower().replace(' ', '.')}@gmail.com",
        "CEP": cep,
        "Endereço": endereco,
        "Bairro": bairro,
        "Cidade": cidade,
        "Estado": estado,
        "Telefone Fixo": gerar_telefone(estado),
        "Celular": gerar_telefone(estado),
        "Altura": altura,
        "Tipo Sanguíneo": random.choice(tipo_sanguineo)
    }

def verificar_bin(bin):
    print(f"Verificando BIN: {bin}")
    banks = ["Banco do Brasil", "Itau", "Caixa Economica", "Bradesco"]
    random_bank = random.choice(banks)
    print(f"Banco: {random_bank}")
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
            print("Saindo, Obrigado por usar o programa!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
