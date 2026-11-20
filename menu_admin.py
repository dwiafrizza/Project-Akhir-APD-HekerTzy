import inquirer
import pungsi as p

def menu_admin():
    while p.current_role == "admin":
        print('='*44)
        print('='*16, 'MENU ADMIN', '='*16)
        print('='*44)
        tanya_menu = [
            inquirer.List(
                "pilihan",
                message="Masukkan pilihan",
                choices=[
                    "1. Menambah Data Hero", 
                    "2. Melihat Daftar Data Hero", 
                    "3. Mengedit Data Hero",
                    "4. Menghapus Data Hero", 
                    "5. Mencari Data Hero",
                    "6. Keluar"
                ],
            )
        ]
        jawab_menu = inquirer.prompt(tanya_menu)
        menu = jawab_menu["pilihan"]
        
        if "2." in menu:
            p.bersihkan_layar()
            p.tampilkan_seluruh_hero()
            print('='*44)
            hasil = input("Kembali ke menu? (y/n): ")
            if hasil == "n":
                p.current_role = None
                break
            p.bersihkan_layar()

        elif "1." in menu:
            p.bersihkan_layar()
            print('='*22, 'TAMBAH DATA HERO', '='*22)
            print('='*62)
            p.tampilkan_seluruh_hero()
            print(f"Jumlah Hero Saat ini adalah {len(p.data_hero)}")

            while True:
                nama_input = input("Masukkan Nama Hero: ")
                if nama_input == "":
                    print("Nama hero tidak boleh kosong!")
                    continue
                
                if p.cek_nama_duplikat(nama_input, p.data_hero):
                    print(f"Gagal! Hero dengan nama '{nama_input}' sudah ada di database.")
                else:
                    break
            
            role = input("Masukkan Role Hero: ")
            lane = input("Masukkan Lane Hero: ")
            damage = input("Masukkan Tipe Damage: ")
            
            try:
                tahun = int(input("Masukkan Tahun Rilis: "))
            except ValueError:
                print("Tahun harus berupa bilangan bulat!")
                input("Tekan enter untuk kembali...")
                p.bersihkan_layar()
                continue
                
            nomor_baru = max(p.data_hero.keys()) + 1
            list_baru = [nama_input, role, lane, damage, str(tahun)]
            
            p.tambah_data_hero(nomor_baru, list_baru)
            print('='*44)
            print("Data hero berhasil ditambahkan.")
            hasil = input("Kembali ke menu? (y/n): ")
            if hasil == "n":
                p.current_role = None
                break
            p.bersihkan_layar()
            
        elif "3." in menu: 
            p.bersihkan_layar()
            p.tampilkan_seluruh_hero()
            print('='*44)
            nama_edit = input("Masukkan Nama Hero yang ingin diedit: ")
            key_target = p.cari_key_hapus(nama_edit)
            
            if key_target != False:
                print('='*44)            
                nama_baru = input("Nama baru: ")
                role_baru = input("Role baru: ")
                lane_baru = input("Lane baru: ")
                damage_baru = input("Tipe damage baru: ")
                
                # Tahun rilis dikunci/tidak boleh diganti, diambil otomatis dari data lama
                tahun_lama = p.data_hero[key_target][4]
                print(f"Tahun Rilis tetap (tidak dapat diubah): {tahun_lama}")
                
                list_update = [nama_baru, role_baru, lane_baru, damage_baru, tahun_lama]
                
                p.edit_data_hero(key_target, list_update)
                print('='*44)
                print("Data hero berhasil diperbarui!")
            else:
                print('='*44)
                print("Gagal! Nama hero tidak ditemukan.")
                
            hasil = input("Kembali ke menu? (y/n): ")
            if hasil.lower() == "n":
                p.current_role = None
                break
            p.bersihkan_layar()

        elif "4." in menu:
            p.bersihkan_layar()
            p.tampilkan_seluruh_hero()
            print('='*44)
            nama_hapus = input("Masukkan Nama Hero yang ingin dihapus (Contoh: Miya): ")
            key_target = p.cari_key_hapus(nama_hapus)
            
            if key_target != False:
                nama_target = p.data_hero[key_target][0]
                del p.data_hero[key_target]
                print('='*44)
                print("Sukses menghapus data:", nama_target)
                
                # Merapikan kembali key dictionary agar urut dari 1 secara otomatis
                urut_data = {}
                key_ulang = 1
                for key in p.data_hero.keys():
                    urut_data[key_ulang] = p.data_hero[key]
                    key_ulang += 1
                p.data_hero = urut_data
            else:
                print('='*44)
                print("Gagal! Nama hero tidak ditemukan.")
                
            hasil = input("Kembali ke menu? (y/n): ")
            if hasil.lower() == "n":
                p.current_role = None
                break
            p.bersihkan_layar()

        elif "5." in menu:
            p.bersihkan_layar()
            print('='*22, 'CARI DATA HERO', '='*22)
            
            daftar_role = ["Fighter", "Marksman", "Assassin", "Mage", "Support", "Tank", "All"]
            daftar_lane = ["EXP Lane", "Gold Lane", "Jungle", "Roam", "Mid Lane", "All"]
            tanya_role = [
                inquirer.List(
                    "role",
                    message="Pilih Role Hero",
                    choices=daftar_role,
                )
            ]
            jawab_role = inquirer.prompt(tanya_role)
            pilih_role = jawab_role["role"]
            
            tanya_lane = [
                inquirer.List(
                    "lane",
                    message="Pilih Lane Hero",
                    choices=daftar_lane,
                )
            ]
            jawab_lane = inquirer.prompt(tanya_lane)
            pilih_lane = jawab_lane["lane"]
            
            p.bersihkan_layar()
            p.tampilkan_hero_filter(pilih_role, pilih_lane)
            print('='*44)
            
            hasil = input("Kembali ke menu? (y/n): ")
            if hasil == "n":
                p.current_role = None
                break
            p.bersihkan_layar()

        else:
            p.current_role = None
            break