# -*- coding: utf-8 -*-
"""
2022.01.08.

내용 : while 연습
"""

qmsg = (("당신의 혈액형은 : \n"
         + "1. A형\n2. B형\n3. O형\n4. AB형\n5. 나가기"))
while True:       
    choice = int(input(qmsg + "\n"))
             
    answer_a = "세심하다"
    answer_b = "거침없다"
    answer_o = "사교성이 좋다"
    answer_ab= "착하다"
    errmsg = "잘못입력했습니다."
    
    if choice == 1:
        result = answer_a
    elif choice == 2:
        result = answer_b
    elif choice == 3:
        result = answer_o
    elif choice == 4:
        result = answer_ab
    elif choice == 5:
        break
    else:
        result = errmsg
        
    print(result)
    