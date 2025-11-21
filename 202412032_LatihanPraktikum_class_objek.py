class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Saya {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}"
    

# Membuat object dosen
dsn1 = Dosen("Ir Abadi Nugroho, S.Kom., M.Kom", "1104129002")
dsn2 = Dosen("Lapu Tombilayuk, S.Kom., M.T.", "1120107301")

# Memanggil method
print(dsn1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dsn2.ajar_mata_kuliah("Sistem Operasi"))