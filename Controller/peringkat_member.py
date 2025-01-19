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
        print("\033[1;36m=" * 40 + "\033[0m")
        print("\033[1;33m       Peringkat Member Terbaik       \033[0m")
        print("\033[1;36m=" * 40 + "\033[0m")
        if member_terbaik:
            print(f"\033[1;32mMember Terbaik:\033[0m {member_terbaik.nama}")
            print(f"\033[1;32mPoin Tertinggi:\033[0m {poin_tertinggi}")
        else:
            print("\033[1;31mBelum ada member yang meminjam buku.\033[0m")
        print("\033[1;36m=" * 40 + "\033[0m")
