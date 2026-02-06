# --- STEP 1: Class Induk (Hero) ---
class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

# --- STEP 2: Class Anak (Mage) ---
# Mage mewarisi sifat dari Hero
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        # Memanggil constructor milik Parent (Hero) agar atribut dasar terisi
        # super().__init__(name, hp, attack_power) 
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    # Skill khusus Mage yang tidak dimiliki Hero biasa
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2) # Damage 2x lipat
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")

# --- STEP 3: Main Program ---
print("\n--- Update Class Hero ---")

# Membuat objek Eudora (Mage) dan Balmond (Hero Biasa)
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

# Menjalankan aksi
eudora.info()
eudora.serang(balmond)         # Serangan biasa (warisan Hero)
print("-" * 30)
eudora.skill_fireball(balmond) # Skill khusus (milik Mage)