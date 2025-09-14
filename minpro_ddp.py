travel_log = []

while True:
    print("\n===== MENU TRAVEL LOG =====")
    print("1. Lihat Travel Log")
    print("2. Tambah Perjalanan")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":  # READ
        if not travel_log:
            print("Belum ada data perjalanan")
        else:
           print("\n===== DAFTAR TRAVEL LOG =====")
           data=travel_log[0]
           print ("Perjalanan 1")
           print ("Destinasi", travel_log[0][0])
           print ("Tanggal", travel_log[0][1])
           print ("Catatan", travel_log[0][2])
           print ("\nPerjalanan 2")
           print ("Destinasi", travel_log[1][0])
           print ("Tanggal", travel_log[1][1])
           print ("Catatan", travel_log[1][2])



    elif pilihan == "2":  # CREATE
        print("\n===== TAMBAH PERJALANAN =====")
        destinasi = input("Masukkan destinasi: ")
        tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
        catatan = input("Masukkan catatan: ")
        log = (destinasi, tanggal, catatan)
        travel_log.append(log)
        print("Perjalanan berhasil ditambahkan!")

    elif pilihan == "3":  # EXIT
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")