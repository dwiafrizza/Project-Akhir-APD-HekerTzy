import os
import inquirer
import pungsi as p

def menu_admin():
    while p.loginadmin == True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 44)
        print("=" * 16, "MENU ADMIN", "=" * 16)
        print("=" * 44)
        jawab_menu = inquirer.prompt([
            inquirer.List(
                "pilihan",
                message="Masukkan pilihan",
                choices=[
                    "1. Menambah Data Hero",
                    "2. Melihat Daftar Data Hero",
                    "3. Mengedit Data Hero",
                    "4. Menghapus Data Hero",
                    "5. Manajemen Akun User",
                    "6. Keluar",
                ],
            )
        ])
        if jawab_menu is None:
            p.loginadmin = False
            break
        menu = jawab_menu["pilihan"]

        if "1." in menu:
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 22, "TAMBAH DATA HERO", "=" * 22)
            print("=" * 62)
            p.tampilkan_seluruh_hero()
            print(f"Jumlah Hero Saat ini adalah {len(p.data_hero)}")
            while True: #akan terus looping smpe ada yg ngehentiin, kyk break
                nama_input = input("Masukkan Nama Hero: ")
                if nama_input == "":
                    print("Nama hero tidak boleh kosong!")
                    continue
                if p.cari_key_hero(nama_input) != False: #kalau dia ga false kan berarti ada di database
                    print(f"{nama_input} sudah ada di database. Silahkan masukkan nama lain.")
                else:
                    break

            while True:
                role = input("Masukkan Role Hero: ")
                cocok_role = [r for r in p.role_valid if r.lower() == role.lower()]
                if cocok_role:
                    role = cocok_role[0]
                    break
                print("Input role tidak valid! Pilihan:", p.role_valid)

            while True:
                lane = input("Masukkan Lane Hero: ")
                cocok_lane = [l for l in p.lane_valid if l.lower() == lane.lower()]
                if cocok_lane:
                    lane = cocok_lane[0]
                    break
                print("Input lane tidak valid! Pilihan:", p.lane_valid)

            while True:
                damage = input("Masukkan Tipe Damage: ")
                cocok_damage = [d for d in p.damage_valid if d.lower() == damage.lower()]
                if cocok_damage:
                    damage = cocok_damage[0]
                    break
                print("Input tipe damage tidak valid! Pilihan:", p.damage_valid)

            tahun_terakhir = max((int(v[4]) for v in p.data_hero.values()), default=2016)
            while True:
                input_tahun = input(f"Masukkan Tahun Rilis (>= {tahun_terakhir}): ").strip()
                try:
                    tahun = int(input_tahun)
                except ValueError:
                    print("Tahun harus berupa bilangan bulat!")
                    continue
                if tahun < tahun_terakhir:
                    print(f"Tahun rilis tidak boleh kurang dari tahun rilis hero terakhir ({tahun_terakhir})!")
                    continue
                break

            nomor_baru = max(p.data_hero.keys()) + 1 if p.data_hero else 1
            p.data_hero[nomor_baru] = [nama_input, role, lane, damage, str(tahun)]
            print("=" * 44)
            print("Data hero berhasil ditambahkan.")

            jawab_kembali = inquirer.prompt([
                inquirer.List("kembali", message="Kembali ke menu?", choices=["Ya", "Tidak"])
            ])
            if jawab_kembali is None or jawab_kembali["kembali"] == "Tidak":
                p.loginadmin = False
                break

        elif "2." in menu:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                p.tampilkan_seluruh_hero()
                print("=" * 44)

                jawab_aksi = inquirer.prompt([
                    inquirer.List(
                        "aksi",
                        message="Pilih tindakan",
                        choices=[
                            "Filter / Cari Hero (Role & Lane)",
                            "Kembali ke Menu Admin",
                            "Logout",
                        ],
                    )
                ])
                if jawab_aksi is None or jawab_aksi["aksi"] == "Kembali ke Menu Admin":
                    break
                if jawab_aksi["aksi"] == "Logout":
                    p.loginadmin = False
                    break

                jawab_role = inquirer.prompt([
                    inquirer.List("role", message="Pilih Role Hero", choices=list(p.role_valid) + ["All"])
                ])
                if jawab_role is None:
                    break

                jawab_lane = inquirer.prompt([
                    inquirer.List("lane", message="Pilih Lane Hero", choices=list(p.lane_valid) + ["All"])
                ])
                if jawab_lane is None:
                    break

                os.system("cls" if os.name == "nt" else "clear")
                p.tampilkan_hero_filter(jawab_role["role"], jawab_lane["lane"])
                print("=" * 44)
                input("Tekan Enter untuk kembali ke daftar hero...")

        elif "3." in menu:
            os.system("cls" if os.name == "nt" else "clear")
            p.tampilkan_seluruh_hero()
            print('='*44)
            nama_edit = input("Masukkan Nama Hero yang ingin diedit: ")
            key_target = p.cari_key_hero(nama_edit)
            
            if key_target != False:
                nama_lama, role_lama, lane_lama, damage_lama, tahun_lama = p.data_hero[key_target]
                print('='*44)
                print("Data lama:", nama_lama, "|", role_lama, "|", lane_lama, "|", damage_lama, "|", tahun_lama)
                print('='*44)
 
                nama_baru = input("Nama baru: ")
 
                role_baru = p.cek_validasi("Role baru: ", p.role_valid)
                role_tambah = inquirer.prompt([
                    inquirer.List("pilihan", message="Tambah role ke-2?", choices=["Ya", "Tidak"])
                ])
                if role_tambah["pilihan"] == "Ya":
                    role_kedua = p.cek_validasi("Role kedua: ", p.role_valid)
                    role_baru = role_baru + "/" + role_kedua
 
                lane_baru = p.cek_validasi("Lane baru: ", p.lane_valid)
                lane_tambah = inquirer.prompt([
                    inquirer.List("pilihan", message="Tambah role ke-2?", choices=["Ya", "Tidak"])
                ])
                if lane_tambah["pilihan"] == "Ya":
                    lane_kedua = p.cek_validasi("Lane kedua: ", p.lane_valid)
                    lane_baru = lane_baru + "/" + lane_kedua
 
                damage_baru = p.cek_validasi("Tipe damage baru: ", p.damage_valid)
                 
                print(f"Tahun Rilis tetap (tidak dapat diubah): {tahun_lama}")
                
                tuple_update = (nama_baru, role_baru, lane_baru, damage_baru, tahun_lama)
                
                p.edit_data_hero(key_target, tuple_update)
                print('='*44)
                print("Data hero berhasil diperbarui!")
            else:
                print('='*44)
                print("Gagal! Nama hero tidak ditemukan.")

            jawab_kembali = inquirer.prompt([
                inquirer.List("kembali", message="Kembali ke menu?", choices=["Ya", "Tidak"])
            ])
            if jawab_kembali is None or jawab_kembali["kembali"] == "Tidak":
                p.loginadmin = False
                break

        elif "4." in menu:
            os.system("cls" if os.name == "nt" else "clear")
            p.tampilkan_seluruh_hero()
            print('='*44)
            nama_hapus = input("Masukkan Nama Hero yang ingin dihapus: ")
            key_target = p.cari_key_hero(nama_hapus)
            
            if key_target != False:
                nama_target, role_target, lane_target, damage_target, tahun_target = p.data_hero[key_target]
                print('='*44)
                print(f"Hero yang dipilih: {nama_target} | {role_target} | {lane_target} | {damage_target} | {tahun_target}")
                print('='*44)
                yakin = inquirer.prompt([
                inquirer.List("yakin", message="Yakin ingin menghapus?", choices=["Ya", "Tidak"])
            ])
 
                if yakin["yakin"] == "Ya":
                    del p.data_hero[key_target]
                    print('='*44)
                    print("Sukses menghapus data:", nama_target)

                    urut_data = {}
                    key_ulang = 1
                    for key in p.data_hero.keys():
                        urut_data[key_ulang] = p.data_hero[key]
                        key_ulang += 1
                    p.data_hero = urut_data
                else:
                    print('='*44)
                    print("Penghapusan dibatalkan.")
            else:
                print('='*44)
                print("Gagal! Nama hero tidak ditemukan.")

            jawab_kembali = inquirer.prompt([
                inquirer.List("kembali", message="Kembali ke menu?", choices=["Ya", "Tidak"])
            ])
            if jawab_kembali is None or jawab_kembali["kembali"] == "Tidak":
                p.loginadmin = False
                break

        elif "5." in menu:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("=" * 14, "MANAJEMEN AKUN USER", "=" * 14)
                if len(p.data_akun) == 0:
                    print("Belum ada akun user terdaftar.")
                    input("Tekan Enter untuk kembali...")
                    break
                p.tampilkan_akun_pandas()
                print()
                jawab_aksi_akun = inquirer.prompt([
                    inquirer.List(
                        "aksi",
                        message="Pilih tindakan akun",
                        choices=["Ban Akun User", "Unban Akun User", "Kembali"],
                    )
                ])
                if jawab_aksi_akun is None or jawab_aksi_akun["aksi"] == "Kembali":
                    break
                target_usn = input("Masukkan Username target: ")
                ditemukan = False
                for akun in p.data_akun:
                    if akun[0] == target_usn:
                        ditemukan = True
                        if len(akun) < 3:
                            akun.append(False)

                        if jawab_aksi_akun["aksi"] == "Ban Akun User":
                            akun[2] = True
                            p.simpan_data_akun(p.data_akun)
                            print(f"Akun '{akun[0]}' berhasil di-BAN.")
                        elif jawab_aksi_akun["aksi"] == "Unban Akun User":
                            akun[2] = False
                            p.simpan_data_akun(p.data_akun)
                            print(f"Akun '{akun[0]}' berhasil di-UNBAN.")
                        break

                if not ditemukan:
                    print("Username tidak ditemukan!")
                input("Tekan Enter untuk melanjutkan...")

        # 6.Keluar
        else:
            p.loginadmin = False
            break