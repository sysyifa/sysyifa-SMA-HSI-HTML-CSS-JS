from flask import Flask, render_template, request

app = Flask(__name__)

semua_pesan = []

@app.route('/tamubuku', methods=['GET', 'POST'])
def tamu_buku():
    global semua_pesan

    if request.method == 'POST':
        nama = request.form.get('nama')
        pesan = request.form.get('pesan')

        data_pesan = {'nama': nama, 'pesan': pesan}
        semua_pesan.append(data_pesan)

    return render_template('tamubuku.html', semua_pesan=semua_pesan)


# Tambahan biar kalau buka root "/" gak not found
@app.route('/')
def home():
    return '<h2>Halaman Utama</h2><p>Klik <a href="/tamubuku">di sini</a> untuk buka buku tamu.</p>'


if __name__ == '__main__':
    app.run(debug=True)
