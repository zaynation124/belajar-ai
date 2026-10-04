produksi = {"mesin": "M1", "operator": "budi", "dihasilkan": 500, "reject": 12}

print("Mesin:", produksi["mesin"])
rate = produksi["reject"] * 100 / produksi["dihasilkan"]
print("Defect rate:", rate, "%")

produksi["reject"] = 15
produksi["shift"] = "malam"
print(produksi)

