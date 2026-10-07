def hitung_defect_rate(dihasilkan, reject):
    return reject * 100 / dihasilkan

def tentukan_status(rate):
    if rate > 5:
       return "BAHAYA"
    elif rate > 2:
       return "PERHATIAN"
    else:
       return "AMAN"

data = []
jumlah = int(input("jumlah mesin: "))

for i in range(1, jumlah + 1):
    nama = input("nama mesin: ")
    dihasilkan = int(input("jumlah dihasilkan: "))
    reject = int(input("jumlah reject: "))
    if dihasilkan > 0:
        data.append({"mesin": nama, "dihasilkan": dihasilkan, "reject": reject})
    else:
        print("dihasilkan harus lebih dari 0, mesin dilewati")

print({'mesin': 'raptor1', 'dihasilkan': 500, 'reject': 12}, {'mesin': 'raptor2', 'dihasilkan': 450, 'reject': 30}, {'mesin': 'raptor3', 'dihasilkan': 400, 'reject': 5})

total_dihasilkan = 0
total_reject = 0

for item in data:
    rate = hitung_defect_rate(item["dihasilkan"], item["reject"])
    print(item["mesin"], round(rate, 1), "%", tentukan_status(rate))
    total_dihasilkan = total_dihasilkan + item["dihasilkan"]
    total_reject = total_reject + item["reject"]

rate_total = hitung_defect_rate(total_dihasilkan, total_reject)
print("Keseluruhan:", round(rate_total, 1), "%", tentukan_status(rate_total))
