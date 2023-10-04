from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def indice():
    return render_template ("index.html")

@app.route("/login",methods=['GET','POST']) 
def login():
    if request.method == 'GET':
      return render_template('login.html')

    if request.method == 'POST':
        return redirect('/')

@app.route("/cadastro")
def cadastro():
    return render_template ("cadastro.html")

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000)

