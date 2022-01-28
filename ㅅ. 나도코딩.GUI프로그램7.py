from cProfile import label
from distutils import command
from tkinter import *

root = Tk()
root.title("nado GUI")
root.geometry("640x480")

def create_new_file():
    print(" 새파일을 만듭니다.")
    
menu=Menu(root)

Menu_file = Menu(menu, tearoff=0)
Menu_file.add_command(label="New File", command=create_new_file)
Menu_file.add_command(label="New window")
Menu_file.add_separator()
Menu_file.add_command(label="open file...")
Menu_file.add_separator()
Menu_file.add_command(label="Save All", state="disable") # 비활성화
Menu_file.add_separator()
Menu_file.add_command(label="exit", command=root.quit)
menu.add_cascade(label="file", menu=Menu_file)

# 에딧 메뉴 (빈값)
menu.add_cascade(label="edit")

# 언어 메뉴추가(radio 버튼을 통해서 택1)
Menu_lang = Menu(menu, tearoff=0)
Menu_lang.add_radiobutton(label="python")
Menu_lang.add_radiobutton(label="java")
Menu_lang.add_radiobutton(label="c++")
menu.add_cascade(label="Languege", menu=Menu_lang)

# view 메뉴
Menu_view = Menu(menu, tearoff=0)
Menu_view.add_checkbutton(label="show minimap")
menu.add_cascade(label="view", menu=Menu_view)

root.config(menu=menu)
root.mainloop()