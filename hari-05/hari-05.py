skor = int(input("Masukkan skor inspeksi (0-100): "))

if skor >= 90:
    print("Grade A")
elif skor >= 75:
    print("Grade B")
elif skor >= 60:
    print("Grade C")
else:
    print("Reject")

