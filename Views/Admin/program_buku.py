from Controller.buku import Buku
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_buku():
    clear_screen()
    print("Menu Kelola Buku")
    print("================")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Hapus Buku")
    print("9. Kembali ke Menu Sebelumnya")
    print("0. Keluar")

    choice = input("Pilih Menu: ")

    if choice == '1':
        tambah_buku()
    elif choice == '2':
        tampilkan_buku()
    elif choice == '3':
        hapus_buku()
    elif choice == '9':
        from main import admin_menu
        admin_menu()
    elif choice == '0':
        exit()
    else:
        print("Input tidak valid, silakan ulangi.")
        menu_buku()

def tambah_buku():
    clear_screen()
    kode = input("Masukkan kode buku: ")
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    Buku(kode, judul, penulis)
    print(f"Buku '{judul}' berhasil ditambahkan!")
    input("Tekan Enter untuk kembali.")
    menu_buku()

def tampilkan_buku():
    clear_screen()
    Buku.tampilkan_buku()
    input("Tekan Enter untuk kembali.")
    menu_buku()

def hapus_buku():
    clear_screen()
    kode = input("Masukkan kode buku yang ingin dihapus: ")
    if Buku.hapus_buku(kode):
        print("Buku berhasil dihapus.")
    else:
        print("Buku tidak ditemukan.")
    input("Tekan Enter untuk kembali.")
    menu_buku()
