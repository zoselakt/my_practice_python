#지역 변수 : 함수내에서 할당되어야만 출력되고 함수밖에 있는 수는 출력 안됨
gun = 10
def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}",format(gun))
print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명 제외
print("남은 총 : {0}".format(gun))

# 전역 변수 : 함수밖에 있는 수도 출력
gun = 10
def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}",format(gun))
print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명 제외
print("남은 총 : {0}".format(gun))
# return으로 함수내에서 빼내기
def checkpoint_ret (gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}",format(gun))
    return gun
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
