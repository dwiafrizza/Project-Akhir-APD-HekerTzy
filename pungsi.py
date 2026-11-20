import os
from prettytable import PrettyTable 
import inquirer
login = False
loginuser = False
loginadmin = False

daftar_admin = [
    ["Rawr", "2112"],
    ["AdminDua", "password123"],
    ["AdminTiga", "secret456"]
]

username = 'Rizki' 
password = '123'   

current_role = None

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
    11: ["Bane", "Fighter/Mage", "EXP Lane/Jungle", "Physical/Magic", "2016"],
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
    36: ["Karrie", "Marksman", "Gold Lane", "Physical/True", "2017"],
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
    49: ["Lesley", "Marksman/Assassin", "Gold Lane", "Physical/True", "2018"],
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
    67: ["Kimmy", "Marksman/Mage", "Gold Lane", "Physical/Magic", "2018"],
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
    79: ["X.Borg", "Fighter", "EXP Lane", "True/Physical", "2019"],
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
    127: ["Hirara", "Assassin", "Jungle", "Physical", "2026"]
}

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_seluruh_hero():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Hero", "Role", "Lane", "Tipe Damage", "Tahun Rilis"]
    for key, value in data_hero.items():
        tabel.add_row([key, value[0], value[1], value[2], value[3], value[4]])
    tabel.align["Nama Hero"] = "l"
    print(tabel)

def buat_set_username():
    set_usn = set()
    # Masukkan admin
    for adm in daftar_admin:
        set_usn.add(adm[0].lower())
    # Masukkan user biasa yang aktif saat ini
    if username:
        set_usn.add(username.lower())
    return set_usn

def cek_username_duplikat(new_user):
    existing_set = buat_set_username()
    if new_user.strip().lower() in existing_set:
        return True
    return False

def buat_set_nama(data_hero):
    set_nama = set()
    for value in data_hero.values():
        set_nama.add(value[0].lower())
    return set_nama

def cek_nama_duplikat(nama_baru, data_hero):
    set_nama = buat_set_nama(data_hero)
    if nama_baru.strip().lower() in set_nama:
        return True
    return False

def filter_hero(role, lane, data_hero):
    # 1. Anggap semua hero lolos di awal
    hasil = set(data_hero.keys())
    
    # 2. Proses Filter berdasarkan Role
    if role != "all":
        role_cocok = set()
        for key, value in data_hero.items():
            if role in value[1].lower():
                role_cocok.add(key)
        hasil = hasil.intersection(role_cocok)
        
    # 3. Proses Filter berdasarkan Lane
    if lane != "all":
        lane_cocok = set()
        for key, value in data_hero.items():
            if lane in value[2].lower():
                lane_cocok.add(key)
        hasil = hasil.intersection(lane_cocok)
        
    return hasil

def tampilkan_hero_filter(role_filter, lane_filter):
    hasil_key = filter_hero(role_filter, lane_filter, data_hero)
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Hero", "Role", "Lane", "Tipe Damage", "Tahun Rilis"]
    if len(hasil_key) == 0:
        print("Tidak ada hero yang ditemukan sesuai filter tersebut!")
    else:
        for key in sorted(hasil_key):
            tabel.add_row([key, data_hero[key][0], data_hero[key][1], data_hero[key][2], data_hero[key][3], data_hero[key][4]])
        tabel.align["Nama Hero"] = "l"
        print(tabel)

def tambah_data_hero(nomor, data_baru):
    data_hero[nomor] = data_baru
    return True

def cari_key_hapus(nama_target):
    for key, value in data_hero.items():
        if nama_target.lower() == value[0].lower():
            return key
    return False

def edit_data_hero(key, data_update):
    data_hero[key] = data_update
    return True