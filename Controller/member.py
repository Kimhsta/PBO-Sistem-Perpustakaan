class Member:
    daftar_member = []

    def __init__(self, nim_mahasiswa, nama, alamat, email, status_keanggotaan):
        self.nim_mahasiswa = nim_mahasiswa
        self.nama = nama
        self.alamat = alamat
        self.email = email
        self.status_keanggotaan = status_keanggotaan
        Member.daftar_member.append(self)

    @classmethod
    def tampilkan_member(cls):
        if not cls.daftar_member:
            print("\033[1;31mTidak ada Mahasiswa yang terdaftar dalam member.\033[0m")
        else:
            print("\033[1;36m=" * 90 + "\033[0m")
            print(
                f"\033[1;33m{'NIM':<10}{'Nama':<20}{'Alamat':<20}{'Email':<30}{'Status':<10}\033[0m"
            )
            print("\033[1;36m=" * 90 + "\033[0m")
            for member in cls.daftar_member:
                print(
                    f"{member.nim_mahasiswa:<10}{member.nama:<20}{member.alamat:<20}"
                    f"{member.email:<30}{member.status_keanggotaan:<10}"
                )
            print("\033[1;36m=" * 90 + "\033[0m")

    @classmethod
    def cari_member(cls, nim_mahasiswa):
        for member in cls.daftar_member:
            nim_mahasiswa = input("Masukkan NIM Member: ")
            member = Member.cari_member(nim_mahasiswa)
            if member.nim_mahasiswa == nim_mahasiswa:
                print("\033[1;32mMember ditemukan!\033[0m")
                print("\033[1;33m" + "=" * 50 + "\033[0m")
                print(
                    f"NIM: {member.nim_mahasiswa}\n"
                    f"Nama: {member.nama}\n"
                    f"Alamat: {member.alamat}\n"
                    f"Email: {member.email}\n"
                    f"Status: {member.status_keanggotaan}"
                )
                print("\033[1;33m" + "=" * 50 + "\033[0m")
                return member
        print("\033[1;31mMember tidak ditemukan.\033[0m")
        return None

    @classmethod
    def hapus_member(cls, nim_mahasiswa):
        for member in cls.daftar_member:
            if member.nim_mahasiswa == nim_mahasiswa:
                cls.daftar_member.remove(member)
                print("\033[1;32mMember berhasil dihapus.\033[0m")
                return True
        print("\033[1;31mMember tidak ditemukan.\033[0m")
        return False

    @classmethod
    def edit_member(cls, nim_mahasiswa, nama=None, alamat=None, email=None, status_keanggotaan=None):
        for member in cls.daftar_member:
            if member.nim_mahasiswa == nim_mahasiswa:
                if nama:
                    member.nama = nama
                if alamat:
                    member.alamat = alamat
                if email:
                    member.email = email
                if status_keanggotaan:
                    member.status_keanggotaan = status_keanggotaan
                print("\033[1;32mMember berhasil diedit.\033[0m")
                return True
        print("\033[1;31mMember tidak ditemukan.\033[0m")
        return False
