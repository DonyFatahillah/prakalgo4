
while True:
    print("\n \n")

    print("@@@@   @@@@@   @@  @  @   @")
    print("@   @  @   @   @ @ @   @ @")
    print("@   @  @   @   @  @@    @")
    print("@@@@   @@@@@   @   @    @")

    print("\n \n")

    print("---PROGRAM KONVERSI BILANGAN---")
    print("1.) Angka Ke Biner >> ")
    print("2.) Biner Ke Angka >> ")
    print("3.) Exit")
    opsi = input("Opsi : ")


    if opsi.isdigit() and opsi == "1":
        angka = int(input("Masukan Angka : "))

        print(f"{angka} ke Biner adalah {format(angka, 'b')}")
        continue

    elif opsi.isdigit() and opsi == "2":
        biner = input("Masukan Angka Biner : ")

        binerInt = int(biner, 2)

        print(f"{biner} ke Angka adalah {int(binerInt)} ")
        continue
    elif opsi.isdigit() and opsi == "3":
        print("Terimakasih Sudah Menggunakan Program ini <3 *muach")
        break
    else:
        print("Opsi tidak valid")
        continue
