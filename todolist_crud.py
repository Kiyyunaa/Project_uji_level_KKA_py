import time


daftar_tugas = []
id_berikutnya = 1

def tampilkan_menu():
    print("\n===== APLIKASI TO DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")


def tambah_tugas():
    global id_berikutnya
    print("\nTambah Tugas Baru")

    nama = input("Nama tugas: ").strip()

    if nama == "":
        print("\nNama tugas tidak boleh kosong!")
        time.sleep(1)
        return

    daftar_tugas.append({'id': id_berikutnya, 'nama': nama, 'selesai': False})
    id_berikutnya += 1

    print("\nMemproses...")
    time.sleep(1)
    print(f"Tugas '{nama}' berhasil ditambahkan!")
    time.sleep(1)

def lihat_tugas():
    print("\nDaftar Tugas")

    if len(daftar_tugas) == 0:
        print("Belum ada tugas.")
        time.sleep(1)
        return

    print("-" * 35)
    for i, tugas in enumerate(daftar_tugas, 1):
        status = "Selesai" if tugas['selesai'] else "Belum"
        print(f"{i}. {tugas['nama']} [{status}]")
    print("-" * 35)
    time.sleep(1)


def tandai_selesai():
    print("\nTandai Tugas Selesai")

    belum = [t for t in daftar_tugas if not t['selesai']]

    if len(belum) == 0:
        print("Semua tugas sudah selesai!")
        time.sleep(1)
        return

    for i, tugas in enumerate(belum, 1):
        print(f"{i}. {tugas['nama']}")

    pilihan = input("Nomor tugas yang selesai: ").strip()

    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(belum):
        print("\nNomor tidak valid!")
        time.sleep(1)
        return

    tugas_dipilih = belum[int(pilihan) - 1]
    for t in daftar_tugas:
        if t['id'] == tugas_dipilih['id']:
            t['selesai'] = True
            break

    print("\nMemproses...")
    time.sleep(1)
    print(f"Tugas '{tugas_dipilih['nama']}' ditandai selesai!")
    time.sleep(1)


def hapus_tugas():
    print("\nHapus Tugas")

    if len(daftar_tugas) == 0:
        print("Belum ada tugas.")
        time.sleep(1)
        return

    for i, tugas in enumerate(daftar_tugas, 1):
        status = "Selesai" if tugas['selesai'] else "Belum"
        print(f"{i}. {tugas['nama']} [{status}]")

    pilihan = input("Nomor tugas yang dihapus: ").strip()

    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(daftar_tugas):
        print("\nNomor tidak valid!")
        time.sleep(1)
        return

    tugas_dihapus = daftar_tugas[int(pilihan) - 1]
    konfirmasi = input(f"Yakin hapus '{tugas_dihapus['nama']}' ? (ya/tidak): ").strip().lower()

    if konfirmasi == "ya":
        daftar_tugas.remove(tugas_dihapus)
        print("\nMemproses...")
        time.sleep(1)
        print("Tugas berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

    time.sleep(1)


def main():
    print("\n Selamat Datang di Aplikasi To Do List")

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan Pilihan: ")

        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            tandai_selesai()
        elif pilihan == "4":
            hapus_tugas()
        elif pilihan == "5":
            print("\nTerimakasih telah menggunakan aplikasi ini")
            time.sleep(1)
            break
        else:
            print("\nPilihan tidak valid")

main()