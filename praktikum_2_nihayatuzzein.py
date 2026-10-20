tugas = float(input("Nilai tugas : "))
uts = float(input("Nilai UTS   : "))
uas = float(input("Nilai UAS   : "))
kehadiran = float(input("Kehadiran   : "))

nilai_akhir = round((0.20 * tugas) + (0.30 * uts) + (0.50 * uas), 2)

lulus = nilai_akhir >= 75 and kehadiran >= 80
predikat = nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0

if not lulus:
    status = "BELUM LULUS"
elif predikat:
    status = "LULUS DENGAN PREDIKAT"
else:
    status = "LULUS"

print()
print("Nilai Akhir :", nilai_akhir)
print("Status      :", status)