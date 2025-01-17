
class Buku:
    daftar_buku = []

    def __init__(self, kode, judul, penulis):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis
        Buku.daftar_buku.append(self)

    @classmethod
    def tampilkan_buku(cls):
        if not cls.daftar_buku:
            print("Tidak ada buku yang tersedia.")
        else:
            print("="*35)
            print(f"{'Kode':<5}{'Judul':<20}{'Penulis':<10}")
            print("="*35)
            for buku in cls.daftar_buku:
                print(f"{buku.kode:<5}{buku.judul:<20}{buku.penulis:<10}")
            print("="*35)

    @classmethod
    def hapus_buku(cls, kode):
        for buku in cls.daftar_buku:
            if buku.kode == kode:
                cls.daftar_buku.remove(buku)
                return True
        return False