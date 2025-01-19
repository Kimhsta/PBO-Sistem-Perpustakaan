from Controller.member import Member
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    clear_screen()
    print("\033[1;36m" + "="*40 + "\033[0m")  # Header line
    print(f"\033[1;33m{title.center(40)}\033[0m")  # Title in yellow
    print("\033[1;36m" + "="*40 + "\033[0m")  # Footer line

def menu_member():
    print_header("Menu Kelola Member")
    print("\033[1;32m1\033[0m. Tambah Member")
    print("\033[1;32m2\033[0m. Lihat Member")
    print("\033[1;32m3\033[0m. Cari Member")
    print("\033[1;32m4\033[0m. Hapus Member")
    print("\033[1;32m5\033[0m. Edit Member")
    print("\033[1;32m9\033[0m. Kembali ke Menu Sebelumnya")
    print("\033[1;32m0\033[0m. Kembali ke Menu Utama")
    print("\033[1;36m" + "-"*40 + "\033[0m")  # Separator

    choice = input("\033[1;34mPilih Menu: \033[0m")
    if choice == '1':
        tambah_member()
    elif choice == '2':
        tampilkan_member()
    elif choice == '3':
        cari_member()
    elif choice == '4':
        hapus_member()
    elif choice == '5':
        edit_member()
    elif choice == '9':
        from main import admin_menu
        admin_menu()
    elif choice == '0':
        from main import main_menu
        main_menu()
    else:
        print("\033[1;31mInput tidak valid, silakan ulangi.\033[0m")
        input("Tekan Enter untuk melanjutkan.")
        menu_member()

def tambah_member():
    print_header("Tambah Member")
    nim_mahasiswa = input("Masukkan NIM Mahasiswa: ")
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    email = input("Masukkan email: ")
    status_keanggotaan = input("Masukkan status [Aktif/Tidak Aktif]: ")
    Member(nim_mahasiswa, nama, alamat, email, status_keanggotaan)
    print(f"\033[1;32mMember '{nama}' berhasil ditambahkan!\033[0m")
    input("Tekan Enter untuk kembali.")
    menu_member()

def hapus_member():
    print_header("Hapus Member")
    nim_mahasiswa = input("Masukkan NIM Mahasiswa yang ingin dihapus: ")
    if Member.hapus_member(nim_mahasiswa):
        print("\033[1;32mMember berhasil dihapus.\033[0m")
    else:
        print("\033[1;31mMember tidak ditemukan.\033[0m")
    input("Tekan Enter untuk kembali.")
    menu_member()

def edit_member():
    print_header("Edit Member")
    nim_mahasiswa = input("Masukkan NIM Mahasiswa yang ingin diedit: ")
    nama = input("Masukkan nama baru: ")
    alamat = input("Masukkan alamat baru: ")
    email = input("Masukkan email baru: ")
    status_keanggotaan = input("Masukkan status baru [Aktif/Tidak Aktif]: ")
    if Member.edit_member(nim_mahasiswa, nama, alamat, email, status_keanggotaan):
        print("\033[1;32mMember berhasil diedit.\033[0m")
    else:
        print("\033[1;31mMember tidak ditemukan.\033[0m")
    input("Tekan Enter untuk kembali.")
    menu_member()

def tampilkan_member():
    print_header("Daftar Member")
    Member.tampilkan_member()
    input("Tekan Enter untuk kembali.")
    menu_member()

def cari_member():
    print_header("Cari Member")
    nim_mahasiswa = input("Masukkan NIM Member: ")
    member = Member.cari_member(nim_mahasiswa)
    if member:
        print(f"\033[1;32mNIM: {member.nim_mahasiswa} - Nama: {member.nama}\033[0m")
    else:
        print("\033[1;31mMember tidak ditemukan.\033[0m")
    input("Tekan Enter untuk kembali.")
    menu_member()