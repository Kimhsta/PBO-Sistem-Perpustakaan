from Controller.peringkat_member import PeringkatMember
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_peringkat_member():
    clear_screen()
    print("Menu Peringkat Member")
    print("====================")
    print("1. Tampilkan Peringkat Member")
    print("9. Kembali ke Menu Sebelumnya")
    print("0. Kembali ke Menu Utama")

    choice = input("Pilih Menu: ")

    if choice == '1':
        tampilkan_peringkat_member()
    elif choice == '9':
        from main import admin_menu
        admin_menu()
    elif choice == '0':
        from main import main_menu
        main_menu()
    else:
        print("Input tidak valid, silakan ulangi.")
        menu_peringkat_member()

def tampilkan_peringkat_member():
    clear_screen()
    PeringkatMember.tampilkan_peringkat()
    input("Tekan Enter untuk kembali.")
    menu_peringkat_member()