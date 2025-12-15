from abc import ABC, abstractmethod

class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass

class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        return f"Member {self.nama} memiliki hak akses penuh."


class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def __str__(self):
        return f"Member: {self.nama} - Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)

    def akses(self):
        return f"Akses diberikan kepada {self.nama}."


def minta_poin():
    while True:
        try:
            inp = input("Masukkan poin member: ").strip()

            if inp == "":
                raise Exception("Input tidak boleh kosong!")

            poin = int(inp)

            return poin

        except ValueError:
            print("Error: Poin harus berupa angka!")

        except Exception as e:  # untuk input kosong
            print("Error:", e)

class PoinTidakValidError(Exception):
    pass

def cek_poin(p):
    if p < 0:
        raise PoinTidakValidError("Poin tidak boleh negatif!")
    return p


if __name__ == "__main__":

    print("=== Input Poin Member 1 ===")
    try:
        p1 = minta_poin()
        p1 = cek_poin(p1)  # cek custom exception
        m1 = Member("Andi", p1)

    except PoinTidakValidError as e:
        print("Kesalahan:", e)
        exit()

    print("\n=== Input Poin Member 2 ===")
    try:
        p2 = minta_poin()
        p2 = cek_poin(p2)
        m2 = Member("Budi", p2)

    except PoinTidakValidError as e:
        print("Kesalahan:", e)
        exit()

    print("\n=== OUTPUT ===")

    print(m1)
    print(m2)

    print("Total poin:", m1 + m2)

    print("Panjang nama m1:", len(m1))
