import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Obtendo a chave secreta das variáveis de ambiente
import secrets
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
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

        # Processar os dados com base no método de pagamento
        print(f'Produto URL: {product_url}')
        print(f'Nome: {name}, E-mail: {email}, País: {country}, Estado: {state}, Cidade: {city}, Município: {municipality}, Residência: {residence}')
        
        if payment_method == 'cartao':
            print(f'Compra com cartão: {card_number}, Senha: {card_password}')
        elif payment_method == 'pix':
            print(f'Compra via Pix: {pix_key}')
        elif payment_method == 'boleto':
            print(f'Boleto gerado: {boleto}')
        
        return redirect('/')
    return render_template('purchase_form.html')

if __name__ == '__main__':
    app.run(debug=True)