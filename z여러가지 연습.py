python = "Python is Amazing"
print(python.lower()) # 전체 소문자
print(python.upper()) # 전체 대문자
print(python[0].isupper()) # 첫번째 문자가 대문자인지 아닌지

# find : 함수도 찾기 / 원하는 값이 없으면 -1
print(python.find("java")) 
# print(python.index("java")) 

# ------------------------------------------------------------------------                
# 별 표현식
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score)
# ------------------------------------------------------------------------                


# ------------------------------------------------------------------------    
#문자열 포맷 / # 숫자든 문자든 %s쓰면됨
print("나는 %d살입니다." % 20)  # %d = 정수값 출력
print("나는 %s을 좋아해요" % "파이썬")  # %s = 문자열
print("Apple은 %c로 시작해요." %"A") # %c = c 는 캐릭터
print("나는 %s색과 %s 색을 좋아해요."%("파란", "빨강")) # 숫자든 문자든 %s쓰면됨
#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {} 색을 좋아해요.".format ("파란", "빨강"))
print("나는 {1}색과 {0} 색을 좋아해요.".format ("파란", "빨강")) # {} 숫자 넣으면 순서대로
#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color = "빨강"))
#방법4 : f-string
age = 20
color= "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # f

# 탈출문자 : 문자열 안에서 탈출 / 엔터키, 백스페이스, 줄바꿈 등 효과
# \\(역슬러쉬 두개) : 문장 내에서 \하나로 
# \Users\GD\Desktop\pythonworkspace
print("\\Users\\GD\\Desktop\\pythonworkspace")
# \r : 커서를맨 앞으로 이동?? (\r 뒤 문자를 맨앞으로, 변경)
print("Red Apple\rpine")     # 출력시 pine이 red 글자 대체함.
# \b : 백스페이스 (바로 앞 한글자 삭제)
print("redd\b apple")


# ------------------------------------------------------------------------    
# list
num_list = [2,7,5,3,4,1,6]

# list.index() : 리스트에 ()안 값이 있으면 ()안에 위치 값을 돌려준다.
num_list.index("조세호")
print(num_list)

# join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" / ".join(interest))


# ------------------------------------------------------------------------    
# dict
icecream = {"메로나" : 1000, "폴라포":1200, "빵빠레": 1800}

# 딕셔너리 연습
icecream = {"메로나" : 1000, "폴라포":1200, "빵빠레": 1800}

# 두개 추가하려면 두번 작성해야함.
icecream ["죠스바"] = 1200 
icecream ["월드콘"] = 1500
print(icecream)

# 딕셔너리 출력
icecream = {"메로나" : 1000, "폴라포":1200, "빵빠레": 1800, "죠스바" : 1200, "월드콘" : 1500}

print("메로나 가격: ", icecream["메로나"])
# 내용 수정 / 삭제
icecream = {"메로나" : 1000, "폴라포":1200, "빵빠레": 1800, "죠스바" : 1200, "월드콘" : 1500}
icecream["메로나"] =1300 # 수정
del icecream["메로나"]  # 삭제
print(icecream)
# 내용 추가
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
inventory ["월드콘"] = [500, 7] #추가
print(inventory)
# 키값출력 / values 값 출력, 총합
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())  
# ice = list(icecream.values())
print(ice)
print(sum(icecream.values())) #총합

# update 함수 / 딕셔너리에 추가
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# dic / zip
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
# 출력 값 : {'apple': 300, 'pear': 250, 'peach': 400}

# 콤마를 중간으로 값을 나눔 / 키 + value , 키 + value
print(icecream.items())

# clear : 모든값삭제
icecream.clear()
print(icecream)

cabinet = {3: "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]) # 대괄호[]는 값이 없으면 키 에러 문자와 수식이 종료
# print(cabinet.get(5)) # 중괄호는 ()값이 없으면 none이라는 문자가 출력
print(cabinet.get(5, "사용가능")) # 5번 을 찾으려하고 사용가능 문자가 출력
print(3 in cabinet) # 3 이 있으면 트루 없으면 폴스

dictionary = {
    "name" :  " 7D 건조 망고",
    "type" : "당절임" ,
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])


# ------------------------------------------------------------------------    
# tuple
# 튜플 - 변경되지 않는 목록
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 세트 (집합) / 중복 단어 출력안됨, 순서없음
my_set = {1,2,3,3,3}
print(my_set)
# 교집합 (java 와 python 모두 할 수 있는 사람.)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
print(java & python)
print(java.intersection(python))
# 합집합 (java 또는 python 할수있는 사람.)
print(java|python)   # | 는 shift + \ (빽스페이스 바로 옆)
print(java.union(python))
# 차집합 (둘중 하나 java 또는 python 중 하나만 가능)
print(java - python)
print(java.difference(python))
#python 수식에 추가
python.add("김태호")
print(python)
#java 수식에서 제거
java.remove("김태호")
print(java)

# ------------------------------------------------------------------------        
# for문
array = [273, 23, 103, 45, 52]

for i in range(len(array)):
    print("{} 번째 반복: {}".format(i, array[i]))
# ------------------------------------------------------------------------    
# 한줄 for (출석번호 1,2,3,4 앞에 100을 붙이기)
students = [1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)
# ------------------------------------------------------------------------            
# 이중 for 문 행렬만들기
il = [[1,2,3,4], [5,6,7,8]]

for i in range(len(il)): # i = 0, 1
    for j in range(len(il[i])): # j = 0, 1, 2, 3
        print(il[i],[j], end= " ")
    print()
# ------------------------------------------------------------------------        
score_list = [90, 45, 70, 60, 55]
number = 1

for score in score_list:
    if 60 <= score:
        print("{} 번 학생은 합격입니다.".format(number))
    elif 60 >= score:
        print("{} 번 학생은 불합격입니다.".format(number))
    number += 1


while True:
    num1 = int(input("첫 번째 정수 입력 : "))
    num2 = int(input("두 번째 정수 입력 : "))
    
    if num1 == 0 and num2 == 0:
        break
    
    print("두 수의 합 : {} ".format(num1 + num2))
# ------------------------------------------------------------------------            
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print(end="")
        
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
# ------------------------------------------------------------------------    
money = int(10000)
percent = [10, -10, 5, -5]

basemoney = money

for i in percent:
    money += money*i/100
    print("{0} 원을 투자했습니다.".format(money))

money = float("{0:.0f}".format(money))

print("최종금액으로 {}원이 되었습니다.".format(money))

if money > basemoney:
    print("good")
elif money == basemoney:
    print("samesame 2")
elif money < basemoney:
    print("bad")