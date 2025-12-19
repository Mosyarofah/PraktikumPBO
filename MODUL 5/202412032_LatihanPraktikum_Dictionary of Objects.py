# Program Manajemen Data Pelanggan

class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"ID: {self.id_pelanggan}, Nama: {self.nama}, Email: {self.email}"


# Dictionary untuk menyimpan data pelanggan
data_pelanggan = {}


# Fungsi menambah pelanggan
def tambah_pelanggan(data, pelanggan):
    if pelanggan.id_pelanggan in data:
        print("ID pelanggan sudah ada.")
    else:
        data[pelanggan.id_pelanggan] = pelanggan
        print("Pelanggan berhasil ditambahkan.")


# Fungsi menghapus pelanggan
def hapus_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        del data[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("Pelanggan tidak ditemukan.")


# Fungsi mencari pelanggan
def cari_pelanggan(data, id_pelanggan):
    return data.get(id_pelanggan, None)


# Menambahkan beberapa pelanggan
tambah_pelanggan(data_pelanggan, Pelanggan("PL001", "Andi", "andi@gmail.com"))
tambah_pelanggan(data_pelanggan, Pelanggan("PL002", "Budi", "budi@gmail.com"))
tambah_pelanggan(data_pelanggan, Pelanggan("PL003", "Citra", "citra@gmail.com"))


# Menampilkan seluruh pelanggan
print("\n=== DAFTAR PELANGGAN ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())


# Mencari pelanggan
id_cari = "PL002"
print(f"\n=== HASIL PENCARIAN ID {id_cari} ===")
hasil = cari_pelanggan(data_pelanggan, id_cari)
if hasil:
    print(hasil.info())
else:
    print("Pelanggan tidak ditemukan.")


# Menghapus pelanggan
hapus_pelanggan(data_pelanggan, "PL001")


# Menampilkan ulang daftar pelanggan
print("\n=== DAFTAR PELANGGAN SETELAH PENGHAPUSAN ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())
