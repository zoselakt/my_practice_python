"""
2022. 01. 08.

내용: 삼항연산자 (if 문)
"""

n1Msg = "첫번째 정수 : "
n2Msg = "두번째 정수 : "

num1 = int(input(n1Msg))
num2 = int(input(n2Msg))

# num1이 num2 보다 크면 num1이 큰값
# num1이 num2 보다 작으면 num2이 큰값
# num2가 더 크거나 num1과 num2가 같으면 false 쪽으로 이동한다

result = num1 if num1 > num2 else "두 수가 같습니다." if num1 == num2 else "두수가 다릅니다."
print("더 큰 값: {}".format(result))
#%%

qmsg = (("당신의 혈액형은 : \n"
         + "1. A형\n2. B형\n3. O형\n4. AB형"))
         
choice = int(input(qmsg + "\n"))
         
answer_a = "세심하다"
answer_b = "거침없다"
answer_o = "사교성이 좋다"
answer_ab= "착하다"
errmsg = "잘못입력했습니다."

result = ((answer_a if choice == 1 else answer_b 
           if choice == 2 else answer_o if choice == 3 else
           answer_ab if choice == 4 else errmsg))

print(result)

#%%
# 일괄처리 / 리펙토리
qmsg = (("당신의 혈액형은 : \n"
         + "1. A형\n2. B형\n3. O형\n4. AB형"))
         
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
else:
    result = errmsg
    
print(result)