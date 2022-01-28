# 필요한것을 부품처럼 묶는
# ex) 사고가 났는데 사고난 부품만 갈으면 되도록
# 같은파일내에서 실행 가능 / 
#  일반가격
def price(people):
    print("{0}명 가격은 {1} 원 입니다. ".format(people, people * 10000))

# 조조할인가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1} 원 입니다. ".format(people, people * 6000))

# 군인할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1} 원 입니다. ".format(people, people * 4000))


# 이름변경불가
