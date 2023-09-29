from random import randint as rd

idxuser = []
listname = [
    # [Sesi Single Name] 📌
    # Bagian (1) 🗒️
    # 1 Nama : Depan =>6 Huruf
    "Nabila",
    "Chyntia",
    "Veronica",
    # Bagian (2) 🗒️
    # 1 Nama : Depan 5 Huruf
    "Sinta",
    "Yudha",
    "Nadia",
    # Bagian (3) 🗒️
    # 1 Nama : Depan 4 Huruf
    "Fina",
    "Dela",
    "Vina",
    # Bagian (4) 🗒️
    # 1 Nama : Depan 3 Huruf
    "Tya",
    "Ayu",
    "Ria",
    # Bagian (5) 🗒️
    # 1 Nama : Depan 1 / 2 Huruf
    "Dy",
    "Md",
    "Y",
    # [Sesi Nama Double] 📌
    # Bagian (1) 🗒️
    # 2 Nama : Depan + Tengah >=6 Huruf
    "Firman Saputra",
    "Saputri Vitras",
    # Bagian (2) 🗒️
    # 2 Nama : Depan =>6 + Tengah 3 / 4 / 5
    "Nicholas Niken",
    "Ayunada Nila",
    "Amanda Hesti",
    "Helena Vira", # Skip Nama Tengah > Hanya Ditambah Angka [contoh: asu123]
    "Roxanne Kei",
    "Demian Xiu",
    # 2 Nama : Depan 6 + Tengah 2 / 1
    "Adinda St",  # Skip Nama Tengah Karena Hanya Sedikit Karakter
    "Claire M",   # Kecuali Jika Ditambah Angka Lebih Dari 3 [contoh: md12345]
    # Bagian (3) [Kebalikannya dari Bagian (2)] 🗒️
    # 2 Nama : Depan 3 / 4 / 5 + Tengah 6
    "Anya Geraldine",
    "Kayla Amanda",
    "Vina Farady",
    "Ayu Ayummu",  # Skip Nama Depan > Hanya Ditambah Angka [contoh: asu123]
    "Yuna Rahmaa",
    "Rei Mysterio",
    # 2 Nama : Depan 2 / 1 + Tengah 6
    "L Kirana",   # Skip Nama Depan Karena Hanya Sedikit Karakter
    "Vi Alphin",  # Kecuali Jika Ditambah Angka Lebih Dari 3 [contoh: md12345]
    # Bagian (4) 🗒️
    # 2 Nama : Depan 3 / 4 / 5 + Tengah 3 / 4 / 5 Huruf
    "Nadia Sinta",
    "Feryn Fey",
    "Dela Ani",
    "Ayu Dewi",
    # Bagian (5) 🗒️
    # 2 Nama : Depan <=2 + Tengah <=2
    "Ky Ky",
    "Md H",
    "M Ce",
    # [Sesi Triple Name] 📌
# Tidak ada penjelasan lebih terperinci.
# Intinya sama dengan sesi sebelumnya yang juga menangani kasus nama dibawah:
# - nama[0], nama[1], dan nama[2] yang memiliki huruf kurang dari atau sama dengan 2.
# - nama[0], nama[1], dan nama[2] yang memiliki 3 / 4 / 5 huruf.
# - nama[0], nama[1], dan nama[2] yang memiliki huruf lebih atau sama dengan 6.
    # Mencakup Semuanya 🗒️
    "Bagas Eka Apriliyansyah",
    "Ayunanda Nabila Celline",
    "M Irfan Abdullah",
    "Ankara Messi Goat",
    "Zidane M EX",
    "S Mega Chan",
    # Tes sendiri nama yang ingin dicoba.
    # Selesai. 🏁
    # [Sesi Quadruple / Quintuple / Sextuple Name] 📌
    "Abdur Rahman Bin Abdul",
    "Megawati Red Bull Mabar Anjay",
    "Erin Chelstha"
]

for list_name in listname:
    random_id = "10009" + str(rd(111111, 1111111))
    id_user   = random_id + "<=>" + list_name
    idxuser.append(id_user)

