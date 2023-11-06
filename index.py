#Flask -> Framework para desenvolvimento de sites e APIs usando python
from flask import Flask, render_template


#Criação do site(VAZIO)
app = Flask(__name__)


#Criar primeira página do site
#route -> O link que a página irá ficar
#função -> o que você quer exibir naquela página


@app.route("/")#Decorator -> Atribui uma nova funcionalidade para função seguinte(ao invés de printar, exibirá a msg na página)
def homepage():
    #O que ele retorna é apresentado na página
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)

#Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) 