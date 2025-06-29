# app.py - Backend Aplikasi Perpustakaan Sederhana

# Impor modul yang diperlukan dari Flask dan SQLAlchemy
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date # Untuk menangani tanggal peminjaman/pengembalian
import os # Untuk mengelola path database

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi database SQLite
# Database akan disimpan sebagai file 'perpustakaan.db' di direktori yang sama
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'perpustakaan.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Mematikan fitur notifikasi perubahan model, tidak wajib tapi disarankan

# Inisialisasi SQLAlchemy dengan aplikasi Flask
db = SQLAlchemy(app)

# --- Definisi Model Database ---
# Model merepresentasikan tabel dalam database Anda.

class Buku(db.Model):
    # Nama tabel di database
    __tablename__ = 'buku'
    # Kolom-kolom tabel
    id_buku = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(255), nullable=False)
    pengarang = db.Column(db.String(255), nullable=False)
    penerbit = db.Column(db.String(255))
    tahun_terbit = db.Column(db.Integer)
    isbn = db.Column(db.String(20), unique=True)
    jumlah_stok = db.Column(db.Integer, nullable=False, default=0)

    # Representasi string dari objek Buku (berguna untuk debugging)
    def __repr__(self):
        return f'<Buku {self.judul}>'

    # Metode untuk mengubah objek Buku menjadi dictionary (JSON-serializable)
    def to_dict(self):
        return {
            'id_buku': self.id_buku,
            'judul': self.judul,
            'pengarang': self.pengarang,
            'penerbit': self.penerbit,
            'tahun_terbit': self.tahun_terbit,
            'isbn': self.isbn,
            'jumlah_stok': self.jumlah_stok
        }

class Anggota(db.Model):
    __tablename__ = 'anggota'
    id_anggota = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(255), nullable=False)
    alamat = db.Column(db.Text)
    telepon = db.Column(db.String(15))
    email = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return f'<Anggota {self.nama}>'

    def to_dict(self):
        return {
            'id_anggota': self.id_anggota,
            'nama': self.nama,
            'alamat': self.alamat,
            'telepon': self.telepon,
            'email': self.email
        }

class Peminjaman(db.Model):
    __tablename__ = 'peminjaman'
    id_peminjaman = db.Column(db.Integer, primary_key=True)
    id_buku = db.Column(db.Integer, db.ForeignKey('buku.id_buku'), nullable=False)
    id_anggota = db.Column(db.Integer, db.ForeignKey('anggota.id_anggota'), nullable=False)
    tanggal_pinjam = db.Column(db.Date, nullable=False, default=date.today)
    tanggal_kembali = db.Column(db.Date) # Nullable, akan diisi saat buku dikembalikan
    status = db.Column(db.String(50), default='Dipinjam') # 'Dipinjam' atau 'Dikembalikan'

    # Definisikan relasi untuk memudahkan akses data terkait
    buku = db.relationship('Buku', backref='peminjaman_buku')
    anggota = db.relationship('Anggota', backref='peminjaman_anggota')

    def __repr__(self):
        return f'<Peminjaman {self.id_peminjaman} - Buku: {self.id_buku}, Anggota: {self.id_anggota}>'

    def to_dict(self):
        return {
            'id_peminjaman': self.id_peminjaman,
            'id_buku': self.id_buku,
            'judul_buku': self.buku.judul if self.buku else None, # Ambil judul buku
            'id_anggota': self.id_anggota,
            'nama_anggota': self.anggota.nama if self.anggota else None, # Ambil nama anggota
            'tanggal_pinjam': self.tanggal_pinjam.isoformat(),
            'tanggal_kembali': self.tanggal_kembali.isoformat() if self.tanggal_kembali else None,
            'status': self.status
        }

# --- Rute API ---

# Rute utama untuk menyajikan file HTML frontend
@app.route('/')
def index():
    return render_template('index.html')

