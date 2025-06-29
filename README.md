Sistem Manajemen Perpustakaan Sederhana
Proyek ini adalah implementasi sistem manajemen data perpustakaan sederhana yang dibangun menggunakan Python Flask sebagai backend dan HTML/CSS/JavaScript sebagai frontend, dengan SQLite sebagai sistem manajemen basis datanya.

Fitur Aplikasi
• Manajemen Buku:
o Menambahkan buku baru (Judul, Pengarang, Penerbit, Tahun Terbit, ISBN, Jumlah Stok).
o Melihat daftar semua buku yang tersedia beserta stoknya.
o (Fitur Edit dan Hapus Buku tersedia secara fungsional di backend API, namun tombol di UI frontend belum sepenuhnya diimplementasikan sebagai modal form).
• Manajemen Anggota:
o Menambahkan anggota baru (Nama, Alamat, Telepon, Email).
o Melihat daftar semua anggota perpustakaan.
o (Fitur Edit dan Hapus Anggota tersedia secara fungsional di backend API, namun tombol di UI frontend belum sepenuhnya diimplementasikan sebagai modal form).
• Manajemen Peminjaman:
o Mencatat transaksi peminjaman buku oleh anggota.
o Melihat daftar peminjaman aktif.
o Mencatat pengembalian buku (mengubah status peminjaman dan menambah stok buku).
Teknologi yang Digunakan
• Backend:
o Python 3: Bahasa pemrograman utama.
o Flask: Framework web mikro untuk membangun API backend.
o Flask-SQLAlchemy: Ekstensi Flask untuk integrasi dengan SQLAlchemy ORM, mempermudah interaksi dengan database.
o SQLite: Sistem manajemen basis data ringan dan serverless, cocok untuk proyek kecil dan pengembangan. Database disimpan dalam file perpustakaan.db.
• Frontend:
o HTML5: Struktur dasar halaman web.
o CSS3 (Tailwind CSS): Styling dan desain antarmuka pengguna.
o JavaScript: Logika interaktif untuk memanggil API backend dan memperbarui UI.
Persyaratan Sistem
Sebelum menjalankan aplikasi ini, pastikan Anda memiliki perangkat lunak berikut terinstal di komputer Anda:
• Python 3.x (disarankan Python 3.8 atau lebih tinggi)
• pip (Package Installer for Python) - biasanya sudah terinstal bersama Python.
• Git (opsional, jika Anda ingin mengkloning repositori ini atau mengunggah ke GitHub)
=======

Fitur Aplikasi
Manajemen Buku:

Menambahkan buku baru (Judul, Pengarang, Penerbit, Tahun Terbit, ISBN, Jumlah Stok).

Melihat daftar semua buku yang tersedia beserta stoknya.

(Fitur Edit dan Hapus Buku tersedia secara fungsional di backend API, namun tombol di UI frontend belum sepenuhnya diimplementasikan sebagai modal form).

Manajemen Anggota:

Menambahkan anggota baru (Nama, Alamat, Telepon, Email).

Melihat daftar semua anggota perpustakaan.

(Fitur Edit dan Hapus Anggota tersedia secara fungsional di backend API, namun tombol di UI frontend belum sepenuhnya diimplementasikan sebagai modal form).

Manajemen Peminjaman:

Mencatat transaksi peminjaman buku oleh anggota.

Melihat daftar peminjaman aktif.

Mencatat pengembalian buku (mengubah status peminjaman dan menambah stok buku).

Teknologi yang Digunakan
Backend:

Python 3: Bahasa pemrograman utama.

Flask: Framework web mikro untuk membangun API backend.

Flask-SQLAlchemy: Ekstensi Flask untuk integrasi dengan SQLAlchemy ORM, mempermudah interaksi dengan database.

SQLite: Sistem manajemen basis data ringan dan serverless, cocok untuk proyek kecil dan pengembangan. Database disimpan dalam file perpustakaan.db.

Frontend:

HTML5: Struktur dasar halaman web.

CSS3 (Tailwind CSS): Styling dan desain antarmuka pengguna.

JavaScript: Logika interaktif untuk memanggil API backend dan memperbarui UI.

