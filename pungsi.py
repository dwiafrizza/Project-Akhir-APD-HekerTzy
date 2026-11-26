import os
import json
import inquirer
import pandas as pd
from prettytable import PrettyTable

FILE_AKUN = "data_akun.json"

loginuser = False
loginadmin = False

daftar_admin = [
    ["Rizki", "007"],
    ["Surya", "002"],
    ["Rizal", "001"],
]

role_valid = ("Fighter", "Marksman", "Assassin", "Mage", "Support", "Tank")
lane_valid = ("EXP Lane", "Gold Lane", "Jungle", "Roam", "Mid Lane")
damage_valid = ("Physical", "Magic")

data_hero = {
    1: ["Miya", "Marksman", "Gold Lane", "Physical", "2016"],
    2: ["Balmond", "Fighter", "EXP Lane/Jungle", "Physical", "2016"],
    3: ["Saber", "Assassin", "Jungle", "Physical", "2016"],
    4: ["Alice", "Mage/Tank", "EXP Lane", "Magic", "2016"],
    5: ["Nana", "Mage/Support", "Mid Lane", "Magic", "2016"],
    6: ["Tigreal", "Tank", "Roam", "Physical", "2016"],
    7: ["Alucard", "Fighter/Assassin", "Jungle", "Physical", "2016"],
    8: ["Karina", "Assassin", "Jungle", "Magic", "2016"],
    9: ["Akai", "Tank", "Roam/Jungle", "Physical", "2016"],
    10: ["Franco", "Tank/Support", "Roam", "Physical", "2016"],
    11: ["Bane", "Fighter/Mage", "EXP Lane/Jungle", "Physical", "2016"],
    12: ["Bruno", "Marksman", "Gold Lane", "Physical", "2016"],
    13: ["Clint", "Marksman", "Gold Lane", "Physical", "2016"],
    14: ["Rafaela", "Support", "Roam", "Magic", "2016"],
    15: ["Eudora", "Mage", "Mid Lane", "Magic", "2016"],
    16: ["Zilong", "Fighter/Assassin", "EXP Lane", "Physical", "2016"],
    17: ["Fanny", "Assassin", "Jungle", "Physical", "2016"],
    18: ["Layla", "Marksman", "Gold Lane", "Physical", "2016"],
    19: ["Minotaur", "Tank/Support", "Roam", "Physical", "2016"],
    20: ["Lolita", "Tank/Support", "Roam", "Physical", "2016"],
    21: ["Hayabusa", "Assassin", "Jungle", "Physical", "2016"],
    22: ["Freya", "Fighter", "EXP Lane/Jungle", "Physical", "2016"],
    23: ["Gord", "Mage", "Mid Lane", "Magic", "2016"],
    24: ["Natalia", "Assassin", "Jungle/Roam", "Physical", "2016"],
    25: ["Kagura", "Mage", "Mid Lane", "Magic", "2016"],
    26: ["Chou", "Fighter", "EXP Lane/Roam", "Physical", "2016"],
    27: ["Johnson", "Tank", "Roam", "Physical", "2017"],
    28: ["Yi Sun-shin", "Assassin/Marksman", "Jungle", "Physical", "2017"],
    29: ["Cyclops", "Mage", "Mid Lane", "Magic", "2016"],
    30: ["Estes", "Support", "Roam", "Magic", "2017"],
    31: ["Hilda", "Fighter/Tank", "EXP Lane/Roam", "Physical", "2017"],
    32: ["Aurora", "Mage", "Mid Lane", "Magic", "2017"],
    33: ["Lapu-Lapu", "Fighter", "EXP Lane", "Physical", "2017"],
    34: ["Vexana", "Mage", "Mid Lane", "Magic", "2017"],
    35: ["Roger", "Fighter/Marksman", "Jungle", "Physical", "2017"],
    36: ["Karrie", "Marksman", "Gold Lane", "Physical", "2017"],
    37: ["Gatotkaca", "Tank/Fighter", "EXP Lane/Roam", "Magic", "2017"],
    38: ["Harley", "Assassin/Mage", "Jungle", "Magic", "2017"],
    39: ["Irithel", "Marksman", "Gold Lane", "Physical", "2017"],
    40: ["Grock", "Tank", "Roam", "Physical", "2017"],
    41: ["Argus", "Fighter", "EXP Lane", "Physical", "2017"],
    42: ["Odette", "Mage", "Mid Lane", "Magic", "2017"],
    43: ["Lancelot", "Assassin", "Jungle", "Physical", "2017"],
    44: ["Diggie", "Support", "Roam", "Magic", "2017"],
    45: ["Hylos", "Tank", "Roam", "Magic", "2017"],
    46: ["Zhask", "Mage", "Mid Lane", "Magic", "2017"],
    47: ["Helcurt", "Assassin", "Jungle/Roam", "Physical", "2017"],
    48: ["Pharsa", "Mage", "Mid Lane", "Magic", "2018"],
    49: ["Lesley", "Marksman/Assassin", "Gold Lane", "Physical", "2018"],
    50: ["Jawhead", "Fighter", "EXP Lane/Roam", "Physical", "2018"],
    51: ["Angela", "Support", "Roam", "Magic", "2018"],
    52: ["Gusion", "Assassin", "Jungle", "Magic", "2018"],
    53: ["Valir", "Mage", "Mid Lane", "Magic", "2018"],
    54: ["Martis", "Fighter", "Jungle/EXP Lane", "Physical", "2018"],
    55: ["Uranus", "Tank", "EXP Lane", "Magic", "2018"],
    56: ["Hanabi", "Marksman", "Gold Lane", "Physical", "2018"],
    57: ["Chang'e", "Mage", "Mid Lane", "Magic", "2018"],
    58: ["Kaja", "Fighter/Support", "Roam", "Magic", "2018"],
    59: ["Selena", "Assassin/Mage", "Jungle/Roam", "Magic", "2018"],
    60: ["Aldous", "Fighter", "EXP Lane", "Physical", "2018"],
    61: ["Claude", "Marksman", "Gold Lane", "Physical", "2018"],
    62: ["Vale", "Mage", "Mid Lane", "Magic", "2018"],
    63: ["Leomord", "Fighter", "Jungle/EXP Lane", "Physical", "2018"],
    64: ["Lunox", "Mage", "Mid Lane", "Magic", "2018"],
    65: ["Hanzo", "Assassin", "Jungle", "Physical", "2018"],
    66: ["Belerick", "Tank", "Roam", "Magic", "2018"],
    67: ["Kimmy", "Marksman/Mage", "Gold Lane", "Magic", "2018"],
    68: ["Thamuz", "Fighter", "EXP Lane/Jungle", "Physical", "2018"],
    69: ["Harith", "Mage", "Gold Lane/Mid Lane", "Magic", "2018"],
    70: ["Minsitthar", "Fighter", "EXP Lane", "Physical", "2018"],
    71: ["Kadita", "Mage/Assassin", "Mid Lane/Roam", "Magic", "2018"],
    72: ["Faramis", "Support/Mage", "Roam/Mid Lane", "Magic", "2018"],
    73: ["Badang", "Fighter", "EXP Lane", "Physical", "2019"],
    74: ["Khufra", "Tank", "Roam", "Physical", "2019"],
    75: ["Granger", "Marksman", "Gold Lane/Jungle", "Physical", "2019"],
    76: ["Guinevere", "Fighter", "EXP Lane", "Magic", "2019"],
    77: ["Esmeralda", "Tank/Mage", "EXP Lane", "Magic", "2019"],
    78: ["Terizla", "Fighter", "EXP Lane", "Physical", "2019"],
    79: ["X.Borg", "Fighter", "EXP Lane", "Physical", "2019"],
    80: ["Ling", "Assassin", "Jungle", "Physical", "2019"],
    81: ["Dyrroth", "Fighter", "EXP Lane/Jungle", "Physical", "2019"],
    82: ["Lylia", "Mage", "Mid Lane", "Magic", "2019"],
    83: ["Baxia", "Tank", "Jungle/Roam", "Magic", "2019"],
    84: ["Masha", "Fighter", "EXP Lane", "Physical", "2019"],
    85: ["Wanwan", "Marksman", "Gold Lane", "Physical", "2019"],
    86: ["Silvanna", "Fighter", "EXP Lane", "Magic", "2019"],
    87: ["Cecilion", "Mage", "Mid Lane", "Magic", "2020"],
    88: ["Carmilla", "Support/Tank", "Roam", "Magic", "2020"],
    89: ["Atlas", "Tank", "Roam", "Magic", "2020"],
    90: ["Popol and Kupa", "Marksman", "Gold Lane", "Physical", "2020"],
    91: ["Yu Zhong", "Fighter", "EXP Lane", "Physical", "2020"],
    92: ["Luo Yi", "Mage", "Mid Lane", "Magic", "2020"],
    93: ["Benedetta", "Assassin", "EXP Lane/Jungle", "Physical", "2020"],
    94: ["Khaleed", "Fighter", "EXP Lane", "Physical", "2020"],
    95: ["Barats", "Tank/Fighter", "Jungle/EXP Lane", "Physical", "2020"],
    96: ["Brody", "Marksman", "Gold Lane", "Physical", "2020"],
    97: ["Yve", "Mage", "Mid Lane", "Magic", "2021"],
    98: ["Mathilda", "Support/Assassin", "Roam", "Magic", "2020"],
    99: ["Paquito", "Fighter", "EXP Lane/Jungle", "Physical", "2021"],
    100: ["Gloo", "Tank", "EXP Lane/Roam", "Magic", "2021"],
    101: ["Beatrix", "Marksman", "Gold Lane", "Physical", "2021"],
    102: ["Phoveus", "Fighter", "EXP Lane", "Magic", "2021"],
    103: ["Natan", "Marksman", "Gold Lane", "Magic", "2021"],
    104: ["Aulus", "Fighter", "Jungle/EXP Lane", "Physical", "2021"],
    105: ["Aamon", "Assassin", "Jungle", "Magic", "2021"],
    106: ["Floryn", "Support", "Roam", "Magic", "2021"],
    107: ["Yin", "Fighter", "EXP Lane/Jungle", "Physical", "2022"],
    108: ["Melissa", "Marksman", "Gold Lane", "Physical", "2022"],
    109: ["Xavier", "Mage", "Mid Lane", "Magic", "2022"],
    110: ["Julian", "Fighter/Assassin", "Jungle/EXP Lane", "Magic", "2022"],
    111: ["Fredrinn", "Fighter/Tank", "Jungle/EXP Lane", "Physical", "2022"],
    112: ["Joy", "Assassin", "Jungle", "Magic", "2022"],
    113: ["Novaria", "Mage", "Mid Lane", "Magic", "2023"],
    114: ["Arlott", "Fighter/Assassin", "EXP Lane", "Physical", "2023"],
    115: ["Ixia", "Marksman", "Gold Lane", "Physical", "2023"],
    116: ["Nolan", "Assassin", "Jungle", "Physical", "2023"],
    117: ["Cici", "Fighter", "EXP Lane", "Physical", "2023"],
    118: ["Chip", "Tank/Support", "Roam", "Magic", "2024"],
    119: ["Zhuxin", "Mage", "Mid Lane", "Magic", "2024"],
    120: ["Suyou", "Fighter/Assassin", "Jungle/EXP Lane", "Physical", "2024"],
    121: ["Lukas", "Fighter", "EXP Lane", "Physical", "2024"],
    122: ["Kalea", "Support/Fighter", "Roam", "Physical", "2025"],
    123: ["Zetian", "Mage", "Mid Lane", "Magic", "2025"],
    124: ["Obsidia", "Marksman", "Gold Lane", "Physical", "2025"],
    125: ["Sora", "Fighter/Assassin", "EXP Lane/Jungle", "Physical", "2025"],
    126: ["Marcel", "Support", "Roam", "Magic", "2025"],
    127: ["Hirara", "Assassin", "Jungle", "Physical", "2026"],
}

