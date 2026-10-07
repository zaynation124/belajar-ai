# Kalkulator Manufaktur

Program Python untuk menghitung defect rate mesin produksi dan menentukan status mutunya.

## Problem
Tim produksi perlu tahu seberapa banyak produk cacat (reject) dari tiap mesin dan dari seluruh pabrik. Menghitungnya manual lambat dan mudah salah, terutama kalau mesinnya banyak.

## User
Operator atau staf kualitas yang ingin mengecek mutu produksi dengan cepat.

## Input
- Jumlah mesin
- Untuk tiap mesin: nama, jumlah yang dihasilkan, dan jumlah reject
- Mesin dengan jumlah dihasilkan 0 dilewati, karena tidak bisa dihitung

## Proses
1. Data tiap mesin disimpan dalam list berisi dictionary.
2. Defect rate dihitung dengan rumus reject x 100 / dihasilkan.
3. Status ditentukan dari rate: di atas 5% BAHAYA, di atas 2% PERHATIAN, selain itu AMAN.
4. Semua mesin dijumlahkan untuk mendapat defect rate keseluruhan.

## Output
Satu baris laporan per mesin (nama, defect rate, status), lalu satu baris defect rate keseluruhan beserta statusnya.

## Cara menjalankan
python3 kalkulator-mfg.py

## Contoh
Input: raptor1 (500, 12), raptor2 (450, 30), raptor3 (400, 5)

raptor1 2.4 % PERHATIAN
raptor2 6.7 % BAHAYA
raptor3 1.2 % AMAN
Keseluruhan: 3.5 % PERHATIAN
