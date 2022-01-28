from tkinter import *

root = Tk()
root.title("nado GUI")
root.geometry("640x480")

#라디오 버튼

Label(root, text="메뉴를 선택하세요.").pack()

burger_var = IntVar() # 인트형 var 이여서 정수형 값 출력됨
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="치킨 햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치즈 햄버거", value=3, variable=burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요.").pack()

drink_var = StringVar() # 스트링형 var여서 스트링 값 출력됨
btn_drink1 = Radiobutton(root, text="콜라" , value="콜라" , variable=drink_var)
btn_drink2 = Radiobutton(root, text="사이다" , value="사이다" , variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()