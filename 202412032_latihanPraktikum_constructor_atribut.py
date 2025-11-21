class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    # Method info kendaraan
    def info(self):
        return f"Merk: {self.merk}, Warna: {self.warna}, Tahun: {self.tahun}, Bahan Bakar: {Kendaraan.bahan_bakar}"


# Instansiasi object
mobil1 = Kendaraan("Toyota Avanza", "Silver", 2020)
motor1 = Kendaraan("Honda Beat", "Merah", 2022)

# Menampilkan info
print(mobil1.info())
print(motor1.info())

# Demonstrasi perbedaan instance attribute dan class attribute
print("\n=== Perbedaan Instance & Class Attribute ===")
print("Merk (instance attribute mobil1):", mobil1.merk)
print("Bahan bakar (class attribute):", Kendaraan.bahan_bakar)

# Mengubah class attribute
Kendaraan.bahan_bakar = "Solar"

print("\n=== Setelah mengubah class attribute ===")
print(mobil1.info())
print(motor1.info())