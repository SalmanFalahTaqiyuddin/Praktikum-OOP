from abc import ABC, abstractmethod

# ==========================================
# 1. INTERFACE / ABSTRACT CLASS (BLUEPRINT)
# ==========================================
class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

# ==========================================
# 2. IMPLEMENTASI PADA CLASS KONKRET
# ==========================================

class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    # Implementasi wajib method serang
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    # Implementasi wajib method info
    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    # Implementasi wajib method serang versi Monster
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    # Implementasi wajib method info
    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")

# ==========================================
# 3. UJI COBA
# ==========================================

unit = GameUnit() # <-- Ini akan ERROR jika diaktifkan (karena abstrak)

h = Hero("Alucard")
m = Monster("Serigala")

h.info()
h.serang("Serigala")

print("-" * 20)

m.info()
m.serang("Alucard")
