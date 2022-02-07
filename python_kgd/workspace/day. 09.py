"""
2022. 01. 09.

내용 : 자료의 구조
"""
# list 는 변할 수 있음. / 규칙성없는 값에 규칙성을 부여하기 위해사
DataList1 = [1, 2, 3]
DataList2 = DataList1

DataList2.append(4)

print(DataList1)
#%%
# tuple 은 변할 수 없음.
DataTuple1 = (1, 2, 3)
DataTuple2 = DataTuple1

DataTuple2 += 4, 5

print(DataTuple1)
#%%
# dictionery 는 한쌍으로 저장되어 관리한다.
# len()을 사용하면 한 쌍을 1로 카운트 한다
# 검색 
# 키값 + in + dict명 : 키 값이 있으면 참
# 키값 + not in + dic명 : 키 값이 없으면 참

# 등급을 입력받아 학점을 출력해주는 프로그램
# 1~5 등급 / A~F 학점

scoreDict = {}
for i in range(5):
    scoreDict[i+1] = chr(i + 66) if i == 4 else chr(i + 65)
    
rating = int(input("내 등급은 : "))

for i in range(5):
    if rating == i+1:
        print(scoreDict[rating] + "학점 입니다.")
        break
#%%
# 딕셔너리 안에 리스트
numDict = {"even" : [2, 4, 6], "odd" : [1, 3, 5]}
for i in numDict["even"]:
    print(i)

#  딕셔너리 안에 리스트 2개
numListDict = {"1학년" : [[30, 40, 50], [80, 90, 10]]}
for i in numListDict["1학년"]:
    for j in i:
        print(j)
    print("==============")