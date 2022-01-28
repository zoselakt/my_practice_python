import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("nado GUI")
root.geometry("640x480")

# 프로그래스 바

# ttk.Progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# #ttk.Progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# ttk.Progressbar.start(10) # 10ms 마다 움직임
# ttk.Progressbar.pack()

# def btncmd():
#     ttk.Progressbar.stop()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): 
        time.sleep(0.01) # 0.01 초 대기
        
        p_var2.set(i)          # 프로그래스 바 값설정
        progressbar2.update()  # ui 업데이트
        print(p_var2.get())    

btn = Button(root, text="시작버튼", command=btncmd2)
btn.pack()

root.mainloop()