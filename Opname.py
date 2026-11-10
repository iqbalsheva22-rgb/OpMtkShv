print("=== SISTEM CEK PASIEN & TAGIHAN OPNAME ===")

nama_pasien = input("Masukkan nama pasien: ")
hari_rawat = int(input("Sudah berapa hari dirawat di RS?: "))
suhu_badan = float(input("Masukkan suhu badan pasien (°C): "))
tingkat_sesak = input("Bagaimana kondisi napasnya? (sesak berat / normal): ").lower()
nafsu_makan = input("Apakah pasien sudah mau makan banyak? (ya / tidak): ").lower()

print("\n=== PILIHAN KELAS KAMAR OPNAME ===")
print("- Kelas 3 (Rp 200.000 / hari)")
print("- Kelas 2(Rp 450.000 / hari)")
print("- Kelas 1 (Rp 800.000 / hari)")
print("- VIP     (Rp 1.500.000 / hari)")
pilihan_kamar = input("Masukkan kelas kamar pasien (3 / 2 / 1 / vip): ").lower()

print(f"\n=== KONDISI & TAGIHAN {nama_pasien.upper()} ===")
if (tingkat_sesak == "sesak berat" and suhu_badan >= 38.5) or (tingkat_sesak == "sesak berat"):
    print("-> Kondisi pasien drop! Segera pindahkan ke ruang ICU.")
    print("-> [INFO] Sistem tagihan ditangguhkan sampai kondisi stabil.")

elif hari_rawat >= 3 and suhu_badan <= 37.5 and tingkat_sesak == "normal" and not (nafsu_makan == "tidak"):
    print("-> Pasien sudah sehat dan diizinkan pulang hari ini.")
                
    if pilihan_kamar == "3":
        tarif_per_hari = 200000
    elif pilihan_kamar == "2":
        tarif_per_hari = 450000
    elif pilihan_kamar == "1":
        tarif_per_hari = 800000
    elif pilihan_kamar == "vip":
        tarif_per_hari = 1500000
    else:
        tarif_per_hari = 200000
                                                                                    
    biaya_kamar = hari_rawat * tarif_per_hari
    biaya_dokter_obat = hari_rawat * 150000 
    total_tagihan = biaya_kamar + biaya_dokter_obat
    
    print("\n================ RIANCIAN NOTA PEMBAYARAN ================")
    print(f" Total Lama Rawat   : {hari_rawat} Hari")
    print(f" Tarif Kamar        : Rp {biaya_kamar:,}")
    print(f" Biaya Dokter & Obat: Rp {biaya_dokter_obat:,}")
    print(f" Total yang Dibayar : Rp {total_tagihan:,}")
    print("============================================================")
    
elif suhu_badan > 37.5 or nafsu_makan == "tidak":
    print("-> Pasien belum stabil. Lanjutkan opname.")
    print("-> [INFO] Tagihan belum dapat dipastikan.")

else:
    print("-> Kondisi pasien tidak dapat dipastikan, tunggu visit dokter selanjutnya.")
