class ManajerInventori:
    def __init__(self):
        # inventori disimpan dalam dictionary
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0"

        if nama in self.inventori:
            self.inventori[nama] += jumlah
        else:
            self.inventori[nama] = jumlah

        return f"Berhasil menambah {jumlah} {nama}. Total: {self.inventori[nama]}"

    def hapus_barang(self, nama):
        if nama in self.inventori:
            del self.inventori[nama]
            return f"{nama} berhasil dihapus dari inventori"
        return f"{nama} tidak ditemukan dalam inventori"

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"
        
        daftar = "Daftar Inventori:\n"
        for barang, jumlah in self.inventori.items():
            daftar += f"- {barang}: {jumlah}\n"
        return daftar


# ====== Testing / Demonstrasi ======

inv = ManajerInventori()

print(inv.tambah_barang("Pensil", 20))
print(inv.tambah_barang("Buku", 15))
print(inv.tambah_barang("Pensil", 10))  # menambah stok

print(inv.lihat_inventori())

print(inv.hapus_barang("Buku"))
print(inv.lihat_inventori())
