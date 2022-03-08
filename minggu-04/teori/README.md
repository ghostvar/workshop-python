# Modul di Python
> Pertemuan Minggu 4

Modul dapat diartikan sebagai package pada java atau script yang akan di require pada php.
Hal ini memudahkan pemrograman jika suatu kelompok fungsi digunakan dan dipanggil pada script-script lainnya.

Sebagai contoh kita memiliki file `fibo.py` yang digunakan untuk menampilkan deret angka fibonacci.

```python
def fib(n):    # menuliskan output nilai fibonacci sampai n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # mengembalikan nilai fibonacci sampai n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Menggunakan interpreter python lalu mengetikan berikut,

```python
>>> import fibo
```

Tanpa harus mendefinisikan kembali fungsi tersebut hanya perlu mengimportnya, maka dapat menggunakan langsung dalam interpreter.

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 6.1. Selengkapnya pada Modul

Terdapat variasi dari script import modul, sebagai contoh

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Dimana fibo tidak akan terdefinisi, identik juga dengan kode berikut

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Atau proses import dengan alias dari nama modul tersebut,

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Tentu nama method juga dapat di alias

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 6.1.1 Eksekusi modul sebagai script

Jika melakukan eksekusi file `fibo.py` dengan perintah berikut

```bash
$ python fibo.py <arguments>
```

Maka tidak akan terdapat output pada console, hal ini karena modul tersebut hanya mendefinisikan fungsi dan tidak menjalankannya,

Tambahkan kode berikut,

```python
...
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

Maka ketika dijalankan,

```bash
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

Dan ketika di import pada interpreter script tidak di eksekusi

```python
>>> import fibo
>>>
```

## 6.1.2. Posisi Folder Modul

Jika mengimport modul bernama `spam` interpreter pertama akan mencari pada modul bawaan dengan nama tersebut. Jika tidak ditemukan maka selanjutnya mencari file spam.py pada direktori yang terdapat pada `sys.path. sys.path` atau directori dimana script dipanggil.

## 6.1.3. File Python ter-_kompilasi_

Untuk mempercepat proses kompilasi, Python cache akan mengkompilasi dari module yang telah di import pada folder `__pychache__` dimana file tersebut sudah berformat sebagai file terkompilasi.

## 6.2. Modul Standar

Python secara default telah memiliki modul standar bawaan.

