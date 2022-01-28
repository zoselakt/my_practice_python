#셔플 중괄호 안에 숫자 계속하여 무작위로 변경
from random import *
list = [1,2,3,4,5]
print(list)
shuffle(list)
print(list)
# 샘플 하나 출력
print(sample(list, 1))

# IF : 변수가 맞는지 아닌지
weather = input ("오늘 날씨는 어때요?")
weather = "비"
if weather == "비" or weather == "눈": 
    print("우산을 챙기세요")  
    
# elif : if가 아닌 경우 출력
elif weather == "미세먼지": 
    print("마스크를 챙기세요")
    
#else : 위조건에 아무것도 해당되지 않을때 출력
else : 
    print("준비물은 필요 없어요.") 
temp = int (input("기온은 어때요?"))
if 30<= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp< 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else :
    print(" 너무 추워요. 나가지마세요")
    
# continue / break
absent = [2, 5] 
no_book = [7] 
for student in range(1, 11) :
    if student in absent:
        continue # 계속하여 진행
    elif student in no_book :
        print("{0}는 교무실로 따라와.".format(student))
        break # 뒤에 숫자가 더있어도 끊음.
    print("{0}, 책을 읽어봐".format(student))