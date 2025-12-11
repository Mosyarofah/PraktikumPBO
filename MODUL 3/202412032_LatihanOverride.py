# Class induk
class Bentuk:
    def luas(self):
        return 0

# Class turunan: Persegi
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

# Class turunan: Lingkaran
class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        phi = 22/7
        return phi * self.radius * self.radius


# Demonstrasi pemanggilan method luas()
p = Persegi(5)
l = Lingkaran(7)

print("Luas Persegi:", p.luas())
print("Luas Lingkaran:", l.luas())
