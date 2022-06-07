import tkinter as tk
import sqlite3

class App:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title('案件管理')
        self.master.geometry('500x700')

        # メニュボタン作成
        self.menu = Menu(self.master)
        self.menu.pack(side='top')

    def mainloop(self):
        self.master.mainloop()



class Menu(tk.Frame):
    def __init__(self, master):
        super(Menu, self).__init__(master)

        self.menu_btn = tk.Button(self, text='test')
        self.menu_btn.pack(side='top')

        # ボタンを押した時の処理

class ListArea(tk.Frame):
    def __init__(self, master):
        super(ListArea, self).__init__(master)

        self.listbox = tk.Listbox(self, height=5)
        self.listbox.pack(side='top')

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()