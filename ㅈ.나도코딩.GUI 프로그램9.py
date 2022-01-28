from cProfile import label
from distutils import command
from tkinter import *

root = Tk()
root.title("nado GUI")
root.geometry("640x480")

#프레임

Label(root, text="메뉴를 선택해 주세요.").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)
#                    왼쪽 정렬  채우기= 양쪽   중앙까지 확장

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()


root.mainloop()
