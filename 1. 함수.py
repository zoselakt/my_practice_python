# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()
 # 입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money
balance = 0
balance = deposit(balance, 1000)
print(balance)
# 출금
def withdraw(percent, cash):
    if percent >= cash :
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(percent - cash))
        return percent - cash
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(percent))
        return percent
percent = 0
percent = deposit(percent, 1000)
percent = withdraw(percent, 2000)
# 수수료
def withdraw_night(percent, cash):
    commission = 100 # 수수료
    return commission, percent - cash - commission
percent = 0 # 잔액
percent = deposit(percent, 1000)
commission, percent = withdraw_night(percent, 500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, percent))

# 기본값(default argument) : 별다른 변수를 넣지 않고 함수내에서 정의된 값을 출력 
#         변수값을 일일이 입력할 필요 없으며 변수의 값을 생략하거나 순서를 변경할 수 있음.
def profile(name, age, main_lang):
    print("이름:{0}\t나이: {1}\t주 사용언어: {2}"\
        .format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

def profile(name, age=17, main_lang= "파이썬"):
    print("이름 : {0}\t 나이 : {1}\t주 사용언어 : {2}" \
        .format(name, age, main_lang))
profile("유재석")
profile("김태호")

# 키워드 (값), (인자) : 함수의 순서와 용도를 미리 예약 / 순서를 맞추지 않아도 된다.
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="파이썬", age=20, name="김태호")

# 함수의 4가지 유형
# 1. input O / output O
# 2. input O / output X
# 3. input X / output O
# 4. input X / output X

# 유형 1 (input, output O)
def calculate_sum(x, y):
    return x + y

result = calculate_sum(1, 2)
print(result)

# 유형 2 (output X)
def save_data_in_database(x):
    print(x, "을 데이터베이스에 저장하겠습니다.")
    print("저장 하였습니다.")
    
save_data_in_database(3)
print(save_data_in_database)

# 유형 3 (input X)
def get_pi():
    return 3.141592

get_pi()

# 유형 4 (input, output X)
def show_current_time():
    import time
    print(time.time(), "입니다.")
    
show_current_time()
print(show_current_time)

# 가변인자 : 전달값이 몇개인지 모르는 상황에서 사용
#            인자 이름앞에 *붙여 사용가능
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end= " ")
    print(lang1, lang2, lang3, lang4, lang5)
profile("유재석", 20, "python", "java","C", "C++", "C#")
profile("김태호", 25, "kotlin", "swift"," ", " ", " ")

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end= " ")
    for lang in language:
        print(lang, end= " ")
        print()
profile("유재석", 20, "python", "java","C", "C++", "C#", "javascript")
profile("김태호", 25, "kotlin", "swift"," ", " ", " ")