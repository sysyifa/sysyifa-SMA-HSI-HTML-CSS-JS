from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def Halaman_utama():
    return  render_template ('index.html')

@app.route("/Profil")
def Halaman_profil():
    return render_template ('profil.html')

if __name__ == '__main__':
    app.run (debug=True)