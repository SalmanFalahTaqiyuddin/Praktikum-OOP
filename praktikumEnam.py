# --- Parent Class ---
class Hero:
    def __init__(self, nama):
        self.nama = nama

    # KUNCI ERROR: Method di bawah ini harus dihapus/dikomentar
    # def serang(self):
    #     print("Hero menyerang dengan tangan kosong.")

# --- Child Classes ---
class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")

class Archer(Hero):
    # Nama method diubah, sehingga Archer tidak punya method 'serang'
    def tembak_panah(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")

class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")

class Healer(Hero):
    def serang(self):
        print(f"{self.nama} (Healer) tidak menyerang, tapi menyembuhkan teman!")

# --- Penerapan Polymorphism ---
pasukan = [
    Mage("Eudora"),
    Archer("Miya"), # Ini yang akan memicu error
    Fighter("Zilong"),
    Healer("Estes")
]

print("--- PERANG DIMULAI ---")

for pahlawan in pasukan:
    # Saat loop sampai di Archer (Miya), program akan CRASH
    # Karena Archer tidak punya 'serang' dan Hero juga tidak punya 'serang'
    pahlawan.serang()
    