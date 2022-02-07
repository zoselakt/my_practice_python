"""
2022. 01. 09

@ 내용 : list 연습
"""
# c 제외 f까지

dataList = [""] * 5

temp = 0

for i in range(len(dataList)):
    temp = i
    if temp > 1:
        temp += 1
    dataList[i] = chr(65 + temp)
    
print(dataList)

#%%
# a ~ z 까지 

DataList = [""] * 26

for i in range(len(DataList)):
    DataList[i] = chr(97 + i if i % 2 == 0 else 65 + i)
    
print(DataList)
    
#%% 
#자연수를 한글로 변경

# 1) 1024 % 10 == 4
# 2) 1024 // 10 == 102
# 3) 102 % 10 == 2
#         .
#         .
#         .

num = int(input("자연수 입력 : "))
hangle = "공일이삼사오륙칠팔구"
result = ""

while num != 0:
    result = hangle[num % 10] + result
    num = num // 10
    
print(result)