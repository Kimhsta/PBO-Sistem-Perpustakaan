from Controller.laporan import Laporan
from main import main_menu
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_laporan():
    clear_screen()
    print("Menu Laporan")
    print("============")
    print("1. Lihat Laporan Peminjaman")
    print("9. Kembali ke Menu Sebelumnya")
    print("0. Kembali ke Menu Utama")

    choice = input("Pilih Menu: ")

    if choice == '1':
        tampilkan_laporan()
    elif choice == '9':
        from main import admin_menu
        admin_menu()
    elif choice == '0':
        main_menu()
    else:
        print("Input tidak valid, silakan ulangi.")
        menu_laporan()

def tampilkan_laporan():
    clear_screen()
    Laporan.tampilkan_laporan()
    input("Tekan Enter untuk kembali.")
    menu_laporan()
