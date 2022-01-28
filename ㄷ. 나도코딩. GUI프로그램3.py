from tkinter import *

root = Tk()
root.title("nado GUI")
root.geometry("640x480")

# list 박스
Listbox = Listbox(root, selectmode="extended", height=0) # single함수는 하나만 선택
Listbox.insert(0, "사과")
Listbox.insert(1, "딸기")
Listbox.insert(2, "바나나")
Listbox.insert(END, "수박")
Listbox.insert(END, "포도")
Listbox.pack()

def btncmd():
    # Listbox.delete(0)  #삭제
    
    # 갯수확인
    # print("리스트에는" , Listbox.size(), "개가 있어요.")
    
    # 항목확인
    # print("1번째부터 3번째까지의 항목 : ", Listbox.get(0, 2))  # 시작값, 끝값
    
    # 선택된 항목확인
    print("선택된 항목 : ", Listbox.curselection())
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

# --------------------------------------------------------------------------
# 체크박스

chlvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chlvar)
# chkbox.select() # 자동선택처리
# chkbox.deselect() # 선택해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지않기", variable=chkvar2)
chkbox2.pack()

def btncmd1():
    print(chlvar.get()) # 0: 체크해제, 1: 체크
    print(chkvar2.get())

root.mainloop()