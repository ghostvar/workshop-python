# I/O pada Python
> Pertemuan Minggu 5

Terdapat beberapa metode untuk menampilkan output serta penyimpanan file untuk keperluan lainnya,

## Pemformatan yang mudah

Penulisan output dapat menggunakan beberapa cara, diantaranya dengan fungsi `print()`, `write()`, atau standar output dengan menggunakan `sys.stdout`.

Proses pemformatan juga terdapat cara diantaranya

 - Diawali dengan `f` didepan string, lalu menambah ekpresi `{` dan `}`

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
```

 - Menggunakan `str.format()`, sama halnya dengan cara pertama menggunakan `{` dan `}` akan tetapi dengan tambahan model formating dari data yang akan di tampilkan

```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
```

Terdapat contoh lain diantaranya

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

## Metode format dengan perintah `format()`

Dasar penggunakan method ini sebagai contoh
```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

atau dapat juga berupa seperti kode berikut

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

## Membaca file

Dapat menggunakan perintah berikut

```python
f = open('workfile', 'w')
```

## Menyimpan struktur data dengan json

Python juga dapat menyimpan data dengan format json yaitu seperti contoh kode berikut

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```