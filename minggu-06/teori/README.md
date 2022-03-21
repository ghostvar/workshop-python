# Penanganan Error dan Exception
> Pertemuan Minggu 6

## Sintak Error

Sintak error, atau dikenal dengan parsing error adalah hal yang paling sering terjadi pada pemrograman tidak hanya pada python. 

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

## Exception

Walaupun suatu statemen atau potongan program secara sintak sudah benar, bisa saja memungkinkan untuk tejadi error. Hal ini dikarenakan kesalahan yang dapat saja terjadi disaat program bekerja bukan kesalahan yang dideteksi ketika proses kompilasi.

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str 
```

## Penanganan Error

Memungkinkan membuat program untuk dapat menangani pengecualian, contoh sebagai berikut,

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

atau penulisan sintak penanganan bersarang,

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

## Statamen `Raise`

statemen `raise` memungkinkan untuk programmer untuk mendefinisikan error tersendiri pada suatu program

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

atau contoh penulisan secara shorthand

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

