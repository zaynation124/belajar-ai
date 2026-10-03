for unit in range(1, 11):
    print("Inspeksi unit", unit)

total = 0
for unit in range(1, 6):
    skor = int(input("Skor unit " + str(unit) + ": "))
    total = total + skor
print("Rata-rata:", total / 5)

hitung = 3
while hitung > 0:
    print("Sisa", hitung)
    hitung = hitung - 1
print("Selesai")
