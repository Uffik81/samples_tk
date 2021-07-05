# Пример решения задачи: выполнение фоновой задачи с взаимодействием с Tkinter-ом

from tkinter import *
import tkinter.ttk as ttk

from time import sleep
from threading import Thread


class WinMain1(Tk):
    def __init__(self):        
        super().__init__()
        self.resizable(False,False)
        # Параметры которые будем изменять
        self._status = ''
        self._index = 0
        self._label = Label(self,text='')
        self._label.pack()
        self._pb = ttk.Progressbar(self, length=100)
        self._pb.pack()
        self.after(10, self.after_callback)

    def after_callback(self):
        # Обновляем параметры в соответствии с полученными данными потока
        self._label['text'] = self._status
        self._pb['value'] = self._index
        self.after(10, self.after_callback)
        pass

    def set_params(self, status ):
        # Передаем параметры от потока
        self._status = status['label']
        self._index = status['index']
        pass

class ThreadApp(Thread):
    def __init__(self,callback):
        super().__init__()
        self._i = 0
        self._runs = True
        self._callback = callback # Передаем потоку функцию для передачи параметров

    def run(self):
        # 
        if self._callback is not None:
            while self._runs:            
                self._callback(status={'index':self._i, 'label':'Индексируем данные....'})
                sleep(1)
                self._i += 1
                if self._i > 100 :
                    self._runs = False
                    # Либо break
            print('Изменен статрус _runs')

if __name__ == '__main__':
    # Создаем форму
    myapp = WinMain1()
    # Создаем поток
    mythread = ThreadApp(callback=myapp.set_params)

    mythread.start()
    myapp.mainloop()
    # Сообщаем потоку, что мы закрыли форму 
    # это примитивный вариант
    mythread._runs = False
