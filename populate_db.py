# populate_db.py - Skrip untuk mengisi database SQLite dengan data contoh

# Impor objek db dan model dari app.py
# Pastikan app.py berada di direktori yang sama
from app import app, db, Buku, Anggota, Peminjaman
from datetime import date, timedelta # Untuk tanggal

# Gunakan app context agar operasi database bisa berjalan
with app.app_context():
    # --- Opsional: Hapus semua tabel jika ingin mulai dari awal ---
    # Ini akan menghapus semua data yang ada! Gunakan dengan hati-hati.
    print("Menghapus tabel yang sudah ada (jika ada)...")
    db.drop_all()

    # --- Buat ulang semua tabel ---
    # Ini penting jika Anda menghapus tabel di atas atau jika database belum pernah dibuat
    print("Membuat ulang tabel database...")
    db.create_all()
    print("Tabel database berhasil dibuat.")

    # --- Menambahkan Data Contoh ke Tabel Buku ---
    print("\nMenambahkan data buku...")
    buku1 = Buku(judul="Filosofi Teras", pengarang="Henry Manampiring", penerbit="Kompas", tahun_terbit=2018, isbn="978-602-412-518-9", jumlah_stok=5)
    buku2 = Buku(judul="Atomic Habits", pengarang="James Clear", penerbit="Gramedia Pustaka Utama", tahun_terbit=2019, isbn="978-602-06-3316-5", jumlah_stok=3)
    buku3 = Buku(judul="Sapiens: A Brief History of Humankind", pengarang="Yuval Noah Harari", penerbit="Kepustakaan Populer Gramedia", tahun_terbit=2017, isbn="978-602-424-648-8", jumlah_stok=2)
    buku4 = Buku(judul="Bumi Manusia", pengarang="Pramoedya Ananta Toer", penerbit="Hasta Mitra", tahun_terbit=1980, isbn="978-979-99450-0-1", jumlah_stok=4)

    db.session.add_all([buku1, buku2, buku3, buku4])
    db.session.commit() # Simpan buku-buku ini terlebih dahulu agar memiliki ID

    print("Data buku berhasil ditambahkan.")

    # --- Menambahkan Data Contoh ke Tabel Anggota ---
    print("\nMenambahkan data anggota...")
    anggota1 = Anggota(nama="Andi Wijaya", alamat="Jl. Merdeka No. 10", telepon="081234567890", email="andi@example.com")
    anggota2 = Anggota(nama="Budi Santoso", alamat="Jl. Raya Indah No. 25", telepon="085678901234", email="budi@example.com")
    anggota3 = Anggota(nama="Citra Dewi", alamat="Perumahan Elok Blok C3", telepon="087812345678", email="citra@example.com")

    db.session.add_all([anggota1, anggota2, anggota3])
    db.session.commit() # Simpan anggota-anggota ini agar memiliki ID

    print("Data anggota berhasil ditambahkan.")

    # --- Menambahkan Data Contoh ke Tabel Peminjaman ---
    print("\nMenambahkan data peminjaman...")
    # Peminjaman aktif
    peminjaman1 = Peminjaman(id_buku=buku1.id_buku, id_anggota=anggota1.id_anggota, tanggal_pinjam=date.today() - timedelta(days=7), status='Dipinjam')
    peminjaman2 = Peminjaman(id_buku=buku2.id_buku, id_anggota=anggota2.id_anggota, tanggal_pinjam=date.today() - timedelta(days=3), status='Dipinjam')

    # Peminjaman yang sudah dikembalikan
    peminjaman3 = Peminjaman(id_buku=buku4.id_buku, id_anggota=anggota1.id_anggota, tanggal_pinjam=date.today() - timedelta(days=15), tanggal_kembali=date.today() - timedelta(days=10), status='Dikembalikan')

    db.session.add_all([peminjaman1, peminjaman2, peminjaman3])
    db.session.commit()

    print("Data peminjaman berhasil ditambahkan.")
    print("\nDatabase 'perpustakaan.db' berhasil diisi dengan data contoh!")

