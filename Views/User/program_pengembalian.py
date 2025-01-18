from Controller.pengembalian import Pengembalian
from Controller.peminjaman import Peminjaman
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_pengembalian(nim_mahasiswa):
    clear_screen()
    print("Program Pengembalian Buku")
    print("=========================")
    Peminjaman.tampilkan_peminjaman(nim_mahasiswa)

    kode_buku = input("Masukkan kode buku yang ingin dikembalikan: ")
    if Pengembalian.kembalikan_buku(nim_mahasiswa, kode_buku):
        print("Buku berhasil dikembalikan.")
    else:
        print("Pengembalian gagal. Buku tidak ditemukan dalam daftar pinjaman.")

    input("Tekan Enter untuk kembali.")
    from Views.User.program_login import User_menu
    User_menu(nim_mahasiswa)
