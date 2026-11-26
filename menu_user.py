import os
import inquirer
import pungsi as p

def menu_user():
    while p.loginuser:
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 44)
        print("=" * 16, "MENU USER", "=" * 17)
        print("=" * 44)
        jawab_menu = inquirer.prompt([
            inquirer.List(
                "pilihan",
                message="Masukkan Pilihan",
                choices=[
                    "1. Melihat Daftar Hero",
                    "2. Mencari Data Hero",
                    "3. Komparasi dan Rekomendasi Hero",
                    "4. Pilih Hero Favorit",
                    "5. Cek Komposisi Tim",
                    "6. Keluar",
                ],
            )
        ])
        if jawab_menu is None:
            p.loginuser = False
            break
        
        menu = jawab_menu["pilihan"]
        
        if "1." in menu:
            os.system("cls" if os.name == "nt" else "clear")
            p.tampilkan_seluruh_hero()
            print("=" * 44)
            jawab_kembali = inquirer.prompt([
                inquirer.List("kembali", message="Kembali ke menu?", choices=["Ya", "Tidak"])
            ])
            if jawab_kembali is None or jawab_kembali["kembali"] == "Tidak":
                p.loginuser = False
                break

        elif "2." in menu:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("=" * 22, "CARI DATA HERO", "=" * 22)
                jawab_role = inquirer.prompt([
                    inquirer.List(
                        "role",
                        message="Pilih Role Hero",
                        choices=list(p.role_valid) + ["All"],
                    )
                ])
                jawab_lane = inquirer.prompt([
                    inquirer.List(
                        "lane",
                        message="Pilih Lane Hero",
                        choices=list(p.lane_valid) + ["All"],
                    )
                ])

                p.tampilkan_hero_filter(jawab_role["role"], jawab_lane["lane"])
                print("=" * 44)
                jawab_aksi = inquirer.prompt([
                    inquirer.List(
                        "aksi",
                        message="Pilih tindakan",
                        choices=["Tetap di Pencarian (Cari Lagi)", "Kembali ke Menu User"],
                    )
                ])
                if jawab_aksi is None or jawab_aksi["aksi"] == "Kembali ke Menu User":
                    break

        elif "3." in menu:
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 10, "KOMPARASI DAN REKOMENDASI HERO", "=" * 10)
            hero1 = input("Masukkan nama hero pertama: ").strip()
            hero2 = input("Masukkan nama hero kedua: ").strip()
            print("=" * 52)
            p.bandingkan_hero(hero1, hero2)
            print("=" * 52)
            jawab_kembali = inquirer.prompt([
                inquirer.List("kembali", message="Kembali ke menu?", choices=["Ya", "Tidak"])
            ])
            if jawab_kembali is None or jawab_kembali["kembali"] == "Tidak":
                p.loginuser = False
                break

        elif "4." in menu:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print('='*44)
                print('='*11, 'DAFTAR HERO FAVORIT', '='*12)
                print('='*44)
                tanya_favorit = [
                    inquirer.List(
                        "pilihan",
                        message="Masukkan Pilihan",
                        choices=[
                            "1. Melihat Hero Favorit",
                            "2. Menambah Hero Favorit",
                            "3. Menghapus Hero Favorit",
                            "4. Kembali"
                        ],
                    )
                ]
                jawab_favorit = inquirer.prompt(tanya_favorit)
                if jawab_favorit is None:
                    break
                pilihan = jawab_favorit["pilihan"]
                if "1." in pilihan:
                    p.bersihkan_layar()
                    print('='*14, 'HERO FAVORIT KAMU', '='*14)
                    p.tampilkan_favorit()
                    input("Tekan Enter untuk kembali...")
                elif "2." in pilihan:
                    p.bersihkan_layar()
                    p.tampilkan_seluruh_hero()
                    print('='*44)
                    nama_hero = input("Masukkan Nama Hero yang ingin difavoritkan: ").strip()
                    hasil = p.tambah_favorit(nama_hero)
                    print('='*44)
                    if hasil == "berhasil":
                        print("Hero berhasil ditambahkan ke favorit!")
                    elif hasil == "sudah_ada":
                        print("Hero tersebut sudah ada di daftar favorit!")
                    else:
                        print("Gagal! Nama hero tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")
                elif "3." in pilihan:
                    p.bersihkan_layar()
                    print('='*14, 'HERO FAVORIT KAMU', '='*14)
                    if p.tampilkan_favorit():
                        nama_hero = input("Masukkan Nama Hero yang ingin dihapus dari favorit: ").strip()
                        print('='*44)
                        if p.hapus_favorit(nama_hero):
                            print("Hero berhasil dihapus dari favorit!")
                        else:
                            print("Gagal! Hero tersebut tidak ada di daftar favorit.")
                    input("Tekan Enter untuk kembali...")
                else:
                    break

        elif "5." in menu:
            os.system("cls" if os.name == "nt" else "clear")
            p.cek_komposisi_draft()
            print("=" * 44)
            jawab_kembali = inquirer.prompt([
                inquirer.List("kembali", message="Kembali ke menu?", choices=["Ya", "Tidak"])
            ])
            if jawab_kembali is None or jawab_kembali["kembali"] == "Tidak":
                p.loginuser = False
                break

        # 6. Keluar
        else:
            p.loginuser = False
            break
