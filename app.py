import  tkinter as tk

def btn_click():
    text1 = txtbox.get()
    label = tk.Label(text=text1)
    label.pack()

root = tk.Tk()
root.geometry('700x500')
root.title('タスク管理')

txtbox = tk.Entry(width=20)
txtbox.pack()

button = tk.Button(root,text = '追加',command=btn_click)
button.pack()


root.mainloop()