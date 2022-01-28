#리스트 (list)
subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호")) # 조세호 몇 번째 칸에 있는지

# append : 맨뒤에 추가
subway.append("하하") 
print(subway) 

# insert : 문자사이추가
subway.insert(1, " 정형돈") # 1번 뒤에 추가하기
print(subway)

# pop : 맨뒤가 삭제됨
print(subway.pop()) 
print(subway) 
print(subway.pop()) # 계속 뒤에서부터 제거됨
print(subway)

# count : 같은 이름 몇번나오는지.
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# sort : 순서대로 정렬
num_list = [2,7,5,3,4,1,6]
num_list.sort()
print(num_list)

# reverse : 순서 반대 정렬
num_list.reverse()
print(num_list)

# clear : 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [2,7,5,3,4,1,6]
mix_list = ["조세호", 20, True]
print(mix_list)

# extend : 리스트 확장
num_list.extend(mix_list)
print(num_list)

# list.remove() : 리스트 요소제거
num_list.remove(20)
print(num_list)

# list.index() : 리스트에 ()안 값이 있으면 ()안에 위치 값을 돌려준다.
num_list.index("조세호")
print(num_list)

# join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" / ".join(interest))