# --- API untuk Buku ---
@app.route('/api/buku', methods=['GET', 'POST'])
def kelola_buku():
    if request.method == 'GET':
        # Mengambil semua buku dari database
        buku_list = Buku.query.all()
        # Mengonversi objek Buku menjadi list of dictionaries
        return jsonify([buku.to_dict() for buku in buku_list])
    elif request.method == 'POST':
        # Menambah buku baru
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data tidak ditemukan dalam request.'}), 400

        # Validasi input minimal
        if not data.get('judul') or not data.get('pengarang'):
            return jsonify({'message': 'Judul dan pengarang wajib diisi.'}), 400

        try:
            # Membuat objek Buku baru dan mengisinya dengan data
            new_buku = Buku(
                judul=data['judul'],
                pengarang=data['pengarang'],
                penerbit=data.get('penerbit'),
                tahun_terbit=data.get('tahun_terbit'),
                isbn=data.get('isbn'),
                jumlah_stok=data.get('jumlah_stok', 0) # Default 0 jika tidak disediakan
            )
            db.session.add(new_buku) # Menambahkan ke sesi database
            db.session.commit() # Menyimpan perubahan ke database
            return jsonify({'message': 'Buku berhasil ditambahkan!', 'buku': new_buku.to_dict()}), 201
        except Exception as e:
            db.session.rollback() # Mengembalikan transaksi jika ada error
            return jsonify({'message': f'Gagal menambahkan buku: {str(e)}'}), 500

@app.route('/api/buku/<int:id_buku>', methods=['GET', 'PUT', 'DELETE'])
def detail_buku(id_buku):
    # Mencari buku berdasarkan ID
    buku = Buku.query.get_or_404(id_buku)

    if request.method == 'GET':
        # Mengambil detail buku tunggal
        return jsonify(buku.to_dict())
    elif request.method == 'PUT':
        # Mengupdate data buku
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data tidak ditemukan dalam request.'}), 400

        try:
            # Update atribut buku dengan data baru
            buku.judul = data.get('judul', buku.judul)
            buku.pengarang = data.get('pengarang', buku.pengarang)
            buku.penerbit = data.get('penerbit', buku.penerbit)
            buku.tahun_terbit = data.get('tahun_terbit', buku.tahun_terbit)
            buku.isbn = data.get('isbn', buku.isbn)
            buku.jumlah_stok = data.get('jumlah_stok', buku.jumlah_stok)
            db.session.commit()
            return jsonify({'message': 'Buku berhasil diupdate!', 'buku': buku.to_dict()})
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Gagal mengupdate buku: {str(e)}'}), 500
    elif request.method == 'DELETE':
        # Menghapus buku
        try:
            db.session.delete(buku)
            db.session.commit()
            return jsonify({'message': 'Buku berhasil dihapus!'}), 204 # 204 No Content
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Gagal menghapus buku: {str(e)}'}), 500

