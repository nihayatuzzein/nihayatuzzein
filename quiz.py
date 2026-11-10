print ("===PROGRAM REMEDIAL MAHASISWA===")

#Input nama mahasiswaa
nama = input("Masukkan Nama Mahasiswa: ")

#Menentukan target nilai
if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    target = 0

#Mengecek nama mahsiswa
if target == 0:
    print("Nama Mahasiswa Tidak Terdaftar")

else:
    print("Nama:", nama)
    print("Target nilai:", target)

    percobaan = 0
    lulus = False 

    # perulangan maksimal 3 kali
    while percobaan < 3 and lulus == False: 

        nilai =int(input("Masukkan Nilai Ujian: "))
        percobaan += 1

        # Mengecek nilai
        if nilai >= target:
            lulus = True
            print("Selamat,", nama,"Berhasil Lulus")
        else:
            print("Nilai Belum Mencapai Target.")
            print("Silahkan Mengikuti Remedial.")
    #Hasil Akhir
    if lulus == True:
        print(nama, "Berhasil Lulus Setelah", percobaan, "kali percobaan.")
    else:
        print(nama, "Tidak Lulus Setelah 3 Kali Percobaan.")