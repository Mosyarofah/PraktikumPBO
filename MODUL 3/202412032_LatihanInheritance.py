# Class induk
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}"


# Class turunan
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)   # Memanggil constructor parent class
        self.nim = nim

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, NIM: {self.nim}"


# Instansiasi objek
p = Person("Andi", 30)
m = Mahasiswa("Budi", 20, "23050123")

# Pemanggilan method info()
print(p.info())
print(m.info())
