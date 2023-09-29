## 00. Tentang

Memfilter atau menangani nama-nama untuk mengevaluasi nilai tersebut menjadi sebuah string kombinasi password berdasarkan jenis nama yang dibaca.

Pada dasarnya hanya ada 3 kemungkinan kode ini dapat berkerja dalam memfilter jenis nama, diantaranya adalah:
- Nama yang memiliki karakter lebih atau sama dengan 6 `(>=)`
- Nama yang memiliki karakter kurang dari atau sama dengan 2 `(<=)`
- Nama yang memiliki karakter sama dengan 3 / 4 / 5 `(==)`

## 01. Keterangan
> **Nama 1 Kata**
- 1A. `nilai[0] >= 6` :

      Nabila 
      Chyntia 
      Veronica

- 1B. `nilai[0] == 3 / 4 / 5` :

      Sinta
      Yudha
      Nadia
      Fina
      Dela
      Vina
      Tya
      Ayu
      Ria

- 1C. `nilai[0] <= 2` :

      Dy  
      Md 
      Y

> **Nama 2 Kata**
- 2A. `nilai[0] >= 6` dan `nilai[1] >= 6` :

      Firman Saputra
      Saputri Vitras

- 2B. `nilai[0] >= 6` dan `nilai[1] == 3 / 4 / 5` :

      Nicholas Niken 
      Ayunada Nila  
      Amanda Hesti 
      Helena Vira 
      Roxanne Kei
      Demian Xiu

- 2C. `nilai[0] >= 6` dan `nilai[1] <= 2` :

      Adinda St
      Claire M

- 2D. `nilai[0] == 3 / 4 / 5` dan `nilai[1] >= 6` :

      Anya Geraldine
      Kayla Amanda
      Vina Farady
      Ayu Ayummu
      Yuna Rahmaa
      Rei Mysterio

- 2E. `nilai[0] <= 2` dan `nilai[1] >= 6` :

      L Kirana | Vi Alphin

- 2F. `nilai[0] == 3 / 4 / 5` dan `nilai[1] == 3 / 4 / 5` :

      Nadia Sinta
      Feryn Fey
      Dela Ani
      Ayu Dewi

- 2G. `nilai[0] <= 2` dan `nilai[1] <= 2` :

      Ky Ky
      Md H 
      M Ce

> **Nama 3 Kata**
- Tidak ada penjelasan lebih terperinci.
  Intinya sama dengan sesi sebelumnya yang juga menangani kasus nama dibawah:
  - `nama[0]`, `nama[1]`, dan `nama[2]` yang memiliki huruf kurang dari atau sama dengan 2 `<= 2`.
  - `nama[0]`, `nama[1]`, dan `nama[2]` yang memiliki `3 / 4 / 5` huruf.
  - `nama[0]`, `nama[1]`, dan `nama[2]` yang memiliki huruf lebih atau sama dengan 6 `>= 6`.
- Mencakup semua nama 3 Kata

      Bagas Eka Apriliyansyah
      Ayunanda Nabila Celline
      M Irfan Abdullah
      Ankara Messi Goat
      Zidane M EX
      S Mega Chan
      DAN LAINNYA!

# 02. Penerapan
- Contoh 1
  - Perhatikan jumlah abjad (karakter)

        M Abdullah Sahad

    - `nama[0] <= 2`, `nama[1] >= 6`, `nama[2] == 5`.
- Maka `kombinasi password` yang akan diperoleh

      m abdullah sahad
      mabdullahsahad
      abdullah
      abdullah123
      abdullah321
      sahad123
      sahad321

- Contoh 2
  - Perhatikan jumlah abjad (karakter)

        Karina Nadila
    
    - `nama[0] >= 6`, `nama[1] >= 6`.

- Maka `kombinasi password` yang akan diperoleh

      karina nadila
      karinanadila
      karina
      nadila
      karina123
      karina321
      nadila123
      nadila321

- Contoh 3
  - Perhatikan jumlah abjad (karakter)

        Via Deliya
    
    - `nama[0] <= 2`, `nama[1] >= 6`.

- Maka `kombinasi password` yang akan diperoleh

      via deliya
      viadelia
      via123
      via321
      delia
      delia123
      delia321

- Contoh 4
  - Perhatikan jumlah abjad (karakter)

        M Vi Alip
    
    - `nama[0] <= 2`, `nama[1] <= 2`, `nama[2] == 4`.

- Maka `kombinasi password` yang akan diperoleh

      m vi alip
      mvalip
      alip123
      alip321

# 03. Kesimpulan.
Mengapa demikian password yang dihasilkan bisa berbeda tergantung jumlah karakter nama? karena pada dasarnya Facebook hanya memperbolehkan pengguna menggunakan password dengan minumum jumlah karakter adalah 5.

Dengan menambah blok pengecualian yang ada dikode ini dapat mengevaluasi dan memfilter value yang didapat dari hasil `dump id` kalian kemudian menjadikannya kombinasi password yang sempurna.

# 04. Akhir.
- Kelebihan(+)
  - Proses loop lebih efisien karena tidak perlu ada percobaan login pada akun yang menggunakan nama yang masuk dalam kategori password kurang dari 5 karakter.
- Kekurangan(-)
  - Proses maintenance kode akan sedikit memakan waktu. Dengan mengimplementasikan kode ini kedalam project bruteforce milik anda artinya anda menambahkan 300+-Line baru untuk kode ini. lol
 
# 05. Once again.
Sebenernya masih banyak yang harus dijelaskan tapi yaudah lah, run aja kodenya di terminal kalian dan pahami sendiri. Sederhana kok!
#### Males ngetiknya panjang lebar, hehe.