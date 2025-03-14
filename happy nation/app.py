import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Obtendo a chave secreta das variáveis de ambiente
import secrets
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
        payment_method = request.form['payment_method']
        name = request.form['name']
        email = request.form['email']
        location = request.form['location']
        card_number = request.form.get('card_number')
        card_password = request.form.get('card_password')
        pix_key = request.form.get('pix_key')
        boleto = request.form.get('boleto')
        
        # Processar os dados com base no método de pagamento
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