class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Private Variable
        self.__hp = hp_awal

    # GETTER
    def get_hp(self):
        return self.__hp

    # SETTER (dengan Validasi)
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")

# --- Uji Coba ---
hero1 = Hero("Layla", 100)

# Tugas Analisis 4 - Poin 1 (Hacking)
print(f"Mencoba akses paksa: {hero1._Hero__hp}") 

# Tugas Analisis 4 - Poin 2 (Uji Validasi)
hero1.set_hp(-100)
print(hero1.get_hp())