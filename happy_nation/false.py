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
    # Listas de nomes masculinos e femininos
    nomes_masculinos = ["João Silva", "Carlos Souza", "Lucas Almeida", "Paulo Sérgio Costa", "Gustavo Fernandes", 
    "Felipe Duarte", "Pedro Gonçalves", "José Barbosa", "Thiago Matos", "Daniel Moreira", 
    "Vinicius Alves", "Matheus Ribeiro", "Henrique Teixeira", "Rodrigo Costa", "Eduardo Lima", 
    "Rafael Pereira", "André Silva", "Diego Mendes", "Gabriel Alves", "Bruno Oliveira", 
    "Leonardo Azevedo", "Marcelo Almeida", "Antonio Melo", "Miguel Santana", "Guilherme Ferreira", 
    "Caio Souza", "Ruan Ribeiro", "Arthur Rocha", "Junior Santos", "Heitor Martins", "Vitor Lima", 
    "Igor Alves", "Hugo Fernandes", "Otávio Ribeiro", "Leandro Batista", "Pablo Matos", "Fábio Gomes", 
    "Robson Lima", "Patrick Oliveira", "Diogo Gonçalves", "Roberto Santos", "Alan Nunes", "Wagner Almeida", 
    "Otávio Nunes", "Samuel Silva", "Enzo Costa", "Filipe Cardoso", "Victor Araújo", "Murilo Santos", 
    "Danilo Costa", "Alexandre Martins", "Cláudio Rocha", "Francisco Pereira", "Ricardo Teixeira", 
    "Fabiano Oliveira", "Leandro Nunes", "Douglas Lima", "Marcos Silva", "Eduardo Rocha", "Alex Silva", 
    "Lucas Teixeira", "Thiago Almeida", "Gustavo Costa", "Vinícius Ribeiro", "Guilherme Santos", 
    "Robson Rocha", "Felipe Souza", "Afonso Martins", "William Almeida", "Daniela Costa", "Marcelo Santos", 
    "Fernando Azevedo", "Arthur Teixeira", "Tiago Lima", "Renato Ribeiro", "Claudio Fernandes", "Lucas Mendes", 
    "Gabriel Cardoso", "Victor Pereira", "Maurício Silva", "Vítor Souza", "Carlos Martins", "André Barbosa", 
    "Felipe Nunes", "Mateus Souza", "David Lima", "Thiago Ribeiro", "Pedro Martins", "Leandro Souza", 
    "Vanderlei Silva", "Wagner Santos", "Paulo Azevedo", "Hugo Almeida", "Luiz Costa", "Alexandre Azevedo", 
    "Ricardo Barbosa", "Fábio Ribeiro", "Vinicius Nunes", "Carlos Azevedo", "Thiago Gomes", "Davi Lima", 
    "Roberto Silva", "Pablo Costa", "Samuel Pereira", "Rafael Nunes", "Renato Santos", "André Costa", 
    "Eduardo Ribeiro", "Marcelo Lima", "Bruno Azevedo", "Diego Teixeira", "Maurício Costa", "Gustavo Almeida", 
    "Ricardo Silva", "Vítor Ribeiro", "Marcelo Nunes", "Alan Rocha", "Robson Ribeiro", "Victor Nunes", 
    "Hugo Costa", "Marcos Ribeiro", "Vinicius Gomes", "Afonso Silva", "Felipe Pereira", "Leonardo Ribeiro", 
    "Carlos Souza", "Júlio Teixeira", "Gabriel Rocha", "Arthur Silva", "Felipe Gomes", "Paulo Ribeiro", 
    "Rafael Costa", "Tiago Santos", "Alex Ribeiro", "Bruno Mendes", "Carlos Teixeira", "Vítor Gomes", 
    "Samuel Nunes", "Leandro Pereira", "Lucas Gomes", "Danilo Ribeiro", "Felipe Fernandes", "Ricardo Lima", 
    "Pedro Souza", "Gilberto Nunes", "Douglas Ribeiro", "Mateus Ribeiro", "Rafael Gomes", "Alan Santos"
]
    
    nomes_femininos = ["Rosa Pietra Sophia Fogaca", "Maria Oliveira", "Ana Beatriz Martins", 
        "Fernanda Pereira", "Mariana Gonçalves", "Clara Mendes", "Isabella Ribeiro", "Camila Araújo", "Sofia Carvalho", "Laura Nunes",
        "Gabriela Rocha", "Julia Ferreira", "Lara Santos", "Luana Souza", "Livia Andrade", "Yasmin Almeida", "Alice Martins",
        "Helena Correia", "Sophia Machado", "Valentina Barbosa", "Carolina Rocha", "Beatriz Nunes", "Cecilia Fernandes", "Clara Gomes",
        "Lorena Vieira", "Renata Cardoso", "Marina Moreira", "Amanda Costa", "Flávia Silva", "Elisa Nunes", "Nicole Ferreira",
        "Rafaela Mendes", "Marcia Souza", "Tainá Araújo", "Letícia Pereira", "Joana Andrade", "Aline Duarte", "Cristina Nogueira", "Larissa Teixeira",
        "Emilly Carvalho", "Daniela Souza", "Bruna Martins", "Sandra Costa", "Mirela Ferreira",
        "Lorraine Vieira", "Isabel Fernandes", "Melina Rocha",
        "Stephanie Souza", "Clarice Matos", "Geovana Pereira", "Eduarda Alves",
        "Jéssica Almeida", "Bianca Ribeiro", "Marcela Souza", "Sara Martins",
        "Amanda Gonçalves", "Manuela Lima", "Raquel Mendes", "Lívia Fernandes"]

    # Escolher aleatoriamente entre masculino e feminino
    sexo = random.choice(["Masculino", "Feminino"])
    
    # Escolher um nome correspondente ao sexo
    if sexo == "Masculino":
        nome = random.choice(nomes_masculinos)
    else:
        nome = random.choice(nomes_femininos)

    # Gerar email a partir do nome
    email = nome.lower().replace(' ', '.') + "@gmail.com"

    # Outros dados
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
    bairros = [ "Centro", "Jardim das Flores", "Vila Nova", "Maria Rachel", "Jardim América", "Vila Mariana", "Bela Vista",
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
        "Jardim Aricanduva", "Parque São Jorge", "Jardim Morumbi", "Chácara Flora", "Vila Ipojuca", "Jardim Olinda"]
    
    enderecos = ["Rua João Patrício de Lima", "Avenida Paulista", "Rua das Flores", "Praça da Sé", "Rua Augusta", "Rua Oscar Freire",
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
        "Rua Humberto I", "Rua José Maria Lisboa", "Rua Dr. Rafael de Barros", "Rua Rafael de Barros"]
    
    tipo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    estado = random.choice(estados)
    cidade = random.choice(cidades[estado])
    bairro = random.choice(bairros)
    endereco = random.choice(enderecos)
    cep = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"

    return {
        "nome": nome,
        "cpf": gerar_cpf(),
        "rg": gerar_rg(),
        "data_nasc": gerar_data_nascimento(),
        "sexo": sexo,
        "signo": random.choice(signos),
        "mae": f"Josefa {random.choice(['Antônia', 'Maria', 'Clara'])}",
        "pai": f"Marcelo {random.choice(['Pedro', 'João', 'Carlos'])} Silva",
        "email": email,
        "cep": cep,
        "endereço": endereco,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "telefone_fixo": gerar_telefone(estado),
        "celular": gerar_telefone(estado),
        "altura": f"1,{random.randint(50, 80)}",
        "tipo_sanguíneo": random.choice(tipo_sanguineo)
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
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()