import  tkinter as tk

class App:
    def __init__(self):
        # ウィンドウを初期化
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400x300')
        self.master.configure(padx=16, pady=16)

        # 入力エリア作成
        self.input_area = InputArea(self.master)
        self.input_area.pack(side='top', fill='x')
        self.input_area.click_add_btn = self.click_add_btn

        # 表示エリア作成
        self.list_area = ListArea(self.master)
        self.list_area.pack(side='bottom', expand=True, fill='both')
    
    def mainloop(self):
        self.master.mainloop()

    def click_add_btn(self):

        todo = self.input_area.entry.get()
        self.input_area.entry.delete(0, 'end')
        self.list_area.listbox.insert('end', todo)

class ListArea(tk.Frame):
    """
    リストの表示エリア
    入力したTODOが表示される
    """
    def __init__(self, master):
        super(ListArea, self).__init__(master)

        # リストの作成
        self.listbox = tk.Listbox(self, height=5)
        self.listbox.pack(side='top', expand=True, fill='both')

        # 削除ボタンの追加
        self.del_btn = tk.Button(self, text='削除', command=self._click_del_btn)
        self.del_btn.pack(side='bottom', fill='x')
    
    def _click_del_btn(self):

        sel = self.listbox.curselection()
        for i in sel[::-1]:
            self.listbox.delete(i)

class InputArea(tk.Frame):

    def __init__(self, master):
        super(InputArea, self).__init__(master)

        self.click_add_btn = None

        # ラベルの作成
        self.label = tk.Label(self, text='TODO')
        self.label.pack(side='left')

        # 入力行の作成
        self.entry = tk.Entry(self)
        self.entry.pack(side='left', expand=True, fill='x')

        # 追加ボタンの作成
        self.add_btn = tk.Button(self, text='追加', command=self._click_add_btn)
        self.add_btn.pack(side='left')
    
    def _click_add_btn(self):
        if self.click_add_btn:
            self.click_add_btn()

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()