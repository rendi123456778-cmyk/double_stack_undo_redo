#Kita buat array untuk menampung undo dan redo nya 
undo_stack = []
redo_stack = []
#kita buat kan satu buah variabel untuk menampung tex yang akan di ketik nanti nya 
teks = ""

while True:
    # kita buat kan menu
    print("\n=== MENU UNDO DAN REDO ===")
    print("1. Tambah teks")
    print("2. Undo")
    print("3. Redo")
    print("4. Lihat teks")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")
    # Tmbah texs
    if pilihan == "1":
        # melakukan peyimpanan teks sebelumnya ke undo stack
        undo_stack.append(teks)
        teks_baru = input("Masukkan teks: ")
        teks = teks_baru
        # menghapus riwayat redo karena ada perubahan baru
        redo_stack.clear()
        print("Teks berhasil diubah!")
  # undo
    elif pilihan == "2":
        if len(undo_stack) > 0:
            # meyimpan kondisi sekarang ke redo stack
            redo_stack.append(teks)
            # mengembalikan teks sebelumnya
            teks = undo_stack.pop()
            print("Undo berhasil!")
        else:
            print("Tidak ada perubahan untuk di-undo.")
    #redo
    elif pilihan == "3":
        if len(redo_stack) > 0:
            # menyimpa kondisi sekarang ke undo stack
            undo_stack.append(teks)
            # mengembalikan teks yang dibatalkan
            teks = redo_stack.pop()
            print("Redo berhasil!")
        else:
            print("Tidak ada perubahan untuk di-redo.")
  # menampilkan text
    elif pilihan == "4":
        print("Teks saat ini:", teks)
  # keluar dari perogram 
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
