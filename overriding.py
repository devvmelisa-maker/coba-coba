class Anggota:
    def __init__(self, nama):
        self.nama = nama
    def batas_hari(self):
     return 7
class AnggotaDosen(Anggota):
     def batas_hari(self):
        return 14
class AnggotaTamu(Anggota):
    def batas_hari(self): 
        return 3
for obj in [Anggota("Rina"), AnggotaDosen("Budi"),
    AnggotaTamu("Sari")]:
    print(obj.nama, "→", obj.batas_hari(), "hari")