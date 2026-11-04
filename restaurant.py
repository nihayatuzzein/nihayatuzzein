print("=========================================")
print("RESTORAN HAYA LEZAT DAN BERGIZI")
print("=========================================")

total = 0
rincian = ""
pilihan = -1

while pilihan != 0:
    print("")
    print("----------- MENU MAKANAN -----------")
    print("1. Nasi Goreng  - Rp25000")
    print("2. Mie Ayam     - Rp15000")
    print("3. Ayam Geprek  - Rp20000")
    print("4. Sate Ayam    - Rp30000")
    print("5. Bakso        - Rp18000")
    print("0. Selesai memilih")
    print("------------------------------------")

    pilihan = int(input("Pilih menu (0-5): "))

    if pilihan == 0:
        print("Selesai memilih.")
    elif pilihan == 1:
        jumlah = int(input("Masukkan jumlah pesanan: "))
        subtotal = 25000 * jumlah
        total = total + subtotal
        rincian = rincian + "Nasi Goreng x " + str(jumlah) + " = Rp" + str(subtotal) + "\n"
    elif pilihan == 2:
        jumlah = int(input("Masukkan jumlah pesanan: "))
        subtotal = 15000 * jumlah
        total = total + subtotal
        rincian = rincian + "Mie Ayam x " + str(jumlah) + " = Rp" + str(subtotal) + "\n"
    elif pilihan == 3:
        jumlah = int(input("Masukkan jumlah pesanan: "))
        subtotal = 20000 * jumlah
        total = total + subtotal
        rincian = rincian + "Ayam Geprek x " + str(jumlah) + " = Rp" + str(subtotal) + "\n"
    elif pilihan == 4:
        jumlah = int(input("Masukkan jumlah pesanan: "))
        subtotal = 30000 * jumlah
        total = total + subtotal
        rincian = rincian + "Sate Ayam x " + str(jumlah) + " = Rp" + str(subtotal) + "\n"
    elif pilihan == 5:
        jumlah = int(input("Masukkan jumlah pesanan: "))
        subtotal = 18000 * jumlah
        total = total + subtotal
        rincian = rincian + "Bakso x " + str(jumlah) + " = Rp" + str(subtotal) + "\n"
    else:
        print("Menu tidak tersedia.")

if total > 200000:
    diskon = 20
else:
    diskon = 0

potongan = int(total * diskon / 100)
total_bayar = total - potongan

print("")
print("=========================================")
print("           STRUK PEMBAYARAN")
print("=========================================")

if rincian == "":
    print("Tidak ada pesanan.")
else:
    print(rincian)

print("-----------------------------------------")
print("Total Belanja : Rp" + str(total))
print("Diskon        : " + str(diskon) + "%")
print("Potongan      : Rp" + str(potongan))
print("Total Bayar   : Rp" + str(total_bayar))
print("=========================================")
print("Terima kasih telah berkunjung!")
print("=========================================")
