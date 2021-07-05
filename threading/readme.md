# Пример взаимодействия Tkinter с Threading #


При изменение параметров виджет-ов в лоб можем получить ошибку от Tkinter
```
Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Python39\lib\threading.py", line 950, in _bootstrap_inner
    self.run()
  File "E:\Разработка\python\tk-thread\mythreadtk.py", line 33, in run
    self._callback(status={'index':self._i, 'label':'Индексируем данные....'})
  File "E:\Разработка\python\tk-thread\mythreadtk.py", line 21, in set_label
    self._label['text'] = status['label']
  File "C:\Python39\lib\tkinter\__init__.py", line 1650, in __setitem__
    self.configure({key: value})
  File "C:\Python39\lib\tkinter\__init__.py", line 1639, in configure
    return self._configure('configure', cnf, kw)
  File "C:\Python39\lib\tkinter\__init__.py", line 1629, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
RuntimeError: main thread is not in main loop
```
Ошибка возникает из-за того что мы пытаемся исправить параметры виджет-ов тогда когда они заняты ткинтером.  
Для решения этой коллизии мы создадим переменные, где будут храниться текущие значения от потока.
Поток в свою очередь будет передавать данные через функцию set_params. Данная функция будем запоминать текущие значения для виджет-ов и не будет мешать ткинтеру
С помощью функции after дождемся своей очереди и присвоим текущие значения переменных виджет-ам.

Этот пример решает проблему взаимодействия с внешним потоком и Tkinter