# --- API untuk Anggota ---
@app.route('/api/anggota', methods=['GET', 'POST'])
def kelola_anggota():
    if request.method == 'GET':
        anggota_list = Anggota.query.all()
        return jsonify([anggota.to_dict() for anggota in anggota_list])
    elif request.method == 'POST':
        data = request.get_json()
        if not data or not data.get('nama'):
            return jsonify({'message': 'Nama anggota wajib diisi.'}), 400
        try:
            new_anggota = Anggota(
                nama=data['nama'],
                alamat=data.get('alamat'),
                telepon=data.get('telepon'),
                email=data.get('email')
            )
            db.session.add(new_anggota)
            db.session.commit()
            return jsonify({'message': 'Anggota berhasil ditambahkan!', 'anggota': new_anggota.to_dict()}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Gagal menambahkan anggota: {str(e)}'}), 500

@app.route('/api/anggota/<int:id_anggota>', methods=['GET', 'PUT', 'DELETE'])
def detail_anggota(id_anggota):
    anggota = Anggota.query.get_or_404(id_anggota)
    if request.method == 'GET':
        return jsonify(anggota.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data tidak ditemukan dalam request.'}), 400
        try:
            anggota.nama = data.get('nama', anggota.nama)
            anggota.alamat = data.get('alamat', anggota.alamat)
            anggota.telepon = data.get('telepon', anggota.telepon)
            anggota.email = data.get('email', anggota.email)
            db.session.commit()
            return jsonify({'message': 'Anggota berhasil diupdate!', 'anggota': anggota.to_dict()})
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Gagal mengupdate anggota: {str(e)}'}), 500
    elif request.method == 'DELETE':
        try:
            db.session.delete(anggota)
            db.session.commit()
            return jsonify({'message': 'Anggota berhasil dihapus!'}), 204
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Gagal menghapus anggota: {str(e)}'}), 500

# --- API untuk Peminjaman ---
@app.route('/api/peminjaman', methods=['GET', 'POST'])
def kelola_peminjaman():
    if request.method == 'GET':
        peminjaman_list = Peminjaman.query.all()
        return jsonify([peminjaman.to_dict() for peminjaman in peminjaman_list])
    elif request.method == 'POST':
        data = request.get_json()
        if not data or not data.get('id_buku') or not data.get('id_anggota'):
            return jsonify({'message': 'ID Buku dan ID Anggota wajib diisi untuk peminjaman.'}), 400

        id_buku = data['id_buku']
        id_anggota = data['id_anggota']

        buku = Buku.query.get(id_buku)
        anggota = Anggota.query.get(id_anggota)

        if not buku:
            return jsonify({'message': 'Buku tidak ditemukan.'}), 404
        if not anggota:
            return jsonify({'message': 'Anggota tidak ditemukan.'}), 404
        if buku.jumlah_stok <= 0:
            return jsonify({'message': 'Stok buku tidak tersedia untuk dipinjam.'}), 400

        try:
            # Kurangi stok buku
            buku.jumlah_stok -= 1
            # Catat peminjaman
            new_peminjaman = Peminjaman(
                id_buku=id_buku,
                id_anggota=id_anggota,
                tanggal_pinjam=date.today(), # Tanggal peminjaman otomatis hari ini
                status='Dipinjam'
            )
            db.session.add(new_peminjaman)
            db.session.commit()
            return jsonify({'message': 'Buku berhasil dipinjam!', 'peminjaman': new_peminjaman.to_dict()}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Gagal mencatat peminjaman: {str(e)}'}), 500

@app.route('/api/peminjaman/<int:id_peminjaman>/kembali', methods=['PUT'])
def kembalikan_buku(id_peminjaman):
    # Mencari transaksi peminjaman berdasarkan ID
    peminjaman = Peminjaman.query.get_or_404(id_peminjaman)

    if peminjaman.status == 'Dikembalikan':
        return jsonify({'message': 'Buku ini sudah dikembalikan sebelumnya.'}), 400

    try:
        # Update status peminjaman menjadi 'Dikembalikan'
        peminjaman.tanggal_kembali = date.today() # Tanggal kembali otomatis hari ini
        peminjaman.status = 'Dikembalikan'

        # Tambah kembali stok buku yang dikembalikan
        buku = Buku.query.get(peminjaman.id_buku)
        if buku:
            buku.jumlah_stok += 1
        
        db.session.commit()
        return jsonify({'message': 'Buku berhasil dikembalikan!', 'peminjaman': peminjaman.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Gagal mengembalikan buku: {str(e)}'}), 500

# Fungsi untuk membuat tabel database sebelum aplikasi berjalan
# Ini harus dijalankan sekali saat aplikasi pertama kali di-deploy atau dijalankan
with app.app_context():
    db.create_all()

# Jalankan aplikasi jika script ini dieksekusi secara langsung
if __name__ == '__main__':
    # Debug mode akan memberikan informasi error lebih detail
    # Host '0.0.0.0' agar bisa diakses dari luar (misal: jika di-deploy di Docker)
    app.run(debug=True, host='0.0.0.0', port=5000)