Persyaratan Sistem
Sebelum menjalankan aplikasi ini, pastikan Anda memiliki perangkat lunak berikut terinstal di komputer Anda:

Python 3.x (disarankan Python 3.8 atau lebih tinggi)

pip (Package Installer for Python) - biasanya sudah terinstal bersama Python.

Git (opsional, jika Anda ingin mengkloning repositori ini atau mengunggah ke GitHub)

Cara Instalasi dan Menjalankan Aplikasi
Ikuti langkah-langkah di bawah ini untuk menyiapkan dan menjalankan aplikasi di lingkungan lokal Anda:

1. Kloning Repositori (Jika dari GitHub)

   # Jika Anda mengambil proyek ini dari GitHub, kloning repositori:

   Jika Anda mengambil proyek ini dari GitHub, kloning repositori:

```
git clone https://github.com/NamaUserAnda/NamaRepoProyekAnda.git
cd NamaRepoProyekAnda
```

(Ganti NamaUserAnda/NamaRepoProyekAnda dengan detail repositori Anda)
<<<<<<< HEAD
Jika Anda hanya memiliki file-nya secara lokal, navigasikan langsung ke folder proyek:

```
cd path/ke/folder/proyek/anda
```

(Ganti path/ke/folder/proyek/anda dengan jalur direktori tempat Anda menyimpan file-file proyek ini di komputer Anda. Contoh: cd C:\Users\Pengguna\Documents\aplikasi_perpustakaan) 2. Instal Dependensi Python
Instal semua pustaka Python yang diperlukan dari file requirements.txt:

```
pip install -r requirements.txt
```

3. Inisialisasi dan Isi Database (Opsional, tapi Direkomendasikan)
   Untuk mengisi database dengan data contoh agar Anda tidak mulai dari nol, jalankan skrip populate_db.py. PENTING: Pastikan server Flask (app.py) TIDAK sedang berjalan saat Anda menjalankan skrip ini.

```
python populate_db.py
```

Skrip ini akan membuat file perpustakaan.db jika belum ada, membuat tabel, dan mengisi beberapa data contoh buku, anggota, dan peminjaman. 4. Jalankan Server Backend (Flask)
Setelah dependensi terinstal dan database diinisialisasi (jika Anda memilih untuk melakukannya), Anda bisa menjalankan server Flask.

```
python app.py
```

Anda akan melihat output di terminal yang menunjukkan server berjalan, biasanya di http://127.0.0.1:5000/. Biarkan jendela terminal ini tetap terbuka. 5. Akses Aplikasi Frontend
Buka browser web favorit Anda (seperti Chrome, Firefox, Edge) dan masukkan alamat berikut di bilah URL:

```
http://127.0.0.1:5000/
```

Aplikasi Sistem Manajemen Perpustakaan akan muncul di browser Anda.
Struktur Proyek

```
=======

Jika Anda hanya memiliki file-nya secara lokal, navigasikan langsung ke folder proyek:

cd C:\Users\andib\Downloads\Data Andi\sibermu\Semester 2\Pengembangan Aplikasi Basis Data\tugas_akhir

2. Instal Dependensi Python
Instal semua pustaka Python yang diperlukan dari file requirements.txt:

pip install -r requirements.txt

3. Inisialisasi dan Isi Database (Opsional, tapi Direkomendasikan)
Untuk mengisi database dengan data contoh agar Anda tidak mulai dari nol, jalankan skrip populate_db.py.
PENTING: Pastikan server Flask (app.py) TIDAK sedang berjalan saat Anda menjalankan skrip ini.

python populate_db.py

Skrip ini akan membuat file perpustakaan.db jika belum ada, membuat tabel, dan mengisi beberapa data contoh buku, anggota, dan peminjaman.

4. Jalankan Server Backend (Flask)
Setelah dependensi terinstal dan database diinisialisasi (jika Anda memilih untuk melakukannya), Anda bisa menjalankan server Flask.

python app.py

Anda akan melihat output di terminal yang menunjukkan server berjalan, biasanya di http://127.0.0.1:5000/. Biarkan jendela terminal ini tetap terbuka.

5. Akses Aplikasi Frontend
Buka browser web favorit Anda (seperti Chrome, Firefox, Edge) dan masukkan alamat berikut di bilah URL:

http://127.0.0.1:5000/

Aplikasi Sistem Manajemen Perpustakaan akan muncul di browser Anda.

Struktur Proyek
>>>>>>> 88748b48c06f0596b82e041c6068e76fc3a35ed6
.
├── app.py                  # Backend aplikasi Flask dan definisi model database
├── index.html              # Frontend aplikasi web (HTML, CSS, JavaScript)
├── populate_db.py          # Skrip opsional untuk mengisi database dengan data contoh
├── requirements.txt        # Daftar pustaka Python yang dibutuhkan
└── templates/              # Folder untuk file HTML (wajib oleh Flask)
    └── index.html          # Frontend aplikasi web (dipindahkan ke sini)
<<<<<<< HEAD
```

