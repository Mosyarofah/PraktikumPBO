def operasi():
    print("=== Operasi Matematika Aman ===")
    print("Pilih operasi:")
    print("1. Pembagian")
    print("2. Perkalian")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()

    try:
        if x == "" or y == "":
            raise ValueError("Input tidak boleh kosong! Anda menekan Enter tanpa mengisi angka.")

        a = float(x)
        b = float(y)

        if a < 0 or b < 0:
            raise ValueError("Hanya angka positif yang diperbolehkan!")

        # Operasi utama
        if pilihan == "1":
            hasil = a / b  # berpotensi ZeroDivisionError
        elif pilihan == "2":
            hasil = a * b
        else:
            raise ValueError("Pilihan tidak valid! Gunakan 1 atau 2.")

    except ValueError as ve:
        print("Terjadi kesalahan input:", ve)

    except ZeroDivisionError:
        print("ERROR: Pembagian dengan penyebut nol tidak diperbolehkan!")

    except Exception as e:
        print("Kesalahan tidak terduga:", e)

    else:
        print(f"Hasil operasi: {hasil}")

    finally:
        print("Selesai memproses input.")


if __name__ == "__main__":
    operasi()
