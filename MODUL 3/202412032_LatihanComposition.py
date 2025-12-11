# Class Penulis
class Penulis:
    def __init__(self, nama):
        self.nama = nama

# Class Buku (memiliki Penulis → composition)
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis.nama}"

# Demonstrasi akses data penulis dari objek buku
p = Penulis("Tere Liye")
b = Buku("Bumi", p)

print(b.info())
print("Nama Penulis:", b.penulis.nama)   # akses langsung ke atribut penulis
