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
            print("Tidak ada Mahasiswa yang terdaftar dalam member.")
        else:
            print("=" * 90)
            print(f"{'NIM':<10}{'Nama':<20}{'Alamat':<20}{'Email':<20}{'Status Keanggotaan':<20}")
            print("=" * 90)
            for member in cls.daftar_member:
                print(
                    f"{member.nim_mahasiswa:<10}{member.nama:<20}{member.alamat:<20}"
                    f"{member.email:<20}{member.status_keanggotaan:<20}"
                )
            print("=" * 90)

    @classmethod
    def cari_member(cls, nim_mahasiswa):
        for member in cls.daftar_member:
            if member.nim_mahasiswa == nim_mahasiswa:
                return member
        return None

    @classmethod
    def hapus_member(cls, nim_mahasiswa):
        for member in cls.daftar_member:
            if member.nim_mahasiswa == nim_mahasiswa:
                cls.daftar_member.remove(member)
                return True
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
                return True
        return False
