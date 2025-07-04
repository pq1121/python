import tkinter
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
from random import randint as rd


class MyArray:

    def __init__(self, size):
        self.__size = size
        self.__array = [rd(1,10000) for i in range(self.__size)]

    def __len__(self):
        return len(self.__array)

    def __getitem__(self, item):
        return self.__array[item]

    def get(self):
        return self.__array


class MyThread(Thread):

    def __init__(self, array, label):
        super().__init__()
        self.__array = array
        self.__label = label

    def run(self):
        self.sort_bubble()

    def sort_bubble(self):
        n = len(self.__array)

        for i in range(n):

            for j in range(0, n - i - 1):

                if self.__array[j] > self.__array[j + 1]:
                    self.__array[j], self.__array[j+1] = self.__array[j+1], self.__array[j]
                    self.__label.configure(text=f"Sorted: {i+1}/{n}")


class Program:

    def __init__(self):

        self.__root = None
        self.__create_window()
        self.__create_widgets()

    def registration_events_buttons(self):
        self.__add_handler_on_click_btn_1(self.__handler_on_click_btn_start)

    def __create_window(self):

        self.__root = tkinter.Tk()
        self.__root.title("Program sort")
        self.__root.geometry("300x200")

    def run(self):
        self.registration_events_buttons()
        self.__root.mainloop()

    def __create_widgets(self):
        self.label_entry = ttk.Label(text="Введите размерность для создания массива")
        self.label_entry.pack(anchor="nw", padx=6, pady=6)
        self.entry = ttk.Entry()
        self.entry.pack(anchor="nw", padx=6, pady=6)
        self.btn_start = ttk.Button(text="Start Sort")
        self.btn_start.pack(anchor="nw", padx=6, pady=6)
        self.output_label = ttk.Label(text="result")
        self.output_label.pack(anchor="nw", padx=6, pady=6)

    def __check_entry(self):

        try:
            value = int(self.entry.get())
            return value
        except ValueError:
            messagebox.showerror("Ошибка", "Введенное значение не является целым числом.")


    def __handler_on_click_btn_start(self):
        size = self.__check_entry()
        if size:
            array = MyArray(size).get()
            tr = MyThread(array, self.output_label)
            tr.start()

    def __add_handler_on_click_btn_1(self, handler):
        self.btn_start.configure(command=handler)



if __name__ == "__main__":
    app = Program()
    app.run()