from tkinter import *

root = Tk()
root.title("nado GUI")
root.geometry("640x480")

# 텍스트/엔트리
# 텍스트
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요.")

# 엔트리
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력하세요")


def btncmd():
    # 내용출력
    print(txt.get("1.0", END))
    print(e.get())
    # 내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)
    
btn8 = Button(root, text="클릭", command=btncmd)
btn8.pack()

root.mainloop()