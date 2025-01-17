class Member:
    daftar_member = []

    def __init__(self, nim_mahasiswa, nama):
        self.nim_mahasiswa = nim_mahasiswa
        self.nama = nama
        Member.daftar_member.append(self)

    @classmethod
    def tampilkan_anggota(cls):
        if not cls.daftar_member:
            print("Tidak ada Mahasiswa yang terdaftar dalam member.")
        else:
            print("="*30)
            print(f"{'ID':<10}{'Nama':<20}")
            print("="*30)
            for member in cls.daftar_member:
                print(f"{member.nim_mahasiswa:<10}{member.nama:<20}")
            print("="*30)

    @classmethod
    def cari_member(cls, nim_mahasiswa):
        for member in cls.daftar_member:
            if member.nim_mahasiswa == nim_mahasiswa:
                return member
        return None