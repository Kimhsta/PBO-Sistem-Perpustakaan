from Controller.member import Member

class Login:
    @staticmethod
    def login(nim_mahasiswa):
        member = Member.cari_member(nim_mahasiswa)
        if member:
            return True
        return False
