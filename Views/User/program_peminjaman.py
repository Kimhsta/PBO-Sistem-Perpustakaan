from Controller.peminjaman import Peminjaman
from Controller.buku import Buku
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_peminjaman(nim_mahasiswa):
    clear_screen()
    print("Program Peminjaman Buku")
    print("=======================")
    Buku.tampilkan_buku()

    kode_buku = input("Masukkan kode buku yang ingin dipinjam: ")
    buku_dipinjam = next((b for b in Buku.daftar_buku if b.kode == kode_buku), None)
    if buku_dipinjam:
        Peminjaman(nim_mahasiswa, buku_dipinjam)
        print(f"Buku '{buku_dipinjam.judul}' berhasil dipinjam oleh anggota dengan ID {nim_mahasiswa}.")
    else:
        print("Buku tidak ditemukan.")

    input("Tekan Enter untuk kembali.")
    from Views.User.program_login import User_menu
    User_menu(nim_mahasiswa)