kesulitan_hero = {
    4: "Sedang", 5: "Sedang", 10: "Sedang", 13: "Sedang", 17: "Sulit",
    21: "Sulit", 25: "Sulit", 26: "Sulit", 52: "Sulit", 59: "Sulit",
    80: "Sulit", 85: "Sulit", 93: "Sulit", 101: "Sulit", 107: "Sulit",
    112: "Sulit"
}
####################################################################################################################
#..general
def cari_key_hero(nama_target):
    target = nama_target.strip().lower()
    for key, value in data_hero.items():
        if value[0].lower() == target:
            return key
    return False
###################################################################################################################
#..json akun handling
def muat_data_akun():
    try:
        with open(FILE_AKUN, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []

def simpan_data_akun(data):
    with open(FILE_AKUN, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
###################################################################################################################
#..MANAJEMEN AKUN USER
data_akun = muat_data_akun()
def tampilkan_akun_pandas():
    baris = []
    for akun in data_akun:
        status_ban = "BANNED" if akun[2] == True else "AKTIF"
        baris.append({
            "Username": akun[0],
            "Password": akun[1],
            "Status": status_ban,
        })
    df = pd.DataFrame(baris)
    print(df)
###################################################################################################################
#..MELIHAT DAFTAR DATA HERO
def tampilkan_seluruh_hero():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Hero", "Role", "Lane", "Tipe Damage", "Tahun Rilis"]
    for key, value in data_hero.items():
        tabel.add_row([key, value[0], value[1], value[2], value[3], value[4]])
    tabel.align["Nama Hero"] = "l"
    print(tabel)
####################################################################################################################
#..SEARCHING HERO
def tampilkan_hero_filter(role_filter, lane_filter):
    hasil = []
    for key, value in data_hero.items():
        cocok_role = (role_filter == "All") or (role_filter in value[1])
        cocok_lane = (lane_filter == "All") or (lane_filter in value[2])
        if cocok_role and cocok_lane:
            hasil.append((key, value))
    if len(hasil) == 0:
        print("Tidak ada hero yang ditemukan sesuai filter tersebut!")
        return
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Hero", "Role", "Lane", "Tipe Damage", "Tahun Rilis"]
    for key, value in hasil:
        tabel.add_row([key, value[0], value[1], value[2], value[3], value[4]])
    tabel.align["Nama Hero"] = "l"
    print(tabel)
###################################################################################################################
#..PILIH HERO FAVORIT
hero_favorit = {}
akun_login = "" 
def ambil_favorit():
    if akun_login not in hero_favorit:
        hero_favorit[akun_login] = []
    return hero_favorit[akun_login]

def tambah_favorit(nama_hero):
    key = cari_key_hero(nama_hero)
    if key is False:
        return "tidak_ada"
    nama_asli = data_hero[key][0]
    favorit = ambil_favorit()
    if nama_asli in favorit:
        return "sudah_ada"
    favorit.append(nama_asli)
    return "berhasil"

def hapus_favorit(nama_hero):
    favorit = ambil_favorit()
    nama_cari = nama_hero
    if nama_cari in favorit:
        favorit.remove(nama_cari)
        return True
    return False

def tampilkan_favorit():
    favorit = ambil_favorit()
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Hero", "Role", "Lane", "Tipe Damage", "Tahun Rilis"]
    nomor = 1
    for value in data_hero.values():
        if value[0] in favorit:
            tabel.add_row([nomor, value[0], value[1], value[2], value[3], value[4]])
            nomor += 1
    if nomor == 1:
        print("Daftar hero favorit masih kosong.")
        return False
    tabel.align["Nama Hero"] = "l"
    print(tabel)
    return True
##################################################################################################################
#..komparasi hero
def cek_kesulitan(key):
    if key in kesulitan_hero:
        return kesulitan_hero[key]
    return "Mudah"

def angka_kesulitan(teks):
    if teks == "Mudah":
        return 1
    if teks == "Sedang":
        return 2
    return 3

def bandingkan_hero(nama1, nama2):
    key1 = cari_key_hero(nama1)
    key2 = cari_key_hero(nama2)

    if key1 is False and key2 is False:
        print("Kedua hero tidak ditemukan!")
        return
    elif key1 is False:
        print(f"Hero '{nama1}' tidak ditemukan!")
        return
    elif key2 is False:
        print(f"Hero '{nama2}' tidak ditemukan!")
        return
    elif key1 == key2:
        print("Pilih dua hero yang berbeda!")
        return
    
    hero1 = data_hero[key1]
    hero2 = data_hero[key2]
    sulit1 = cek_kesulitan(key1)
    sulit2 = cek_kesulitan(key2)
    tabel1 = PrettyTable()
    tabel1.field_names = ["Data", hero1[0]]
    tabel1.add_row(["Role", hero1[1]])
    tabel1.add_row(["Lane", hero1[2]])
    tabel1.add_row(["Tipe Damage", hero1[3]])
    tabel1.add_row(["Tahun Rilis", hero1[4]])
    tabel1.add_row(["Kesulitan", sulit1])

    tabel2 = PrettyTable()
    tabel2.field_names = ["Data", hero2[0]]
    tabel2.add_row(["Role", hero2[1]])
    tabel2.add_row(["Lane", hero2[2]])
    tabel2.add_row(["Tipe Damage", hero2[3]])
    tabel2.add_row(["Tahun Rilis", hero2[4]])
    tabel2.add_row(["Kesulitan", sulit2])

    baris1 = tabel1.get_string().split("\n")
    baris2 = tabel2.get_string().split("\n")
    for i in range(len(baris1)):
        print(baris1[i] + "   " + baris2[i])
        
    print()
    angka1 = angka_kesulitan(sulit1)
    angka2 = angka_kesulitan(sulit2)
    if angka1 < angka2:
        print(f"Direkomendasikan untuk pemula: {hero1[0]} (kesulitan {sulit1} vs {hero2[0]} yang {sulit2}).")
    elif angka2 < angka1:
        print(f"Direkomendasikan untuk pemula: {hero2[0]} (kesulitan {sulit2} vs {hero1[0]} yang {sulit1}).")
    else:
        print(f"Keduanya sama-sama memiliki tingkat kesulitan {sulit1}, cocok dicoba sesuai preferensi.")

##################################################################################################################
#..CEK KOMPOSISI TIM (DRAFT PICK)
def tampilkan_daftar_per_role_horizontal(hero_terpakai):
    data = {}

    for role in role_valid:
        hero = []
        for key, value in data_hero.items():
            if role in value[1].split("/") and key not in hero_terpakai:
                hero.append(value[0])
        data[role] = pd.Series(hero)

    df = pd.DataFrame(data).fillna("")
    print(df)

def lane_sesuai_hero(lane_pilih, hero_info):
    lane_asli = [lane.strip().lower() for lane in hero_info[2].split("/")]
    return lane_pilih.lower() in lane_asli

def rekomendasi_lane_hero(hero_info):
    lane_asli = [lane.strip() for lane in hero_info[2].split("/")]
    return lane_asli[0]

def cek_komposisi_draft():
    tim = []
    hero_terpakai = set()
    print("=" * 14, "DRAFT PICK", "=" * 14)
    for slot in range(1, 6):
        print()
        print(f"--- Pick ke-{slot} dari 5 ---")
        jawab_lane = inquirer.prompt([
            inquirer.List("lane", message=f"Pilih Lane ke-{slot}", choices=list(lane_valid))
        ])
        if jawab_lane is None:
            return #biar ga error pas ctrl+c
        lane_pilih = jawab_lane["lane"]
        tampilkan_daftar_per_role_horizontal(hero_terpakai)
        while True:
            nama_input = input(f"Masukkan nama hero untuk {lane_pilih}: ").strip()
            key_hero = cari_key_hero(nama_input)
            if key_hero is False:
                print("Nama hero tidak ditemukan, coba lagi.")
                continue
            if key_hero in hero_terpakai:
                print(f"{data_hero[key_hero][0]} sudah dipilih di pick sebelumnya.")
                continue
            break
        hero_terpakai.add(key_hero)
        info_hero = data_hero[key_hero]
        tim.append({
            "key": key_hero,
            "nama": info_hero[0],
            "role_hero": info_hero[1],
            "lane_hero": info_hero[2],
            "damage": info_hero[3],
            "lane_pilih": lane_pilih,
        })
    tabel = PrettyTable()
    tabel.field_names = ["Pick", "Hero", "Role Hero", "Lane Dipilih", "Lane Hero", "Damage", "Status Lane"]
    peta_lane = {lane: [] for lane in lane_valid}
    jml_physical = 0
    jml_magic = 0
    semua_lane_cocok = True

    for idx, item in enumerate(tim, start=1):
        peta_lane[item["lane_pilih"]].append(item["nama"])
        cocok_lane = lane_sesuai_hero(item["lane_pilih"], data_hero[item["key"]])
        rekom_lane = rekomendasi_lane_hero(data_hero[item["key"]])
        if not cocok_lane:
            semua_lane_cocok = False

        if item["damage"] == "Physical":
            jml_physical += 1
        elif item["damage"] == "Magic":
            jml_magic += 1
        status_lane = "Sesuai" if cocok_lane else f"Saran -> {rekom_lane}"
        tabel.add_row([
            idx,
            item["nama"],
            item["role_hero"],
            item["lane_pilih"],
            item["lane_hero"],
            item["damage"],
            status_lane,
        ])
    print()
    print("=== HASIL DRAFT TIM ===")
    print(tabel)
    
    print()
    print("=== VALIDASI LANE===")
    ada_tabrakan = False
    for lane, daftar_nama in peta_lane.items():
        if len(daftar_nama) == 0:
            print(f"- {lane}: KOSONG (belum ada hero)")
        elif len(daftar_nama) == 1:
            print(f"- {lane}: {daftar_nama[0]} (Aman)")
        else:
            ada_tabrakan = True
            print(f"- {lane}: {' dan '.join(daftar_nama)} tidak seharusnya di satu lane yang sama.")
    
    print()
    print("=== VALIDASI KESESUAIAN LANE DENGAN ROLE ===")
    ada_saran_lane = False
    for item in tim:
        if not lane_sesuai_hero(item["lane_pilih"], data_hero[item["key"]]):
            ada_saran_lane = True
            rekom_lane = rekomendasi_lane_hero(data_hero[item["key"]])
            print(f"- {item['nama']} ditaruh di {item['lane_pilih']}; disarankan ke {rekom_lane}.")
    if not ada_saran_lane:
        print("- Semua hero berada di lane yang tepat.")
    
    print()
    print("=== VALIDASI KESEIMBANGAN DAMAGE ===")
    damage_seimbang = (jml_physical == 3 and jml_magic == 2) or (jml_physical == 2 and jml_magic == 3)
    print(f"Jumlah Physical: {jml_physical} | Jumlah Magic: {jml_magic}")
    if damage_seimbang:
        print("Status Damage: SEIMBANG (3:2).")
    else:
        print("Status Damage: BELUM SEIMBANG (target komposisi 3 Physical / 2 Magic atau sebaliknya).")

    print()
    print("=== KESIMPULAN KOMPOSISI ===")
    if not ada_tabrakan and semua_lane_cocok and damage_seimbang:
        print("Komposisi tim sudah seimbang, saatnya bantai para poke.")
    else:
        print("Komposisi tim masih perlu penyesuaian sesuai catatan di atas.")
###############################################################################################################
def cek_validasi(pesan, daftar_valid):
    while True:
        inputan = input(pesan).strip()
        for pilihan in daftar_valid:
            if inputan.lower() == pilihan.lower():
                return pilihan
        print("Input tidak valid! Pilihan:", daftar_valid)

def edit_data_hero(key, data_update):
    data_hero[key] = tuple(data_update)
    return True