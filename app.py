import os
import cloudinary
from cloudinary.exceptions import Error as CloudinaryError
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)


cloudinary.config( 
  cloud_name = os.getenv("CLOUND_NAME"), 
  api_key = os.getenv("API_KEY"), 
  api_secret = os.getenv("API_SECRET") 
)

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
        telefone = request.form.get('telefone') 
        return redirect(url_for('reserva_sucesso', nome=nome, email=email, telefone=telefone))
    return render_template('reserva.html')

@app.route('/reserva_sucesso')
def reserva_sucesso():
    nome = request.args.get('nome')
    email = request.args.get('email')
    telefone = request.args.get('telefone')
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
            try:
    
                upload_result = cloudinary.uploader.upload(file)
                imagem_url = upload_result['secure_url']

                avaliacoes.append({
                    "imagem": imagem_url,
                    "nome": nome,
                    "comentario": comentario,
                    "status": status
                })

                return redirect(url_for('index'))
            except CloudinaryError as e:
                return f"Erro ao fazer upload da imagem: {e}"

        return "Formato de arquivo não permitido."
    
    return render_template('avaliacao.html')

if __name__ == "__main__":
    app.run(debug=True)
