from Controller.peminjaman import Peminjaman

class Pengembalian:
    @staticmethod
    def kembalikan_buku(member, kode_buku):
        for pinjaman in Peminjaman.daftar_peminjaman:
            if pinjaman.member == member and pinjaman.buku.kode == kode_buku:
                Peminjaman.daftar_peminjaman.remove(pinjaman)
                return True
        return False
