import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("nado GUI")
root.geometry("640x480")

# 콤보박스

Values = [str(i) + "일" for i in range(1, 32)]
ComboBox = ttk.Combobox(root, height=5, values=Values)
ComboBox.pack()
ComboBox.set("카드결재일") # 최초 띄울 목록 제목

readonly_combobox = ttk.Combobox(root, height=10, values=Values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()

def btncmd():
    print(ComboBox.get()) # 글씨 작성가능
    print(readonly_combobox.get()) # 글씨 작성불가능

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()