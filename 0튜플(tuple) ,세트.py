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

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # 대괄호 / 클래스 set
menu = list(menu)
print(menu, type(menu)) # 중괄호 / 클래스 list
menu = tuple(menu)
print(menu, type(menu)) # 소괄호 / 클래스 tuple