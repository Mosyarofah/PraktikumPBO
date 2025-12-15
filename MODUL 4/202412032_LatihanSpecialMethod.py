class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __eq__(self, other):
        return self.nilai == other.nilai

    def __len__(self):
        return len(self.nama)

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

m1 = Mahasiswa("Andi", 85)
m2 = Mahasiswa("Budi", 85)
m3 = Mahasiswa("Cici", 92)

print("=== Representasi String ===")
print(m1)
print(m2)
print(m3)

print("\n=== Perbandingan Kesetaraan (==) ===")
print("m1 == m2 ?", m1 == m2)
print("m1 == m3 ?", m1 == m3)

print("\n=== Operasi Matematika ===")
print("m1 + m3 =", m1 + m3)
print("m2 * 2 =", m2 * 2)

print("\n=== Panjang Nama (__len__) ===")
print("len(m1) =", len(m1))
print("len(m3) =", len(m3))

print("\n=== Sorting daftar mahasiswa berdasarkan nilai ===")
daftar = [m1, m2, m3]
urut = sorted(daftar, key=lambda x: x.nilai)
for m in urut:
    print(m)
