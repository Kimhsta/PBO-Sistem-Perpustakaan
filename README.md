# 📚 PBO - Sistem Perpustakaan

Repository ini berisi implementasi dari **Sistem Informasi Perpustakaan** sederhana yang dikembangkan menggunakan prinsip **Pemrograman Berorientasi Objek (PBO)**. Proyek ini dirancang untuk memenuhi tugas kuliah dengan fokus pada pengelolaan buku, anggota perpustakaan, dan transaksi peminjaman serta pengembalian buku.

---

## ✨ Fitur Utama

- **Manajemen Buku**:  
  Tambah, edit, dan hapus data buku termasuk informasi seperti judul dan penulis.

- **Manajemen Anggota**:  
  Registrasi anggota baru, pembaruan data anggota, dan penghapusan anggota.

- **Peminjaman & Pengembalian Buku**:  
  - Pencatatan transaksi peminjaman buku oleh anggota.  
  - Pencatatan pengembalian buku dan perhitungan denda keterlambatan (jika ada).

- **Autentikasi Pengguna**:  
  Sistem login untuk petugas perpustakaan dengan otentikasi username dan password.

---

## 🔧 Teknologi yang Digunakan

- **Bahasa Pemrograman**: Python  
- **Tools**:  
  - IDE: Visual Studio Code  
  - Manajemen Paket: pip  

---

## 📁 **Struktur Proyek**

```plaintext
PBO-Sistem-Perpustakaan/
├── Controller/
│   ├── buku_controller.py
│   ├── anggota_controller.py
│   └── peminjaman_controller.py
├── Views/
│   ├── main_view.py
│   ├── buku_view.py
│   ├── anggota_view.py
│   └── peminjaman_view.py
├── Models/
│   ├── buku_model.py
│   ├── anggota_model.py
│   └── peminjaman_model.py
├── __pycache__/
├── main.py
└── README.md
