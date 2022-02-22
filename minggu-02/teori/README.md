# Pengendali Aliran Program
> Pertemuan Minggu 2

Setelah percobaan statement `while`, Python juga menggunakan aliran program umumnya pada bahasa pemrograman lain.

## Statemen if

```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```
dapat dengan atau tanpa menggunakan `elif`, dan `else` adalah opsional. Sintak `elif` adalah kepanjangan dari `else if` pada bahasa pemrograman umumnya.

## Statemen for

Statement for sedikit berbeda ketimbang pada bahasa pemrograman lainnya mungkin anda terbiasa menggunakan C atau Pascal.

```python
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

Sedikit trik untuk melakukan iterasi dengan koleksi data, mungkin berubah sebuah array atau lainnya.

```python
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

## Fungsi `range()`

Jika ingin melakukan iterasi pada antrian angka, terdapat fungsi bawaan yaitu `range()`.

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

Default parameter pada fungsi `range()` adalah batas akhir dari jumlah antrian angka yang akan dimunculkan; `range(10)` akan mengembalikan nilai iterasi yang berawal dari 0 sampai dengan 9.

```python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]
```

Contoh lain untuk mengkombinasikan fungsi `range()` dan `len()`

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```

## Statemen `break` dan `continue`, dan else pada perulangan

Layaknya pada C, perulangan bisa memiliki sintak `break` dan `continue`.

Serta memungkinkan juga pada python perulangan memiliki sintak `else`, hal ini memungkinkan ketika kondisi perulangan salah maka blok kode proram `else` akan dijalankan.

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

Dan berikut adalah contoh penggunaan `continue` pada python

```python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found an odd number", num)
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

## Statemen `pass`

Statemen `pass` adalah pendefinisian untuk blok program yang tidak melakukan sesuatu, sebagai contoh:

```python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```

Atau pada kelas kosong

```python
>>> class MyEmptyClass:
...     pass
...
```

Atau juga pada suatu pendefinisian fungsi 

```python
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```

## Statemen match

Statement `match` memungkinkan pada kondisi yang memiliki kesamaan dari satu atau lebih nilai,

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

