import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("Selamat Datang di Sistem Perpustakaan")
    print("=====================================")
    print("1. Menu Admin")
    print("2. Program Pengguna")
    print("0. Keluar")

    choice = input("Pilih Menu: ")

    if choice == '1':
        from Views.Admin import program_buku, program_member, program_laporan
        admin_menu()
    elif choice == '2':
        member_menu()
    elif choice == '0':
        print("Terima kasih!")
        exit()
    else:
        print("Input tidak valid, silakan ulangi.")
        main_menu()

def admin_menu():
    clear_screen()
    print("Menu Admin")
    print("==========")
    print("1. Kelola Buku")
    print("2. Kelola Anggota")
    print("3. Lihat Laporan")
    print("0. Kembali ke Menu Utama")

    choice = input("Pilih Menu: ")

    if choice == '1':
        from Views.Admin import program_buku
        program_buku.menu_buku()
    elif choice == '2':
        from Views.Admin import program_member
        program_member.menu_member()
    elif choice == '3':
        from Views.Admin import program_laporan
        program_laporan.menu_laporan()
    elif choice == '0':
        main_menu()
    else:
        print("Input tidak valid, silakan ulangi.")
        admin_menu()

def member_menu():
    clear_screen()
    print("Menu Pengguna")
    print("=============")
    print("1. Login")
    print("0. Kembali ke Menu Utama")

    choice = input("Pilih Menu: ")

    if choice == '1':
        from Views.User import program_login
        program_login.login() 
    elif choice == '0':
        main_menu()
    else:
        print("Input tidak valid, s1ilakan ulangi.")
        member_menu()

if __name__ == "__main__":
    main_menu()
