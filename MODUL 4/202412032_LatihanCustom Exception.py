class UmurTidakValidError(Exception):
    """Kesalahan untuk umur yang tidak masuk akal."""
    pass

class UmurTerlaluMudaError(Exception):
    """Kesalahan untuk umur kurang dari 5 tahun."""
    pass

class UmurTerlaluTuaError(Exception):
    """Kesalahan untuk umur lebih dari 100 tahun."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Kesalahan jika umur tidak memenuhi syarat pendaftaran akun."""
    pass

def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda! Minimal 5 tahun.")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua! Maksimal 100 tahun.")
    return umur


def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Akun hanya bisa dibuat oleh umur 18+.")
    return "Akun berhasil dibuat."


if __name__ == "__main__":
    
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)
        except ValueError:
            print("Input harus berupa bilangan bulat!")
        except (UmurTidakValidError, UmurTerlaluMudaError, UmurTerlaluTuaError) as e:
            print("Error:", e)
        else:
            print("Umur berhasil disimpan:", umur)
            break
        finally:
            print("Selesai memproses input.\n")

    # Proses daftar akun
    try:
        hasil = daftar_akun(umur)
        print(hasil)
    except AkunTidakDiizinkanError as e:
        print("Gagal daftar akun:", e)
