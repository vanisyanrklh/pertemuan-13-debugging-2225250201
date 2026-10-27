def status_lulus(nilai):
    # Memperbaiki operator pembanding dari '>' menjadi '>=' 
    # agar nilai 60 ikut masuk ke dalam kategori lulus
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

# Rancangan test case: 59, 60, dan 61
test_cases = [59, 60, 61]

print("=== HASIL PENGUJIAN KODE (TEST CASE) ===")
for nilai in test_cases:
    hasil = status_lulus(nilai)
    print(f"Nilai {nilai} -> {hasil}")