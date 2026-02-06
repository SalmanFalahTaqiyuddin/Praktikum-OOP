from abc import ABC, abstractmethod

# 1. ABSTRACTION (Kerangka Dasar)
class BarangElektronik(ABC):
    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        # 2. ENCAPSULATION (Private Attributes)
        self.__stok = 0
        self.__harga_dasar = harga_dasar
        
        # Inisialisasi stok menggunakan setter untuk validasi awal
        self.set_stok(stok)

    # Getter untuk stok
    def get_stok(self):
        return self.__stok

    # Getter untuk harga dasar
    def get_harga_dasar(self):
        return self.__harga_dasar

    # Setter dengan Validasi
    def set_stok(self, jumlah):
        if jumlah >= 0:
            self.__stok = jumlah
            return True
        else:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# 3. INHERITANCE (Pewarisan)
class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor
        self.pajak = 0.10  # Pajak 10%

    # 4. POLYMORPHISM (Override Method)
    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(10%): Rp {self.get_harga_dasar() * self.pajak:,.0f}")

    def hitung_harga_total(self, jumlah):
        harga_plus_pajak = self.get_harga_dasar() * (1 + self.pajak)
        return harga_plus_pajak * jumlah


class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)
        self.kamera = kamera
        self.pajak = 0.05  # Pajak 5%

    # 4. POLYMORPHISM (Override Method)
    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(5%): Rp {self.get_harga_dasar() * self.pajak:,.0f}")

    def hitung_harga_total(self, jumlah):
        harga_plus_pajak = self.get_harga_dasar() * (1 + self.pajak)
        return harga_plus_pajak * jumlah


# Fitur Keranjang Belanja (Fungsi di luar class)
def proses_transaksi(daftar_belanja):
    print("\n--- STRUK TRANSAKSI ---")
    total_tagihan = 0
    for i, item in enumerate(daftar_belanja, 1):
        produk = item['produk']
        qty = item['jumlah']
        
        # Cek ketersediaan stok
        if produk.get_stok() >= qty:
            subtotal = produk.hitung_harga_total(qty)
            print(f"{i}. ", end="")
            produk.tampilkan_detail()
            print(f"Beli: {qty} unit | Subtotal: Rp {subtotal:,.0f}")
            
            # Kurangi stok
            produk.set_stok(produk.get_stok() - qty)
            total_tagihan += subtotal
        else:
            print(f"{i}. Stok {produk.nama} tidak mencukupi!")
            
    print("-" * 30)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}")
    print("-" * 30)


# --- EKSEKUSI SESUAI ALUR PROGRAM (USER STORY) ---

print("--- SETUP DATA ---")
# 1. Admin membuat data produk
laptop_rog = Laptop("ROG Zephyrus", 10, 20000000, "Ryzen 9")
iphone_13 = Smartphone("iPhone 13", 20, 15000000, "12MP")

print(f"Berhasil menambahkan stok {laptop_rog.nama}: {laptop_rog.get_stok()} unit.")

# 2. Admin mencoba mengisi stok dengan angka negatif
iphone_13.set_stok(-5) 
print(f"Berhasil menambahkan stok {iphone_13.nama}: {iphone_13.get_stok()} unit.")

# 3 & 4. User membeli produk dan menampilkan struk
keranjang = [
    {"produk": laptop_rog, "jumlah": 2},
    {"produk": iphone_13, "jumlah": 1}
]

proses_transaksi(keranjang)