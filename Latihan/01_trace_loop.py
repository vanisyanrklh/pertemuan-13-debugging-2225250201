# ==============================================================================
# PREDIKSI OUTPUT SEBELUM PROGRAM DIJALANKAN
# ==============================================================================
# Perulangan range(1, 5) mencakup nilai i = 1, 2, 3, 4.
# Kode ini menghitung perkalian beruntun (faktorial 4!):
#  - Iterasi 1: total = 1 * 1 = 1
#  - Iterasi 2: total = 1 * 2 = 2
#  - Iterasi 3: total = 2 * 3 = 6
#  - Iterasi 4: total = 6 * 4 = 24
# PREDIKSI OUTPUT AKHIR: 24
# ==============================================================================

print("=== TABEL TRACING PERULANGAN ===")
print(f"{'Iterasi':<10} | {'Nilai i':<10} | {'Perhitungan (total * i)':<25} | {'Total Terbaru':<15}")
print("-" * 70)

# Inisialisasi awal
total = 1
print(f"{'Awal':<10} | {'-':<10} | {'Nilai Awal':<25} | {total:<15}")

# Perulangan dan Tracing
iterasi = 1
for i in range(1, 5):
    total_lama = total
    total = total * i
    ekspresi = f"{total_lama} * {i}"
    print(f"{iterasi:<10} | {i:<10} | {ekspresi:<25} | {total:<15}")
    iterasi += 1

print("-" * 70)
print(f"\nHasil Output (print(total)): {total}")
