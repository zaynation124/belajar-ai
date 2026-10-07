def hitung_defect_rate(dihasilkan, reject):
   return reject * 100 / dihasilkan

def tentukan_status(rate):
  if rate > 5:
    return "BAHAYA"
  elif rate > 2:
    return "PERHATIAN"
  else :
    return "AMAN"

data_produksi = [
    {"mesin": "M1", "dihasilkan": 500, "reject": 12},
    {"mesin": "M2", "dihasilkan": 450, "reject": 30},
    {"mesin": "M3", "dihasilkan": 400, "reject": 5},
 ]

for item in data_produksi:
   rate = hitung_defect_rate(item["dihasilkan"], item["reject"])
   print(item["mesin"], round(rate, 1), "%", tentukan_status (rate))

