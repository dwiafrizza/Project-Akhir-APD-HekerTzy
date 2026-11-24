import inquirer
import pungsi as p

def menu_user():
    while p.loginuser == True:
        p.bersihkan_layar()
        print('='*44)
        print('='*16, 'MENU USER', '='*17)
        print('='*44)
        
        tanya_menu = [
            inquirer.List(
                "pilihan",
                message="Masukkan Pilihan",
                choices=[
                    "1. Melihat Daftar Data Hero", 
                    "2. Searching Data Hero", 
                    "3. Bandingkan dan Rekomendasi Hero",
                    "4. Keluar"
            ],
            )
        ]
        jawab_menu = inquirer.prompt(tanya_menu)
        menu = jawab_menu["pilihan"]
        
        if "1." in menu:
            p.bersihkan_layar()
            p.tampilkan_seluruh_hero()
            print('='*44)
            hasil = input("Kembali ke menu? (y/n): ")
            if hasil.lower() == "n":
                p.loginuser = False
                break
            p.bersihkan_layar()

        elif "2." in menu:
            p.bersihkan_layar()
            print('='*22, 'CARI DATA HERO', '='*22)
            
            tanya_role = [
                inquirer.List(
                    "role",
                    message="Pilih Role Hero",
                    choices= list(p.role_valid) + ["All"],
                )
            ]
            jawab_role = inquirer.prompt(tanya_role)
            pilih_role = jawab_role["role"]
            
            tanya_lane = [
                inquirer.List(
                    "lane",
                    message="Pilih Lane Hero",
                    choices=list(p.lane_valid) + ["All"],
                )
            ]
            jawab_lane = inquirer.prompt(tanya_lane)
            pilih_lane = jawab_lane["lane"]
            
            p.bersihkan_layar()
            p.tampilkan_hero_filter(pilih_role, pilih_lane)
            print('='*44) 

            if p.kembali_menu() == False:
                p.loginuser = False
                break
            p.bersihkan_layar()

        elif "3." in menu:
            p.bersihkan_layar()
            print('='*10, 'BANDINGKAN DAN REKOMENDASI HERO', '='*10)

            hero1 = input("Masukkan nama hero pertama: ")
            hero2 = input("Masukkan nama hero kedua: ")
            print('='*52)
            p.bandingkan_hero(hero1, hero2)
            print('='*52)

            if p.kembali_menu() == False:
                p.loginuser = False
                break
            p.bersihkan_layar()