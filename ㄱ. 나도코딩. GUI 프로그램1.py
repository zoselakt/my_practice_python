from tkinter import *

root = Tk()
root.title("nado GUI")
root.geometry("640x480") 

# ------------------------------------------------------------------------                
# 레이블
label1 = Label(root, text="안녕하세요.")
label1.pack()

photo = PhotoImage(file="pang/gui.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    
    global photo2 # 이미지 변경
    photo2 = PhotoImage(file="pang/gui change.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭" , command=change)
btn.pack()
# ------------------------------------------------------------------------                
# 버튼
# 텍스트가 많아지면 자동으로 커진다.
btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=5, pady=10, text="버튼333333333333333")
btn3.pack()
# 텍스트에 상관없이 크기 고정
btn4 = Button(root, width=10, height=10, text="버튼444444444444444")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼 5")
btn5.pack()

photo = PhotoImage(file="pang/gui.png")  # file = "경로 / 사진이름"
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었습니다.")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
# ------------------------------------------------------------------------                
# ------------------------------------------------------------------------                