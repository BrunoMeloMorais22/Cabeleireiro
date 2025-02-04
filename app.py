import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

avaliacoes = []

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', avaliacoes=avaliacoes)

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

@app.route('/avaliacao', methods=["GET", "POST"])
def avaliacao():
    if request.method == "POST":
        nome = request.form.get('nome')
        comentario = request.form.get('comentario')
        status = request.form.get('gostou_naogostou')

        if 'imagem' not in request.files:
            return "Nenhum arquivo enviado."

        file = request.files['imagem']

        if file.filename == '':
            return "Nenhuma imagem selecionada."

        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

        avaliacoes.append({
            "imagem": filepath,
            "nome": nome,
            "comentario": comentario,
            "status": status
        })

        return redirect(url_for('index'))
    return render_template('avaliacao.html')

if __name__ == "__main__":
    app.run(debug=True)