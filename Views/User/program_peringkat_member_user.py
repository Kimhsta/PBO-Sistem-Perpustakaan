from Controller.peringkat_member import PeringkatMember
from Controller.member import Member
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_peringkat_member_user(nim_mahasiswa):
    clear_screen()
    print("\033[1;36m=" * 40 + "\033[0m")
    print("\033[1;33m         Menu Peringkat Member        \033[0m")
    print("\033[1;36m=" * 40 + "\033[0m")
    print(f"\033[1;34mNIM Mahasiswa: {nim_mahasiswa}\033[0m")
    print("1. Tampilkan Peringkat Member")
    print("0. Kembali ke Halaman Home")

    choice = input("\033[1;34mPilih Menu: \033[0m")

    if choice == '1':
        tampilkan_peringkat_member(nim_mahasiswa)
    elif choice == '0':
        from Views.User.program_login import User_menu
        User_menu(nim_mahasiswa)
    else:
        print("\033[1;31mInput tidak valid, silakan ulangi.\033[0m")
        input("Tekan Enter untuk melanjutkan.")
        menu_peringkat_member_user(nim_mahasiswa)

def tampilkan_peringkat_member(nim_mahasiswa):
    clear_screen()
    PeringkatMember.tampilkan_peringkat()
    input("\033[1;34mTekan Enter untuk kembali.\033[0m")
    menu_peringkat_member_user(nim_mahasiswa)
