# Responsi Workshop Python
> Responsi Ujian Akhir Semester

Adapun soal yang telah di tentukan, yaitu membuat script `responsi.py` untuk mendownload dan menampilkan sebagian dari data yang telah di tentukan pada url pada file `url.md` pada repo.

## Import Paket

Dari script yang telah dibuat terdapat dua paket yang dibutuhkan yaitu `request` untuk melakukan request data json, dan `json` untuk melakukan validasi terhadap data json yang di request.

## Method-method

Terdapat 3 method diantaranya `is_json()` untuk melakukan validasi json, `parsing()` untuk menampilkan sebagian dari data yang telah di request, dan terakhir `save_to_file()` untuk menyimpan isi content json kedalam sebuah file.

## Cara Kerja Program

Program pertama-tama membaca isi dari file `url.md` untuk menentukan enpoint json dan nama file, kemudian melakukan request menggunakan fungsi `get()` dari paket request.

Ketika respon dari request valid dan pengecekan `is_json()` juga valid, selanjutnya adalah parsing dari method `parsing()` yang telah dibuat untuk menampilkan sebagian dari data.

Terakhir adalah menyimpan data menggunakan method `save_to_file()` yang telah dibuat dan nama file yang telah di tentukan.

Script memiliki beberapa Error Handling untuk menangani error-error seperti gagal melakukan request, json tidak valid dan semacamnya.

Terimakasih.