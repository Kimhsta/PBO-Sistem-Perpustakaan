from Controller.member import Member
from Controller.peminjaman import Peminjaman

class PeringkatMember:
    @classmethod
    def hitung_peringkat(cls):
        member_terbaik = None
        poin_tertinggi = 0
        for member in Member.daftar_member:
            poin = len([p for p in Peminjaman.daftar_peminjaman if p.member == member.nim_mahasiswa])
            if poin > poin_tertinggi:
                poin_tertinggi = poin
                member_terbaik = member
        return member_terbaik, poin_tertinggi

    @classmethod
    def tampilkan_peringkat(cls):
        member_terbaik, poin_tertinggi = cls.hitung_peringkat()
        if member_terbaik:
            print(f"Member terbaik: {member_terbaik.nama} dengan poin {poin_tertinggi}")
        else:
            print("Belum ada member yang meminjam buku.")