for list in idxuser:
    userid   = list.split("<=>")[0]
    fullname = list.split("<=>")[1].lower()
    name     = fullname.split(" ")
    num1     = "123"
    num2     = "321"
    extend1  = "katasandi"
    extend2  = "indonesia"
    try:
        if len(name) == 1:  # Nama dengan 1 kata
            if len(fullname) >= 6:
                password = [
                    fullname,
                    fullname + num1,
                    fullname + num2
                ]
            elif len(fullname) == 3 or len(fullname) == 4 or len(fullname) == 5:
                password = [
                    fullname + num1,
                    fullname + num2
                ]
            elif len(fullname) <= 2:
                password = [
                    extend1,
                    extend2
                ]
        elif len(name) == 2:  # Nama dengan 2 kata
            if len(name[0]) >= 6 and len(name[1]) >= 6:
                password = [
                    fullname,
                    name[0] + name[1],
                    name[0],
                    name[1],
                    name[0] + num1,
                    name[0] + num2,
                    name[1] + num1,
                    name[1] + num2
                ]
            elif len(name[0]) >= 6 and (len(name[1]) == 5 or len(name[1]) == 4 or len(name[1]) == 3):
                password = [
                    fullname,
                    name[0],
                    name[0] + name[1],
                    name[0] + num1,
                    name[0] + num2,
                    name[1] + num1,
                    name[1] + num2
                ]
            elif len(name[0]) >= 6 and len(name[1]) <= 2:
                password = [
                    fullname,
                    name[0],
                    name[0] + name[1],
                    name[0] + num1,
                    name[0] + num2
                ]
            elif (len(name[0]) == 5 or len(name[0]) == 4 or len(name[0]) == 3) and len(name[1]) >= 6:
                password = [
                    fullname,
                    name[1],
                    name[0] + name[1],
                    name[1] + num1,
                    name[1] + num2,
                    name[0] + num1,
                    name[0] + num2
                ]
            elif len(name[0]) <= 2 and len(name[1]) >= 6:
                password = [
                    fullname,
                    name[1],
                    name[0] + name[1],
                    name[1] + num1,
                    name[1] + num2
                ]
            elif (len(name[0]) == 5 or len(name[0]) == 4 or len(name[0]) == 3) and (len(name[1]) == 5 or len(name[1]) == 4 or len(name[1]) == 3):
                password = [
                    fullname,
                    name[0] + name[1],
                    name[0] + num1,
                    name[0] + num2,
                    name[1] + num1,
                    name[1] + num2
                ]
            elif len(name[0]) <= 2 and len(name[1]) <= 2:
                password = [
                    extend1,
                    extend2
                ]
        elif len(name) == 3:  # Nama dengan 3 kata
            if len(name[0]) <= 2 and len(name[1]) <= 2 and len(name[2]) <= 2:
                password = [
                    fullname,
                    name[0] + name[1] + name[2]
                ]
            elif len(name[0]) <= 2 and len(name[1]) <= 2 and (len(name[2]) == 3 or len(name[2]) == 4 or len(name[2]) == 5):
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) <= 2 and len(name[1]) <= 2 and len(name[2]) >= 6:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[2],
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) <= 2 and (len(name[1]) == 3 or len(name[1]) == 4 or len(name[1]) == 5) and len(name[2]) <= 2:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[1] + num1,
                    name[1] + num2
                ]
            elif len(name[0]) <= 2 and (len(name[1]) == 3 or len(name[1]) == 4 or len(name[1]) == 5) and (len(name[2]) == 3 or len(name[2]) == 4 or len(name[2]) == 5):
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[1] + num1,
                    name[1] + num2,
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) <= 2 and (len(name[1]) == 3 or len(name[1]) == 4 or len(name[1]) == 5) and len(name[2]) >= 6:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[1] + num1,
                    name[1] + num2,
                    name[2],
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) <= 2 and len(name[1]) >= 6 and len(name[2]) <= 2:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[1],
                    name[1] + num1,
                    name[1] + num2
                ]
            elif len(name[0]) <= 2 and len(name[1]) >= 6 and (len(name[2]) == 3 or len(name[2]) == 4 or len(name[2]) == 5): 
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[1],
                    name[1] + num1,
                    name[1] + num2,
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) <= 2 and len(name[1]) >= 6 and len(name[2]) >= 6:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[1],
                    name[1] + num1,
                    name[1] + num2,
                    name[2],
                    name[2] + num1,
                    name[2] + num2
                ]
            elif (len(name[0]) == 3 or len(name[0]) == 4 or len(name[0]) == 5) and (len(name[1]) == 3 or len(name[1]) == 4 or len(name[1]) == 5) and len(name[2]) <= 2:
                 password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0] + num1,
                    name[0] + num2,
                    name[1] + num1,
                    name[1] + num2
                ]
            elif (len(name[0]) == 3 or len(name[0]) == 4 or len(name[0]) == 5) and (len(name[1]) == 3 or len(name[1]) == 4 or len(name[1]) == 5) and (len(name[2]) == 3 or len(name[2]) == 4 or len(name[2]) == 5):
                 password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0] + num1,
                    name[0] + num2,
                    name[1] + num1,
                    name[1] + num2,
                    name[2] + num1,
                    name[2] + num2
                ]
            elif (len(name[0]) == 3 or len(name[0]) == 4 or len(name[0]) == 5) and (len(name[1]) == 3 or len(name[1]) == 4 or len(name[1]) == 5) and len(name[2]) >= 6:
                 password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0] + num1,
                    name[0] + num2,
                    name[1] + num1,
                    name[1] + num2,
                    name[2],
                    name[2] + num1,
                    name[2] + num2
                ]
            elif (len(name[0]) == 3 or len(name[0]) == 4 or len(name[0]) == 5) and len(name[1]) <= 2 and len(name[2]) <= 2:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0] + num1,
                    name[0] + num2
                ]
            elif (len(name[0]) == 3 or len(name[0]) == 4 or len(name[0]) == 5) and len(name[1]) <= 2 and (len(name[2]) == 3 or len(name[2]) == 4 or len(name[2]) == 5):
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0] + num1,
                    name[0] + num2,
                    name[2] + num1,
                    name[2] + num2
                ]
            elif (len(name[0]) == 3 or len(name[0]) == 4 or len(name[0]) == 5) and len(name[1]) <= 2 and len(name[2]) >= 6:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0] + num1,
                    name[0] + num2,
                    name[2],
                    name[2] + num1,
                    name[2] + num2
                ]
            elif (len(name[0]) == 3 or len(name[0]) == 4 or len(name[0]) == 5) and len(name[1]) >= 6 and len(name[2]) <= 2:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0] + num1,
                    name[0] + num2,
                    name[1],
                    name[1] + num1,
                    name[1] + num2
                ]
            elif (len(name[0]) == 3 or len(name[0]) == 4 or len(name[0]) == 5) and len(name[1]) >= 6 and (len(name[2]) == 3 or len(name[2]) == 4 or len(name[2]) == 5):
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0] + num1,
                    name[0] + num2,
                    name[1],
                    name[1] + num1,
                    name[1] + num2,
                    name[2] + num1,
                    name[2] + num2
                ]
            elif (len(name[0]) == 3 or len(name[0]) == 4 or len(name[0]) == 5) and len(name[1]) >= 6 and len(name[2]) >= 6:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0] + num1,
                    name[0] + num2,
                    name[1],
                    name[1] + num1,
                    name[1] + num2,
                    name[2],
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) >= 6 and len(name[1]) >= 6 and len(name[2]) <=2:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0],
                    name[0] + num1,
                    name[0] + num2,
                    name[1],
                    name[1] + num1,
                    name[1] + num2
                ]
            elif len(name[0]) >= 6 and len(name[1]) >= 6 and (len(name[2]) == 3 or len(name[2]) == 4 or len(name[2]) == 5):
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0],
                    name[0] + num1,
                    name[0] + num2,
                    name[1],
                    name[1] + num1,
                    name[1] + num2,
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) >= 6 and len(name[1]) >= 6 and len(name[2]) >= 6:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0],
                    name[0] + num1,
                    name[0] + num2,
                    name[1],
                    name[1] + num1,
                    name[1] + num2,
                    name[2],
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) >= 6 and len(name[1]) <= 2 and len(name[2]) <= 2:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0],
                    name[0] + num1,
                    name[0] + num2,
                ]
            elif len(name[0]) >= 6 and len(name[1]) <= 2 and (len(name[2]) == 3 or len(name[2]) == 4 or len(name[2]) == 5):
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0],
                    name[0] + num1,
                    name[0] + num2,
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) >= 6 and len(name[1]) <= 2 and len(name[2]) >= 6:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0],
                    name[0] + num1,
                    name[0] + num2,
                    name[2],
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) >= 6 and (len(name[1]) == 3 or len(name[1]) == 4 or len(name[1]) == 5) and len(name[2]) <= 2:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0],
                    name[0] + num1,
                    name[0] + num2,
                    name[1] + num1,
                    name[1] + num2,
                ]
            elif len(name[0]) >= 6 and (len(name[1]) == 3 or len(name[1]) == 4 or len(name[1]) == 5) and (len(name[2]) == 3 or len(name[2]) == 4 or len(name[2]) == 5):
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0],
                    name[0] + num1,
                    name[0] + num2,
                    name[1] + num1,
                    name[1] + num2,
                    name[2] + num1,
                    name[2] + num2
                ]
            elif len(name[0]) >= 6 and (len(name[1]) == 3 or len(name[1]) == 4 or len(name[1]) == 5) and len(name[2]) >= 6:
                password = [
                    fullname,
                    name[0] + name[1] + name[2],
                    name[0] + name[1],
                    name[0] + name[1] + num1,
                    name[0] + name[1] + num2,
                    name[0],
                    name[0] + num1,
                    name[0] + num2,
                    name[1] + num1,
                    name[1] + num2,
                    name[2],
                    name[2] + num1,
                    name[2] + num2
                ]
        elif len(name) >= 4:  # Nama dengan >= 4 kata
            password = [
                fullname, extend1, extend2,
                name[0] + name[1] + name[2] + name[3]
            ]
        pw = ', '.join(password)
        print(f'Contoh ID: {userid}\nNama: {fullname}\nPass: {pw}\n\n')
    except Exception as e:
        print(e)
