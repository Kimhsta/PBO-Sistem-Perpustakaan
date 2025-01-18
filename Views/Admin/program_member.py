from Controller.member import Member
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_member():
    clear_screen()
    print("Menu Kelola Member")
    print("===================")
    print("1. Tambah Member")
    print("2. Lihat Member")
    print("3. Cari Member")
    print("4. Hapus Member")
    print("5. Edit Member")
    print("9. Kembali ke Menu Sebelumnya")
    print("0. Kembali ke Menu Utama")

    choice = input("Pilih Menu: ")

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
        print("Input tidak valid, silakan ulangi.")
        menu_member()

def tambah_member():
    clear_screen()
    nim_mahasiswa = input("Masukkan NIM Mahasiswa: ")
    nama = input("Masukkan nama member: ")
    alamat = input("Masukkan alamat member: ")
    email = input("Masukkan email member: ")
    status_keanggotaan = input("Masukkan status keanggotaan member: ")
    Member(nim_mahasiswa, nama, alamat, email, status_keanggotaan)
    print(f"Member '{nama}' berhasil ditambahkan!")
    input("Tekan Enter untuk kembali.")
    menu_member()

def hapus_member():
    clear_screen()
    nim_mahasiswa = input("Masukkan NIM Mahasiswa yang ingin dihapus: ")
    if Member.hapus_member(nim_mahasiswa):
        print("Member berhasil dihapus.")
    else:
        print("Member tidak ditemukan.")
    input("Tekan Enter untuk kembali.")
    menu_member()

def edit_member():
    clear_screen()
    nim_mahasiswa = input("Masukkan NIM Mahasiswa yang ingin diedit: ")
    nama = input("Masukkan nama member baru: ")
    alamat = input("Masukkan alamat member baru: ")
    email = input("Masukkan email member baru: ")
    status_keanggotaan = input("Masukkan status keanggotaan member baru: ")
    if Member.edit_member(nim_mahasiswa, nama, alamat, email, status_keanggotaan):
        print("Member berhasil diedit.")
    else:
        print("Member tidak ditemukan.")
    input("Tekan Enter untuk kembali.")
    menu_member()

def tampilkan_member():
    clear_screen()
    Member.tampilkan_member()
    input("Tekan Enter untuk kembali.")
    menu_member()

def cari_member():
    clear_screen()
    nim_mahasiswa = input("Masukkan Nim member: ")
    member = Member.cari_member(nim_mahasiswa)
    if member:
        print(f"NIM: {member.nim_mahasiswa} - Nama: {member.nama}")
    else:
        print("Member tidak ditemukan.")
    input("Tekan Enter untuk kembali.")
    menu_member()
