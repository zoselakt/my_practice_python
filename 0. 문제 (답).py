# 문제 1
station = "사당"
print (station + "행 열차가 들어오고 있습니다.")

# 문제 2
from _typeshed import Self
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

# #문제3
url = "http://naver.com"
my_str = url.replace("http://","") # 규칙 1 (http:// 는 제외)
my_str = my_str[:my_str.index(".")] # 규칙 2 (naver 뒤 점부터 제외)
password = my_str[:3]+ str(len(my_str))+ str(my_str.count("e"))+"!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# 문제 4
from random import *
users = range(1, 21) # 1부터 20까지 생성
users = list(users)
shuffle(users)
print(users)
winners = sample(users, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")

# 문제 5
from random import*
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15: # 5~15분 매칭
        print("[O] {0} 번째 손님 (소요시간 : {1} 분)".format(i, time))
        cnt += 1
    else :
        print("[ ] {0} 번째 손님 ( 소요시간 : {1} 분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))

# 문제 6
def std_weight(height, gender): 
    if gender == "남자":
        return height * height * 22
    else : 
        return height * height * 21
height = 175
gender = "남자"
weight = round(std_weight(height / 100 , gender), 2)
print("키 {0} cm {1} 의 표준체중은 {2} kg 입니다.".format(height, gender, weight))

# 문제 7
for i in range(1, 51):
    with open (str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 : ")

# 문제 8
class house:
    #매물초기화
     def __init__(self, location, house_type, deal_type, price, comletion_year):
         self.location = location
         self.house_type = house_type
         self.deal_type = deal_type
         self.price = price
         self.completion_year = comletion_year
      
     #매물정보표시
     def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
            , self.price, self.completion_year)

houses = []
house1 = house("강남", "아파트", "매매","10억","2010년" )
house2 = house("마포", "오피스텔", "전세","5억","2007년" )
house3 = house("송파", "빌라", "월세","500 / 50","2000년" )

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0} 대의 매물이있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
    
# 문제 9
class soldouterror (Exception):
    pass

chicken = 10
waiting = 1 # (대기번호 1부터 시작 / 홀 안에는 현재 만석)
while(True):
    try:
        print("[남은치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken: # 남은치킨보다 주문량이 많을때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0} ] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -=order
        
        if chicken == 0:
            raise soldouterror
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except soldouterror:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break

# 문제 10
# import 1.문제(답)  영어로 된 파일 작성후 진행
# 1.문제(답).sign()

# def sign():
#     print("이 프로그램은 나도코딩에 의해 만들어 졌습니다.")
#     print("유튜브 : http://youtude.com")
#     print("이메일 : nadocoding@gmail.com")