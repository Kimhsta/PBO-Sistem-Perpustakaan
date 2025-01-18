class Peminjaman:
    daftar_peminjaman = []

    def __init__(self, member, buku):
        self.member = member
        self.buku = buku
        Peminjaman.daftar_peminjaman.append(self)

    @classmethod
    def tampilkan_peminjaman(cls, member):
        pinjaman = [p for p in cls.daftar_peminjaman if p.member == member]
        if not pinjaman:
            print("Belum ada buku yang dipinjam.")
        else:
            print("="*40)
            print(f"{'Kode Buku':<10}{'Judul Buku':<20}")
            print("="*40)
            for p in pinjaman:
                print(f"{p.buku.kode:<10}{p.buku.judul:<20}")
            print("="*40)
