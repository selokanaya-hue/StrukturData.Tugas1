# Project 1: Data Nilai Mahasiswa (Array 1D)
# Dibuat untuk Tugas Struktur Data Pertemuan 2

daftar_nama = []
daftar_nilai = []
MAKS_MAHASISWA = 10

def tampilkan_menu():
    print("\n=== MENU DATA NILAI MAHASISWA ===")
    print("1. Input Data")
    print("2. Tampilkan Data")
    print("3. Nilai Tertinggi & Terendah")
    print("4. Rata-rata")
    print("5. Ubah Data")
    print("6. Hapus Data")
    print("7. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-7): ")
    
    if pilihan == '1':
        if len(daftar_nama) >= MAKS_MAHASISWA:
            print(f"Maaf, kapasitas maksimal sudah penuh ({MAKS_MAHASISWA} mahasiswa).")
            continue
            
        try:
            jml = int(input(f"Masukkan jumlah mahasiswa yang ingin ditambahkan (sisa {MAKS_MAHASISWA - len(daftar_nama)}): "))
            if len(daftar_nama) + jml > MAKS_MAHASISWA:
                print("Jumlah melebihi batas maksimal!")
                continue
                
            for i in range(jml):
                print(f"\nMahasiswa ke-{len(daftar_nama) + 1}")
                nama = input("Masukkan nama mahasiswa: ")
                nilai = float(input("Masukkan nilai mahasiswa: "))
                daftar_nama.append(nama)
                daftar_nilai.append(nilai)
            print("Data berhasil ditambahkan!")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            
    elif pilihan == '2':
        if not daftar_nama:
            print("\nBelum ada data mahasiswa.")
        else:
            print("\n--- DAFTAR NILAI MAHASISWA ---")
            print(f"{'No':<4} | {'Nama':<15} | {'Nilai':<5}")
            print("-" * 32)
            for i in range(len(daftar_nama)):
                print(f"{i+1:<4} | {daftar_nama[i]:<15} | {daftar_nilai[i]:<5}")
                
    elif pilihan == '3':
        if not daftar_nilai:
            print("\nBelum ada data nilai.")
        else:
            max_nilai = max(daftar_nilai)
            min_nilai = min(daftar_nilai)
            idx_max = daftar_nilai.index(max_nilai)
            idx_min = daftar_nilai.index(min_nilai)
            print(f"\nNilai Tertinggi: {max_nilai} (oleh {daftar_nama[idx_max]})")
            print(f"Nilai Terendah : {min_nilai} (oleh {daftar_nama[idx_min]})")
            
    elif pilihan == '4':
        if not daftar_nilai:
            print("\nBelum ada data nilai.")
        else:
            rata_rata = sum(daftar_nilai) / len(daftar_nilai)
            print(f"\nRata-rata nilai kelas adalah: {rata_rata:.2f}")
            
    elif pilihan == '5':
        if not daftar_nama:
            print("\nBelum ada data untuk diubah.")
        else:
            print("\n1. Ubah berdasarkan Index")
            print("2. Ubah berdasarkan Nama")
            sub_pilih = input("Pilih metode ubah (1/2): ")
            
            if sub_pilih == '1':
                try:
                    idx = int(input("Masukkan nomor/index mahasiswa (1 s.d. len): ")) - 1
                    if 0 <= idx < len(daftar_nama):
                        daftar_nama[idx] = input("Masukkan nama baru: ")
                        daftar_nilai[idx] = float(input("Masukkan nilai baru: "))
                        print("Data berhasil diubah!")
                    else:
                        print("Index tidak ditemukan.")
                except ValueError:
                    print("Input harus berupa angka!")
            elif sub_pilih == '2':
                cari_nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
                if cari_nama in daftar_nama:
                    idx = daftar_nama.index(cari_nama)
                    daftar_nama[idx] = input("Masukkan nama baru: ")
                    daftar_nilai[idx] = float(input("Masukkan nilai baru: "))
                    print("Data berhasil diubah!")
                else:
                    print("Nama tidak ditemukan.")
                    
    elif pilihan == '6':
        if not daftar_nama:
            print("\nBelum ada data untuk dihapus.")
        else:
            print("\n1. Hapus berdasarkan Index")
            print("2. Hapus berdasarkan Nama")
            sub_pilih = input("Pilih metode hapus (1/2): ")
            
            if sub_pilih == '1':
                try:
                    idx = int(input("Masukkan nomor/index mahasiswa yang akan dihapus: ")) - 1
                    if 0 <= idx < len(daftar_nama):
                        nama_terhapus = daftar_nama.pop(idx)
                        daftar_nilai.pop(idx)
                        print(f"Data {nama_terhapus} berhasil dihapus!")
                    else:
                        print("Index tidak valid.")
                except ValueError:
                    print("Input harus berupa angka!")
            elif sub_pilih == '2':
                cari_nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
                if cari_nama in daftar_nama:
                    idx = daftar_nama.index(cari_nama)
                    daftar_nama.pop(idx)
                    daftar_nilai.pop(idx)
                    print(f"Data {cari_nama} berhasil dihapus!")
                else:
                    print("Nama tidak ditemukan.")
                    
    elif pilihan == '7':
        print("\nKeluar dari program. Terima kasih!")
        break
    else:
        print("\nPilihan tidak valid. Silakan pilih menu 1-7.")