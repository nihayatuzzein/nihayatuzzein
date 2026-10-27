
nama = input("masukkan nama :")
kelas = input("kelas :")

nilai_a = int(input("Masukkan Nilai algoritma:"))
nilai_b = int(input("Masukkan Nilai agama:"))
nilai_c = int(input("Masukkan Nilai basisdata:"))
nilai_d = int(input("Masukkan Nilai bahasa inggris:"))
nilai_e = int(input("Masukkan Nilai logika informatika:"))
nilai_f = int(input("Masukkan Nilai bahasa indonesia:"))
nilai_g = int(input("Masukkan Nilai pancasila:"))

rata_rata = (nilai_a + nilai_b + nilai_c + nilai_d + nilai_e + nilai_f + nilai_g) / 7
print(rata_rata) 

# penentuan lulus atau tidak
if rata_rata >=80 and rata_rata <=100:
    # kondisi jika terprnuhi 
    # maka
    print ("nilai : a")
elif rata_rata >=70 and rata_rata <=80:
    print("nilai:b")
elif rata_rata >=50 and rata_rata <=70:
    print("nilai:c")
elif rata_rata >=70 and rata_rata <=80:
    print("nilai:d")
else:
    # cukup menampilkan hasil
    # maka
    print("Nilai : E")


 