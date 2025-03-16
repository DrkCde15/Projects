from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Conexão com o banco de dados MySQL
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="loja_fantasma"
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Coleta de dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        localizacao = request.form['localizacao']
        rua = request.form['rua']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        pais = request.form['pais']
        metodo_pagamento = request.form['metodo_pagamento']
        chave_pix = request.form.get('chave_pix')
        numero_cartao = request.form.get('numero_cartao')
        validade_cartao = request.form.get('validade_cartao')
        cvv_cartao = request.form.get('cvv_cartao')

        # Conectar ao banco de dados
        db = conectar_banco()
        cursor = db.cursor()

        # Inserir dados no banco
        cursor.execute("""
            INSERT INTO usuarios (nome, email, cpf, localizacao, rua, bairro, cidade, estado, pais, metodo_pagamento, chave_pix)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nome, email, cpf, localizacao, rua, bairro, cidade, estado, pais, metodo_pagamento, chave_pix))

        db.commit()  # Confirmar inserção no banco
        cursor.close()
        db.close()

        return 'Cadastro realizado com sucesso!'
    
    return render_template('cadastro.html')

@app.route('/produtos')
def produtos():
    # Aqui você pode adicionar código para buscar os produtos do banco, por exemplo:
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)