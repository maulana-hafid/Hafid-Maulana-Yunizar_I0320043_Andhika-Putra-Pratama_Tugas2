print("Tugas 1")
print("Perhitungan cepat")
print("                 ")

print("Menghitung luas lingkaran" )
r = float(input("Masukkan nilai jari-jari: "))
phi = 3.14
luas_lingkaran = phi * r * r
print("Luas lingkaran adalah: ", luas_lingkaran)

print("                ")
print("Menghitung luas persegi panjang", )
panjang = float(input("Masukkan nilai panjangnya: "))
lebar = float(input("Masukkan nilai lebarnya: "))
luas_persegi_panjang = panjang * lebar
print("Luas persegi panjang adalah: ", luas_persegi_panjang)

print("                     ")
print("Menghitung luas kubus")
s = float(input("Masukkan nilai rusuknya: "))
luas_kubus = 6 * s * s
print("Luas Kubus adalah: ", luas_kubus)

print("                     ")
print("Mengubah celcius ke farenheit")
F = float(input("Masukkan suhu awal(farenheit): "))
C = 5 / 9 * (F-32)
print("Suhu farenheit", F, "F")
print("Suhu Celcius", C, "C")

print("                      ")
print("Mengubah reamur ke kelvin")
R = float(input("Masukkan suhu awal(reamur): "))
K = 5 / 4 * R + 273
print("Suhu reamur", R, "R")
print("Suhu kelvin", K, "K")