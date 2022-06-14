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

        # 表示エリア
        self.listarea = ListArea(self.master)
        self.listarea.pack(side='top')

        # 入力エリア
        self.inputarea = InputArea(self.master)
        self.inputarea.pack(side='top')
        self.inputarea.click_add_btn = self.click_add_btn

    def mainloop(self):
        self.master.mainloop()

    def click_add_btn(self):
        todo = self.inputarea.entry.get()
        self.inputarea.entry.delete(0, 'end')
        self.listarea.listbox.insert('end', todo)


class Menu(tk.Frame):
    def __init__(self, master):
        super(Menu, self).__init__(master)

        self.menu_btn = tk.Button(self, text='終了', command=self.end_button)
        self.menu_btn.pack(side='right')

    def end_button(self):
        self.master.destroy()

        # ボタンを押した時の処理

class ListArea(tk.Frame):
    def __init__(self, master):
        super(ListArea, self).__init__(master)

        self.listbox = tk.Listbox(self, height=5)
        self.listbox.pack(side='top')

class InputArea(tk.Frame):
    def __init__(self, master):
        super(InputArea, self).__init__(master)

        self.click_add_btn = None

        self.entry = tk.Entry(self)
        self.entry.pack(side='left')

        self.inputbtn = tk.Button(self, text='追加', command=self._click_add_btn)
        self.inputbtn.pack(side='right', expand=True, fill='x')

    def _click_add_btn(self):
        if self.click_add_btn:
            self.click_add_btn()

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()