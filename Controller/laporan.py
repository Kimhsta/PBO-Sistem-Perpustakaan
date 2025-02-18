from Controller.member import Member
from Controller.peminjaman import Peminjaman

class Laporan:

    @staticmethod
    def cari_member(nim_mahasiswa):
        for member in Member.daftar_member:
            if member.nim_mahasiswa == nim_mahasiswa: 
                return member
        return None

    @staticmethod
    def tampilkan_laporan():
        print("Laporan Peminjaman Buku")
        print("=======================")
        print(f"{'ID Member':<15} {'Nama Member':<20} {'Judul Buku':<30} {'Status':<10}")
        print("=" * 75)
        for peminjaman in Peminjaman.daftar_peminjaman:
            nim_mahasiswa = peminjaman.member 
            member = Laporan.cari_member(nim_mahasiswa)
            nama_member = member.nama if member else "Tidak Diketahui"
            status = "Dipinjam" 
            print(f"{nim_mahasiswa:<15} {nama_member:<20} {peminjaman.buku.judul:<30} {status:<10}")
        print("=" * 75)