Penjelasan Singkat Fungsi
• app.py: Ini adalah "otak" aplikasi. Ia mendefinisikan model untuk Buku, Anggota, dan Peminjaman yang berhubungan langsung dengan tabel di database SQLite. File ini juga menyediakan API (Application Programming Interface) yang memungkinkan frontend berkomunikasi dengannya untuk menambah, melihat, mengedit, dan menghapus data (operasi CRUD).
• index.html: Ini adalah antarmuka pengguna grafis (GUI) yang Anda lihat di browser. Menggunakan HTML untuk struktur, Tailwind CSS untuk tampilan visual yang menarik, dan JavaScript untuk interaktivitas. JavaScript di sini bertugas memanggil API yang ada di app.py untuk mengambil atau mengirim data.
• populate_db.py: Skrip ini bersifat utilitas. Gunakan ini sekali di awal untuk menyiapkan database kosong atau untuk mengisi database dengan beberapa data dummy, mempermudah pengujian dan demonstrasi.
• requirements.txt: Daftar semua pustaka Python eksternal yang dibutuhkan proyek ini (misalnya Flask, Flask-SQLAlchemy) beserta versi spesifiknya. Memastikan lingkungan pengembangan yang konsisten.
• perpustakaan.db: File ini adalah database SQLite Anda. Ia akan dibuat secara otomatis saat app.py atau populate_db.py pertama kali dijalankan. Semua data buku, anggota, dan peminjaman Anda akan disimpan di sini.
• templates/: Folder ini adalah konvensi Flask. Flask mencari file HTML yang akan ditampilkan (render_template) di dalam folder ini.
=======

Penjelasan Singkat Fungsi
app.py: Ini adalah "otak" aplikasi. Ia mendefinisikan model untuk Buku, Anggota, dan Peminjaman yang berhubungan langsung dengan tabel di database SQLite. File ini juga menyediakan API (Application Programming Interface) yang memungkinkan frontend berkomunikasi dengannya untuk menambah, melihat, mengedit, dan menghapus data (operasi CRUD).

index.html: Ini adalah antarmuka pengguna grafis (GUI) yang Anda lihat di browser. Menggunakan HTML untuk struktur, Tailwind CSS untuk tampilan visual yang menarik, dan JavaScript untuk interaktivitas. JavaScript di sini bertugas memanggil API yang ada di app.py untuk mengambil atau mengirim data.

populate_db.py: Skrip ini bersifat utilitas. Gunakan ini sekali di awal untuk menyiapkan database kosong atau untuk mengisi database dengan beberapa data dummy, mempermudah pengujian dan demonstrasi.

requirements.txt: Daftar semua pustaka Python eksternal yang dibutuhkan proyek ini (misalnya Flask, Flask-SQLAlchemy) beserta versi spesifiknya. Memastikan lingkungan pengembangan yang konsisten.

perpustakaan.db: File ini adalah database SQLite Anda. Ia akan dibuat secara otomatis saat app.py atau populate_db.py pertama kali dijalankan. Semua data buku, anggota, dan peminjaman Anda akan disimpan di sini.

templates/: Folder ini adalah konvensi Flask. Flask mencari file HTML yang akan ditampilkan (render_template) di dalam folder ini.

Semoga README.md ini sangat membantu Anda dalam menyajikan proyek Anda!

> > > > > > > 88748b48c06f0596b82e041c6068e76fc3a35ed6
