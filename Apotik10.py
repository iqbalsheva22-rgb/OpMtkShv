katalog_nama = [
    "Minyak Telon", "Paracetamol Sirup", "Vitamin C Anak", "Diapet Anak", "Promag Tablet",
    "Amoxicillin Kapsul", "Obat Batuk Dewasa", "Panadol Forte", "Obat Tidur (Resep)", "Suplemen Lansia"
]
katalog_usia = [0, 1, 2, 5, 12, 17, 17, 18, 21, 50]

print("=== DAFTAR OBAT APOTEK ===")
print("1. Minyak Telon (Min. 0 Tahun)")
print("2. Paracetamol Sirup (Min. 1 Tahun)")
print("3. Vitamin C Anak (Min. 2 Tahun)")
print("4. Diapet Anak (Min. 5 Tahun)")
print("5. Promag Tablet (Min. 12 Tahun)")
print("6. Amoxicillin Kapsul (Min. 17 Tahun)")
print("7. Obat Batuk Dewasa (Min. 17 Tahun)")
print("8. Panadol Forte (Min. 18 Tahun)")
print("9. Obat Tidur (Resep) (Min. 21 Tahun)")
print("10. Suplemen Lansia (Min. 50 Tahun)")

print("\n===============================")
pilih = int(input("Pilih nomor obat (1-10): "))
usia = int(input("Masukkan usia Anda (Tahun): "))


indeks = pilih - 1
nama_obat = katalog_nama[indeks]
usia_minimal = katalog_usia[indeks]

print(f"\n--- HASIL CEK IZIN BELI {nama_obat} ---")
if usia < usia_minimal:
    print(f"Ditolak! Usia anda kurang dari batas minimal {usia_minimal} tahun.")

elif usia > usia_minimal:
    print(f"Diizinkan! Usia anda memenuhi syarat perizinan konsumsi .")

elif usia == usia_minimal:
    print(f"Diizinkan! Usia anda memenuhi syarat perizinan konsumsi obat.")