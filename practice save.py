# 홀수, 짝수 구분하기
number = input("1234 >")
last_character = number[-1]

if last_character in "02468":
    print("짝수입니다.")
    
if last_character in "13579":
    print("홀수입니다.")
# ------------------------------------------------------------------------                
# 연습문제 주소: https://codeup.kr/problem.php?id=1165
# 축구의 신
game_time, score = input().split()
game_time = int(game_time)
score = int(score)

if(game_time % 10 == 0):
    final_score = score + int((90 - game_time) / 5)
else:
    final_score = score + int((90 - game_time) / 5) + 1

print(final_score)

# ------------------------------------------------------------------------                
# 연습문제 주소: https://codeup.kr/problem.php?id=1180
# 
std_limit = input()

amount = std_limit[1] + std_limit[0]
amount = int(amount) * 2

if(amount > 99):
    amount = amount % 100

if(amount <= 50):
    print(amount)
    print('GOOD')
else:
    print(amount)
    print('OH MY GOD')


# ------------------------------------------------------------------------                
# 연습문제 주소 : https://wikidocs.net/7030
# 정각구분하기 / 슬라이싱으로 뒤에서 자르기
time = input("현재시간: ")
if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")
# ------------------------------------------------------------------------                
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은?")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")
# ------------------------------------------------------------------------                    
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
종목 = input("종목명: ")
if 종목 in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")    
# ------------------------------------------------------------------------                
# 연습문제 주소 : https://wikidocs.net/7031
# 학점 확인하기
score = input("score: ")
score = int(score)
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")
# ------------------------------------------------------------------------                
# 환율변환하기
exchange = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * exchange[currency], "원")
# ------------------------------------------------------------------------                
number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")
# ------------------------------------------------------------------------                
우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")
# ------------------------------------------------------------------------
num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
# ------------------------------------------------------------------------
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])

# if (시가+변동폭) > 최고가:
#     print("상승장")
# else:
#     print("하락장")