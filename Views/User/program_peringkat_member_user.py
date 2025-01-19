from Controller.peringkat_member import PeringkatMember
from Controller.member import Member
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_peringkat_member_user(nim_mahasiswa):
    clear_screen()
    print("Menu Peringkat Member")
    print("====================")
    print(f"NIM Mahasiswa: {nim_mahasiswa}")
    print("1. Tampilkan Peringkat Member")
    print("0. Kembali ke Halaman Home")

    choice = input("Pilih Menu: ")

    if choice == '1':
        tampilkan_peringkat_member()
    elif choice == '0':
        from Views.User.program_login import User_menu
        User_menu(nim_mahasiswa)
    else:
        print("Input tidak valid, silakan ulangi.")
        menu_peringkat_member_user(nim_mahasiswa)

def tampilkan_peringkat_member():
    clear_screen()
    PeringkatMember.tampilkan_peringkat()
    input("Tekan Enter untuk kembali.")
    menu_peringkat_member_user(nim_mahasiswa)