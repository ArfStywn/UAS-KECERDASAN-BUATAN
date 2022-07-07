# Fuzzy Class

class Fuzzy:
    # input
    masaKerja = 0  # menggunakan satuan th / tahun
    produkTerjual = 0  # Menggunakan satuan unit barang

    # define bonus
    bonus = 0
    bonusSedikit = 0
    bonusSedang = 0
    bonusBanyak = 0

    # define masa kerja
    masaKerjaMagang = 0
    masaKerjaBaru = 0
    masaKerjaSedang = 0
    masaKerjaLama = 0

    # define gaji
    terjualSedikit = 0
    terjualSedang = 0
    terjualBanyak = 0

    # define default role
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0
    z5 = 0
    z6 = 0

    # define real role
    R1 = 0
    R2 = 0
    R3 = 0
    R4 = 0
    R5 = 0
    R6 = 0

    # others
    total_RiZi = 0
    total_R = 0
    nilai_z = 0
    angka = 0

    def __init__(self, masaKerja, produkTerjual):
        self.masaKerja = masaKerja
        self.produkTerjual = produkTerjual
        self.hitungMasaKerja()
        self.hitungProdukTerjual()
        self.hitungRole()

    def hitungMasaKerja(self):
        # Jika karyawan magang
        if self.masaKerja <= 2:
            self.masaKerjaMagang = 1
        elif 2 < self.masaKerja < 3:
            self.masaKerjaMagang = (3 - self.masaKerja) / (3 - 2)
        else:
            self.masaKerjaMagang = 0
            
        # Jika karyawan baru
        if self.masaKerja <= 3:
            self.masaKerjaBaru = 2
        elif 3 < self.masaKerja < 5:
            self.masaKerjaBaru = (5 - self.masaKerja) / (5 - 3)
        else:
            self.masaKerjaBaru = 0
            
        # Jika karyawan sedang
        if self.masaKerja <= 3:
            self.masaKerjaSedang = 0
        elif 5 < self.masaKerja < 7:
            self.masaKerjaSedang = (7 - self.masaKerja) / (7 - 5)
        else:
            self.masaKerjaSedang = 0
        
        # Jika karyawan lama
        if self.masaKerja <= 2:
            self.masaKerjaLama = 0
        elif 5 < self.masaKerja <= 8:
            self.masaKerjaLama = (self.masaKerja - 5) / (8 - 5)
        else:
            self.masaKerjaLama = 1

        

    def hitungProdukTerjual(self):
        # Jika produk terjual sedikit
        if self.produkTerjual <= 4:
            self.terjualSedikit = 1
        elif 4 < self.produkTerjual <= 7:
            self.terjualSedikit = (7 - self.produkTerjual) / (7 - 4)
        else:
            self.terjualSedikit = 0
            
        # Jika produk terjual sedang
        if self.produkTerjual <= 4:
            self.terjualSedang = 1
        elif 4 < self.produkTerjual <= 7:
            self.terjualSedang = (7 - self.produkTerjual) / (7 - 4)
        else:
            self.terjualSedang = 0
            
        # Jika produk terjual banyak
        if self.produkTerjual <= 6:
            self.terjualBanyak = 0
        elif 6 < self.produkTerjual <= 10:
            self.terjualBanyak = (self.produkTerjual - 6) / (10 - 6)
        else:
            self.terjualBanyak = 1


    def hitungRole(self):
        self.R1 = min(self.masaKerjaMagang, self.terjualSedikit)
        self.z1 = 2000000 - (2000000 * self.R1)

        self.R2 = min(self.masaKerjaBaru, self.terjualSedikit)
        self.z2 = 2000000 - (1800000 * self.R2)

        self.R3 = min(self.masaKerjaBaru, self.terjualSedang)
        self.z3 = 2000000 - (1700000 * self.R3)

        self.R4 = min(self.masaKerjaBaru, self.terjualBanyak)
        self.z4 = 2000000 - (1600000 * self.R4)

        self.R5 = min(self.masaKerjaSedang, self.terjualSedikit)
        self.z5 = 3000000 + (self.R5 * 300000)

        self.R6 = min(self.masaKerjaSedang, self.terjualSedang)
        self.z6 = 3500000 + (self.R6 * 300000)

        self.R7 = min(self.masaKerjaSedang, self.terjualBanyak)
        self.z7 = 4000000 + (self.R7 * 300000)

        self.R8 = min(self.masaKerjaLama, self.terjualSedikit)
        self.z8 = 4500000 + (self.R8 * 300000)

        self.R9 = min(self.masaKerjaLama, self.terjualSedang)
        self.z9 = 5000000 + (self.R9 * 300000)

        self.R10 = min(self.masaKerjaLama, self.terjualBanyak)
        self.z10 = 6000000 + (self.R10 * 300000)

        # Menghitung nilai bonus
        # Menjumlahkan (Ri) dan (Zi)
        self.total_RiZi = (self.R1 * self.z1) + (self.R2 * self.z2) + (self.R3 * self.z3) + \
                          (self.R4 * self.z4) + (self.R5 * self.z5) + (self.R6 * self.z6) + \
                          (self.R7 * self.z7) + (self.R8 * self.z8) + (self.R9 * self.z9) + \
                          (self.R10 * self.z10) 

        # Menjumlahkan seluruh (Ri)
        self.total_R = self.R1 + self.R2 + self.R3 + self.R4 + self.R5 + self.R6 + self.R7 + self.R8 + self.R9 + self.R10 
        self.nilai_z = self.total_RiZi / self.total_R

        self.hitungBonus()

    def hitungBonus(self):
        self.bonus = self.nilai_z

        if self.bonus <= 300000:
            self.bonusSedikit = 1
        elif 300000 < self.bonus <= 2000000:
            self.bonusSedikit = (2000000 - self.bonus) / (2000000 - 300000)
        else:
            self.bonusSedikit = 0
            
        if self.bonus <= 300000:
            self.bonusSedang = 1
        elif 300000 < self.bonus <= 2000000:
            self.bonusSedang = (2000000 - self.bonus) / (2000000 - 300000)
        else:
            self.bonusSedang = 0

        if self.bonus <= 300000:
            self.bonusBanyak = 0
        elif 300000 < self.bonus <= 20000000:
            self.bonusBanyak = (self.bonus - 300000) / (2000000 - 300000)
        else:
            self.bonusBanyak = 1

        return format(self.bonus, '.2f')

    def displayMasaKerja(self):
        if self.masaKerjaBaru != 0:
            msg = "Magang ({})".format("%.2f" % self.masaKerjaMagang)
            return msg
        elif self.masaKerjaBaru != 0:
            msg = "Baru ({})".format("%.2f" % self.masaKerjaBaru)
            return msg
        elif self.masaKerjaSedang != 0:
            msg = "Sedang ({})".format("%.2f" % self.masaKerjaSedang)
            return msg
        elif self.masaKerjaLama != 0:
            msg = "Lama ({})".format("%.2f" % self.masaKerjaLama)
            return msg

    def displayProdukTerjual(self):
        if self.terjualSedikit != 0:
            msg = "Sedikit ({})".format("%.2f" % self.terjualSedikit)
            return msg
        elif self.terjualSedang != 0:
            msg = "Sedang ({})".format("%.2f" % self.terjualSedang)
            return msg
        elif self.terjualBanyak != 0:
            msg = "Banyak ({})".format("%.2f" % self.terjualBanyak)
            return msg

    def displayBonus(self):
        if self.bonusSedikit != 0:
            msg = "Sedikit ({})".format("%.2f" % self.bonusSedikit)
            return msg
        elif self.bonusSedikit != 0:
            msg = "Sedang ({})".format("%.2f" % self.bonusSedang)
            return msg
        elif self.bonusBanyak != 0:
            msg = "Banyak ({})".format("%.2f" % self.bonusBanyak)
            return msg