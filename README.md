# dokumentasi_pertemuan13.py

print("""
# Pertemuan 13 - Debugging dan Testing

Nama  : Vanisya Nur Khalimah
NIM   : 2225520201
Kelas : S1 Pendidikan Matematika

## Kasus
Program yang diuji adalah program perhitungan rata-rata nilai mahasiswa.
Pada versi awal terdapat bug yang menyebabkan hasil perhitungan tidak sesuai
karena jumlah data tidak dihitung dengan benar.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|----|-------|----------|------------|--------|
| TC01 | [80, 90, 100] | 90.0 | 270 | Gagal |
| TC02 | [70, 80] | 75.0 | 150 | Gagal |
| TC03 | [100] | 100.0 | 100 | Gagal |

## Bug Report

Gejala:
- Program menampilkan jumlah nilai, bukan rata-rata nilai.

Lokasi:
- Fungsi hitung_rata_rata().

Akar Penyebab:
- Program menjumlahkan seluruh nilai tetapi tidak membaginya dengan banyak data.

Perbaikan:
- Menambahkan operasi pembagian:
  rata_rata = total / len(data)

## Retest

| ID | Expected | Actual Setelah Perbaikan | Status |
|----|----------|-------------------------|--------|
| TC01 | 90.0 | 90.0 | Berhasil |
| TC02 | 75.0 | 75.0 | Berhasil |
| TC03 | 100.0 | 100.0 | Berhasil |

## Cara Menjalankan

python3 praktik/praktik_4_debugging.py

## Riwayat Git

Sebelum Perbaikan:
git add .
git commit -m "Menambahkan program rata-rata nilai"

Sesudah Perbaikan:
git add .
git commit -m "Memperbaiki bug perhitungan rata-rata"

## Refleksi

Teknik debugging yang paling membantu adalah penggunaan print() untuk
melacak nilai variabel pada setiap tahap perhitungan. Teknik ini membantu
menemukan bahwa program hanya menghitung total nilai tanpa membaginya
dengan jumlah data sehingga akar penyebab bug dapat diketahui dengan cepat.
""")
