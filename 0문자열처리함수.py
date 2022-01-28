#문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # 전체 소문자
print(python.upper()) # 전체 대문자
print(python[0].isupper()) # 첫번째 문자가 대문자인지 아닌지

# len : 길이가 몇자리인지
print(len(python)) 

# replace : 대문자인지 소문자인지도 영향주므로 주의! / 특정글자 변경
print(python.replace("Python", "java")) 

# index : 글자가 몇번째 위치에 있는지
index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index) # 두번째 n 찾기

# find : 함수도 찾기 / 원하는 값이 없으면 -1
print(python.find("java")) 
# print(python.index("java")) 

# count : n 이 몇개 들어있는지.
print(python.count("n")) 

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
#방법4
age = 20
color= "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # f

# 탈출문자 : 문자열 안에서 탈출 / 엔터키, 백스페이스, 줄바꿈 등 효과
print("백문이 불여일견 \n 백견이 불여일타") # \n 줄바꿈 엔터키 효과
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \'나도코딩\'입니다.") # \" 는 출력될때 따옴표표시로 나옴
# \\(역슬러쉬 두개) : 문장 내에서 \하나로 
# \Users\GD\Desktop\pythonworkspace
print("\\Users\\GD\\Desktop\\pythonworkspace")
# \r : 커서를맨 앞으로 이동?? (\r 뒤 문자를 맨앞으로, 변경)
print("Red Apple\rpine")     # 출력시 pine이 red 글자 대체함.
# \b : 백스페이스 (바로 앞 한글자 삭제)
print("redd\b apple")
# \t : 탭
print("red\tapple")

# 슬라이싱 : 앞에서 부터 특정정보만 출력
jumin = "990120-1234567" 
print("성별 : "+jumin[ 7 ])
print("년생 : "+ jumin[0:2]) # 0에서 2번 까지
print("생년월일 : "+ jumin[:6]) # 처음부터 6번까지
print("뒤 7자리 : "+ jumin[7:]) # 7번부터 끝까지

# 확장 슬라이싱 :
number = [1, 2, 3, 4, 5]
print(number[::-1])  # 반대로 출력

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) # 1부터 2씩 더해서 출력