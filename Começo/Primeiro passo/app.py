from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome_responsavel = request.form['nome_responsavel']
        cpf_responsavel = request.form['cpf_responsavel']
        telefone = request.form['telefone']
        email = request.form['email']
        endereco = request.form['endereco']
        nome_crianca = request.form['nome_crianca']
        escola = request.form['escola']
        data_vencimento = request.form['data_vencimento']

        print(f'{nome_responsavel}, {cpf_responsavel}, {telefone}, {email}, {endereco}, {nome_crianca}, {escola}, {data_vencimento}')
        return render_template('cadastro.html', sucesso=True)

    return render_template('cadastro.html', sucesso=False)

if __name__ == '__main__':
    app.run(debug=True)
