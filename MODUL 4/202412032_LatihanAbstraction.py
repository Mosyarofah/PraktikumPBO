from abc import ABC, abstractmethod
import math

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass


class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari


class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar, warna):
        self.panjang = panjang
        self.lebar = lebar
        self.warna = warna

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def info(self):
        return f"Persegi Panjang warna {self.warna}"


class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi


# --------------------------
# Contoh penggunaan (a–d)
# --------------------------

print("=== LINGKARAN ===")
ling = Lingkaran(5)
print("Luas:", f"{ling.luas():.2f}")
print("Keliling:", f"{ling.keliling():.2f}")

print("\n=== PERSEGI PANJANG ===")
pp = PersegiPanjang(4, 3, "Biru")
print("Luas:", pp.luas())
print("Keliling:", pp.keliling())
print("Info:", pp.info())

print("\n=== PERSEGI ===")
sq = Persegi(6)
print("Luas:", sq.luas())
print("Keliling:", sq.keliling())
