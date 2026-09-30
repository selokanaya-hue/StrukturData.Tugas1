# Project 3: Manajemen Data Barang (Array 1D)
# Dibuat untuk Tugas Struktur Data Pertemuan 2

nama_barang = []
harga_barang = []
MAKS_BARANG = 20  # Batas maksimal barang sesuai ketentuan tugas

def menu_barang():
    print("\n=== MENU DATA BARANG ===")
    print("1. Input Data")
    print("2. Tampilkan Data")
    print("3. Cari Barang")
    print("4. Urutkan Harga")
    print("5. Hapus Data")
    print("6. Keluar")

while True:
    menu_barang()
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == '1':
        # 1. Input Data Barang
        if len(nama_barang) >= MAKS_BARANG:
            print(f"Maaf, kapasitas maksimal barang sudah penuh ({MAKS_BARANG} barang).")
            continue
            
        try:
            jml = int(input(f"Masukkan jumlah barang yang ingin diinput (sisa kapasitas: {MAKS_BARANG - len(nama_barang)}): "))
            if len(nama_barang) + jml > MAKS_BARANG:
                print("Jumlah melebihi batas maksimal kapasitas penyimpanan!")
                continue
                
            for i in range(jml):
                print(f"\nBarang ke-{len(nama_barang) + 1}")
                nama = input("Masukkan nama barang: ")
                harga = float(input("Masukkan harga barang: "))
                nama_barang.append(nama)
                harga_barang.append(harga)
            print("Data barang berhasil ditambahkan!")
        except ValueError:
            print("Input tidak valid! Pastikan harga berupa angka.")
            
    elif pilihan == '2':
        # 2. Tampilkan Seluruh Data Barang
        if not nama_barang:
            print("\nBelum ada data barang.")
        else:
            print("\n" + "="*45)
            print("=== DAFTAR INVENTARIS BARANG ===")
            print("="*45)
            print(f"{'No':<4} | {'Nama Barang':<20} | {'Harga':<12}")
            print("-" * 45)
            for i in range(len(nama_barang)):
                print(f"{i+1:<4} | {nama_barang[i]:<20} | Rp {harga_barang[i]:<10,.2f}")
            print("-" * 45)
                
    elif pilihan == '3':
        # 3. Cari Barang Berdasarkan Nama
        if not nama_barang:
            print("\nData barang kosong.")
        else:
            cari = input("Masukkan nama barang yang ingin dicari: ").lower()
            ditemukan = False
            print("\nHasil Pencarian:")
            for i in range(len(nama_barang)):
                if cari in nama_barang[i].lower():
                    print(f" - Ditemukan: {nama_barang[i]} seharga Rp {harga_barang[i]:,.2f} (Index ke-{i+1})")
                    ditemukan = True
            if not ditemukan:
                print("Barang yang dicari tidak ditemukan.")
                
    elif pilihan == '4':
        # 4. Urutkan Harga Berdasarkan Ascending (Termurah ke Termahal)
        if not nama_barang:
            print("\nData barang kosong untuk diurutkan.")
        else:
            # Algoritma Bubble Sort sederhana untuk mengurutkan harga beserta namanya agar tetap sinkron
            n = len(nama_barang)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if harga_barang[j] > harga_barang[j + 1]:
                        # Tukar posisi harga
                        harga_barang[j], harga_barang[j + 1] = harga_barang[j + 1], harga_barang[j]
                        # Tukar posisi nama agar mengikuti harga
                        nama_barang[j], nama_barang[j + 1] = nama_barang[j + 1], nama_barang[j]
            print("\nData barang berhasil diurutkan berdasarkan harga (Termurah ke Termahal)!")
            
    elif pilihan == '5':
        # 5. Hapus Data Berdasarkan Index
        if not nama_barang:
            print("\nBelum ada data barang untuk dihapus.")
        else:
            try:
                idx = int(input("Masukkan nomor/index barang yang akan dihapus: ")) - 1
                if 0 <= idx < len(nama_barang):
                    n_hapus = nama_barang.pop(idx)
                    harga_barang.pop(idx)
                    print(f"Barang '{n_hapus}' berhasil dihapus dari sistem!")
                else:
                    print("Nomor index barang tidak valid.")
            except ValueError:
                print("Harap masukkan angka index yang benar!")
                
    elif pilihan == '6':
        print("\nKeluar dari program Manajemen Data Barang. Terima kasih!")
        break
    else:
        print("\nPilihan menu tidak valid. Silakan masukkan nomor 1 sampai 6.")