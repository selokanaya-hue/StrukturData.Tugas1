# Project 2: Data Mahasiswa 2D (Array 2D)
# Dibuat untuk Tugas Struktur Data Pertemuan 2

def jalankan_project2():
    print("\n=== PROGRAM DATA NILAI MAHASISWA (ARRAY 2D) ===")
    
    # Validasi input jumlah mahasiswa dan mata kuliah
    try:
        jml_mhs = int(input("Masukkan jumlah mahasiswa (maks. 10): "))
        jml_mk = int(input("Masukkan jumlah mata kuliah (maks. 5): "))
        
        if jml_mhs > 10 or jml_mk > 5:
            print("Peringatan: Jumlah mahasiswa maksimal 10 dan mata kuliah maksimal 5!")
            return
    except ValueError:
        print("Input harus berupa angka!")
        return
    
    # Inisialisasi array 1D untuk nama dan array 2D untuk nilai
    nama_mhs = []
    nama_mk = []
    
    # Input nama-nama mata kuliah
    print("\n--- Input Nama Mata Kuliah ---")
    for j in range(jml_mk):
        mk = input(f"Masukkan nama mata kuliah ke-{j+1}: ")
        nama_mk.append(mk)
        
    # Input data mahasiswa dan nilai setiap mata kuliah (Array 2D)
    # Konsep Array 2D di Python: list di dalam list (nilai_2d[baris][kolom])
    nilai_2d = []
    for i in range(jml_mhs):
        print(f"\nMahasiswa ke-{i+1}")
        nama = input("Masukkan nama mahasiswa: ")
        nama_mhs.append(nama)
        
        baris_nilai = []
        for j in range(jml_mk):
            nilai = float(input(f"  Masukkan nilai untuk matkul {nama_mk[j]}: "))
            baris_nilai.append(nilai)
        nilai_2d.append(baris_nilai) # Memasukkan baris nilai ke array 2D
        
    # Tampilkan Tabel Data Nilai & Rata-rata per Mahasiswa
    print("\n" + "="*70)
    print("=== TABEL DATA NILAI MAHASISWA (ARRAY 2D) ===")
    print("="*70)
    
    # Membuat header tabel dinamis
    header = f"{'No':<3} | {'Nama':<12}"
    for mk in nama_mk:
        header += f" | {mk:<12}"
    header += f" | {'Rata-rata':<8}"
    print(header)
    print("-" * len(header))
    
    # Menampilkan isi data dari array 2D dan menghitung rata-rata mahasiswa
    for i in range(jml_mhs):
        total_nilai = sum(nilai_2d[i])
        rata_rata = total_nilai / jml_mk
        
        baris = f"{i+1:<3} | {nama_mhs[i]:<12}"
        for j in range(jml_mk):
            baris += f" | {nilai_2d[i][j]:<12.1f}"
        baris += f" | {rata_rata:<8.1f}"
        print(baris)
    print("-" * len(header))
    
    # Mencari Nilai Tertinggi & Terendah Tiap Mata Kuliah (Kolom dalam Array 2D)
    print("\n--- Analisis Nilai per Mata Kuliah ---")
    
    print("Nilai Tertinggi tiap mata kuliah:")
    for j in range(jml_mk):
        # Mengambil nilai berdasarkan kolom (mata kuliah yang sama dari setiap mahasiswa)
        kolom_nilai = [nilai_2d[i][j] for i in range(jml_mhs)]
        maks = max(kolom_nilai)
        print(f" - {nama_mk[j]} : {maks}")
        
    print("\nNilai Terendah tiap mata kuliah:")
    for j in range(jml_mk):
        kolom_nilai = [nilai_2d[i][j] for i in range(jml_mhs)]
        min_val = min(kolom_nilai)
        print(f" - {nama_mk[j]} : {min_val}")

# Menjalankan fungsi utama
if __name__ == "__main__":
    jalankan_project2()