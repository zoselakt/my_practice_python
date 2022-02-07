"""
2022.01.09.

내용: 함수 연습
"""
# 자연수를 음수로
def changeNagative(num):
    result = 0
    if num > 0 :
        result = num * -1
    else:
        result = False
    return result

result = changeNagative(int(input("자연수 : ")));

if not result:
    print("자연수만 가능합니다.")
else:
    print(result)
#%%
# 1~n 까지의 합
def printSum(end):
    result = 0
    for i in range(end):
        result += i + 1
    print(result)
    
printSum(10)
#%%
#홀수를 짝수로 짝수를 홀수로 바꿔주는 메소드
def change(num):
    if num > -1:
        num += 1
    else:
        num = False
    return num

result = change(int(input("정수 : ")))
Msg = ""  # 프린트문 등 반복되는 것이 많을 때 일괄처리 형식으로 사용

if not result:
    Msg = "음수는 불가능합니다."
else:
    if result % 2 == 0:
        Msg = "홀수에서 짝수로 변경되었습니다."
    else:
        Msg = "짝수에서 홀수로 변경되었습니다."
               
print(Msg)
#%%
# 오른차순 정렬 / 변수가 하나일때 반복문 하나 , 둘일때는 두개
numList = [7, 2, 5, 6, 9, 1]

def sortASC(numList):
    for i in range(len(numList) -1):
        for j in range(i +1, len(numList)):
            if numList[i] > numList[j]:
                temp = numList[i]
                numList[i] = numList[j]
                numList[j] = temp
                
sortASC(numList)
print(numList)
#%%
# 정수 중 최대값과 최소값을 구해주는 메소드
def getMaxMin(dataList):
    maxdata = dataList[0]
    mindata = dataList[0]
    resultList = []
    
    for i in range(1, len(dataList)):
        if maxdata < dataList[i]:
            maxdata = dataList[i]
        if mindata > dataList[i]:
            mindata = dataList[i]
    resultList.append(maxdata)
    resultList.append(mindata)
    return resultList
    
dataList = [3, 5, 7, 8]
result = getMaxMin(dataList)
print("최대값 : " + str(result[0]))
print("최소값 : " + str(result[1]))
#%%
#소문자를 대문자로
def changetoupper(string):
    result = ""
    for i in string:
        if ord(i) >= 97 and ord(i) <= 122:
            result += chr(ord(i) - 32)
        else:
            result += i
    return result

print(changetoupper("AsdftttttttttttTT"))
#%%
#한글을 정수로 (일공이사 → 1024)
def changeToInteger(hangle):
    hangle_org = "공일이삼사오육칠팔구"
    result = ""
    for i in hangle:
        result += str(hangle_org.index(i))
    return int(result)

print(changeToInteger("일공이사"))