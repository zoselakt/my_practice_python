"""
2022.01.08.

내용 : for 문 영문 출력
"""
# A ~ F 출력 / 글자는 순서가 없으니 아스키코드로 실행한다.
# print(ord("A"))
# print(ord("B"))  아스키코드

for i in range (6):
    print(chr(i + 65))
    
#%%
# A ~ F 출력, c는 출력 x / 

for i in range (5):
    if i > 1:
        i += 1
    print(chr(65 + i))
    
   #%%
   
temp = 0
   
for i in range(5):
    temp = i
    temp = temp + 1 if i > 1 else temp
    print(chr(65 + temp))
    
#%%
# aBcDeFgHiJkLmNoPqRsTuVwXyZ 출력
# 아스키코드 97 66 99 등 출력

for i in range(26):
    print(chr(97 + i if i % 2 == 0 else 65 + i), end=" ")