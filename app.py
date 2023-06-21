from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/salary/', methods=['GET', 'POST'])
def salary():
    if request.method == 'POST':
        nama = request.form['nama']
        divisi = request.form['divisi']
        lembur = int(request.form['lembur'])
        return render_template('hasil.html', nama=nama, divisi=divisi, lembur=lembur)
    else:
        return render_template('salary.html')


@app.route('/hitung_gaji/', methods=['POST'])
def hitung_gaji():
    nama = request.form['nama']
    divisi = request.form['divisi']
    lembur = int(request.form['lembur'])

    gaji_pokok = 5000000
    tunjangan = get_tunjangan(divisi)
    total_gaji = hitung_total_gaji(gaji_pokok, tunjangan, lembur)

    return render_template('hasil.html', nama=nama, divisi=divisi, gaji=total_gaji)



def get_tunjangan(divisi):
    tunjangan_dict = {
        'Marketing': 1000000,  # Marketing
        'IT': 800000,   # Developer
        'Lapangan': 600000    # Lapangan
    }
    return tunjangan_dict.get(divisi, 0)

def hitung_total_gaji(gaji_pokok, tunjangan, lembur):
    return gaji_pokok + tunjangan + (lembur * 50000)

if __name__ == '__main__':
    app.run(debug=True)
