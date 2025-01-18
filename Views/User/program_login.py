from Controller.login import Login
from Controller.member import Member
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    clear_screen()
    print("Program Login")
    print("=============")
    nim_mahasiswa = input("Masukkan NIM Mahasiswa: ")

    if Login.login(nim_mahasiswa):
        print("Login berhasil!")
        input("Tekan Enter untuk melanjutkan.")
        User_menu(nim_mahasiswa)
    else:
        print("NIM Mahasiswa tidak valid.")
        input("Tekan Enter untuk mencoba lagi.")
        login()

def User_menu(nim_mahasiswa):
    clear_screen()
    print("Selamat datang di Program User")
    print("=================================")
    print(f"NIM Mahasiswa: {nim_mahasiswa}")
    print("1. Program Peminjaman Buku")
    print("2. Program Pengembalian Buku")
    print("0. Kembali ke Halaman Home")

    choice = input("Pilih Menu: ")

    if choice == '1':
        from Views.User.program_peminjaman import menu_peminjaman
        menu_peminjaman(nim_mahasiswa)
    elif choice == '2':
        from Views.User.program_pengembalian import menu_pengembalian
        menu_pengembalian(nim_mahasiswa)
    elif choice == '0':
        from main import main_menu
        main_menu()
    else:
        print("Input tidak valid, silakan ulangi.")
        User_menu(nim_mahasiswa)
