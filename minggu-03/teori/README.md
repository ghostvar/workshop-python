# Struktur Data
> Pertemuan Minggu 3

## 5.1. Selengkapnya Lists

Tipe data ini memiliki beberapa method, diantaranya:

* __list.append(x)__

Menambah x pada akhir list. Identik dengan a[len(a):] = [x].

* __list.extend(iterable)__

Memperpanjang list dengan menambahkan iterable pada setiap item. Identik dengan a[len(a):] = iterable.

* __list.insert(i, x)__

Menyisipkan x pada posisi index i. Parameter pertama adalah posisi index yang akan di sisipkan, jadi a.insert(0, x) akan menyisipkan di awal list, dan a.insert(len(a), x) identik dengan a.append(x).

* __list.remove(x)__

Menghapus item diawal yang memiliki nilai x. Jika terdapat ValueError item tersebut tidak terdapat pada list.

* __list.pop([i])__

Menghapus item pada posisi index i pada list, dan mengembalikannya. jika tidak terdapat index, a.pop() menghapus dan mengembalikan item terakhir pada list. Notasi ini sering terlihat pada refrensi Python Library.)

* __list.clear()__

Menghapus semua item pada list. Identik dengan del a[:].

* __list.index(x[, start[, end]])__

Mengembalikan index basis-nol pada list pada item pertama dimana nilai sama dengan x. Akan terdapat ValueError jika tidak ditemukan value.

Parameter opsional start dan end adalah notasi untuk interpreter dan digunakan untuk antrian pencarian pada list. Nilai index yang dikembalikan relatif dari awal dari antrian penuh dari pada argument start.

* __list.count(x)__

Mengembalikan berapa kalinya x tampil pada list.

* __list.sort(*, key=None, reverse=False)__

Pengurutan pada list (parameter digunakan untuk kostumisasi).

* __list.reverse()__

Membalikan urutan pada list.

* __list.copy()__

Mengembalikan salinan dari list. Identik dengan a[:].

## 5.1.1 Menggunakan List sebagai Stacks

Pada method-method list mempermudah penggunaan list sebagai stack, dimana element terakhir yang masuk adalah element pertama yang keluar (last-in, first-out), sebagai contoh:

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

## 5.1.2. Menggunakan list sebagai Antrian

Dan juga mudah digunakan untuk antrian dimana element pertama yang masuk adalah element pertama yang keluar (first-in, first-out), sebagai contoh:

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

## 5.1.3. List Comprehensions

List Comprehensions adalah metode peringkasan dalam pembuatan list. Umumnya aplikasi akan membuat list dari nilai kembalian atau iterasi dari suatu operasi dan nilai akan di tambahkan pada per iterasi tersebut. Sebagai contoh:

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Dengan cara diatas sebuah variabel bernama `x` akan tetap tampil sebagai variabel terdeklarasi walaupun perulangan telah berakhir. Tapi pada python jika diringkas maka dapat menggunakan kode berikut,

```python
squares = list(map(lambda x: x**2, range(10)))
```

atau Identik dengan,

```python
squares = [x**2 for x in range(10)]
```

## 5.1.4. Nested List Comprehensions

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

## 5.2. Statement del

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

## 5.3. Tuples and Sequences

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples mungkin menyusup:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples tidak dapat dimutasi:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # tapi dapat membawa object termutasi:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

## 5.4. Sets

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # menampilkan duplikasi
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # testing komposisi
True
>>> 'crabgrass' in basket
False

>>> # Contoh penggunaan operasi set pada huruf unik pada dua kata
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique huruf pada a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # huruf pada a tapi tidak pada b
{'r', 'd', 'b'}
>>> a | b                              # huruf pada a atau b atau keduanya
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # huruf pada kedua a dan b
{'a', 'c'}
>>> a ^ b                              # huruf pada a atau b tapi tidak keduanya
{'r', 'd', 'b', 'm', 'z', 'l'}
```

## 5.5. Dictionaries

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

## 5.6. Looping Techniques



```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

## 5.7. More on Conditions

Kondisi operator pada `if` dan `while` dapat bebas digunkan dengan apa saja, tidak hanya dengan komparasi.

```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

## 5.8. Komparasi Sequences dengan Tipe lain

Object sequence dapat dikomparasi dengan tipe yang lain. Komparasi menggunakan _lexicographical_ ordering: Pertama, terdapat dua item dikomparasi jika berbeda maka digunakan sebagai acuan komparasi, dan jika sama, maka kedua item berikutkan dikomparasi begitu seterusnya.

```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
