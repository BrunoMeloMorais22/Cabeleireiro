from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/perfil', methods=["GET", "POST"])
def perfil():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        return redirect(url_for('index02', nome=nome, email=email))
    return render_template('perfil.html')

@app.route('/index02')
def index02():
    nome = request.args.get('nome')
    email = request.args.get('email')
    return render_template('index02.html', nome=nome, email=email)

@app.route('/reserva', methods=["GET", "POST"])
def reserva():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefnoe')
        return redirect(url_for('reserva_sucesso', nome=nome, email=email, telefone=telefone))
    return render_template('reserva.html')

@app.route('/reserva_sucesso')
def reserva_sucesso():
    nome = request.args.get('nome')
    email = request.args.get('email')
    telefone = request.args.get('telefnoe')
    return render_template('reserva_sucesso.html', nome=nome, email=email, telefone=telefone)

if __name__ == "__main__":
    app.run(debug=True)