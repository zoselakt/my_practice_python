# 사전 자료형 : 키에 중복을 허용하지 않는다.
from functools import partial
cabinet = {3: "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[5]) # 대괄호[]는 값이 없으면 키 에러 문자와 수식이 종료
#print(cabinet.get(5)) # 중괄호는 ()값이 없으면 none이라는 문자가 출력
print(cabinet.get(5, "사용가능")) # 5번 을 찾으려하고 사용가능 문자가 출력
print(3 in cabinet) # 3 이 있으면 트루 없으면 폴스

closet = {"A-3": "유재석", "B-100" : "김태호"}
print(closet["A-3"])
# 새 손님
print(closet)
closet["A-3"] = "김종국" # 변경되여 출력
closet["C-200"] = "조세호" # 추가되어 출력
print(closet)
# 간 손님
del closet["A-3"]
print(closet)
# 현재 키만 출력
print(closet.keys())
#키, value 쌍으로 출력
print(closet.items())
# 모든값삭제
closet.clear()
print(closet)


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