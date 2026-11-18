import inquirer
import pungsi as p

def menu_user():
    while p.current_role == "user":
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
                    "2. Cari Hero Berdasarkan Filter", 
                    "3. Keluar"
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
                p.current_role = None
                break
            p.bersihkan_layar()

        elif "2." in menu:
            p.bersihkan_layar()
            print('='*22, 'FILTER DATA HERO', '='*22)
            
            daftar_role = ["Assassin", "Mage", "Marksman", "Fighter", "Tank", "Support", "All"]
            daftar_lane = ["Gold Lane", "EXP Lane", "Mid Lane", "Jungler", "Roamer", "All"]
            
            tanya_role = [
                inquirer.List(
                    "role",
                    message="Pilih Role Hero",
                    choices=daftar_role,
                )
            ]
            jawab_role = inquirer.prompt(tanya_role)
            pilih_role = jawab_role["role"].lower()
            
            tanya_lane = [
                inquirer.List(
                    "lane",
                    message="Pilih Lane Hero",
                    choices=daftar_lane,
                )
            ]
            jawab_lane = inquirer.prompt(tanya_lane)
            pilih_lane = jawab_lane["lane"].lower()
            
            p.bersihkan_layar()
            print(f"Hasil Filter -> Role: {jawab_role['role']} | Lane: {jawab_lane['lane']}\n")
            p.tampilkan_hero_filter(pilih_role, pilih_lane)
            print('='*44)
            
            hasil = input("Kembali ke menu? (y/n): ")
            if hasil.lower() == "n":
                p.current_role = None
                break
            p.bersihkan_layar()

        else:
            p.current_role = None
            break