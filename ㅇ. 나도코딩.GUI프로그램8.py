from distutils.log import error
from tkinter import messagebox
from tkinter import *

from django.http import response

root = Tk()
root.title("nado GUI")
root.geometry("640x480")
# 메세지 박스
def info():
    messagebox.showinfo("알림", "정상적으로 예매 되었습니다.")
def warn():
    messagebox.showwarning("경고", "정상적으로 예매되지 않았습니다.")
def error():
    messagebox.showerror("에러", "결재 오류가 발생했습니다.")
    
def okcancel():
    messagebox.askokcancel("주의", "해당좌석은 유아동반석입니다.")
def retrycancel():
    messagebox.askretrycancel("재시도", "다시시도하겠습니까.")
def yesno():
    messagebox.askyesnocancel("예/아니오" , " 해당좌석은 역방향입니다.")
    
def yesnocancel():
    messagebox.askokcancel(title=None, message="예매 내역이 저장되지 않았습니다. \n 저장 후 프로그램을 종료하겠습니까?")
    # 예- true / 아니오- false / 그외-none
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소 취소")
    
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="에러").pack()
Button(root, command=retrycancel, text="재시도").pack()
Button(root, command=yesno, text="예 / 아니오").pack()

Button(root, command=yesno, text="예 / 아니오 / 취소").pack()

root.mainloop()