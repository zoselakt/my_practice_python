# for : 종료조건은 모르지만 반복해야하는 횟수를 알때 사용
#       반복되는 일을 줄이기 위하여 / 반드시 콜론(:)을 마지막에 써야함.
for waiting_no in range(5):
    print("대기번호 : {0}". format(waiting_no))
starbucks = ["아이언맨", "토르", " 아이엠그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    
# 한줄 for (출석번호 1,2,3,4 앞에 100을 붙이기)
students = [1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)

# while : 반복횟수는 모르지만 종료조건을 알때 사용
#         반복문 / 특정 단어, 조건이 만족하는 경우 종료
guest= "토르"
index = 5
while index>=1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았습니다.".format(guest, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")
        
# while 무한루프 종료방법 ctrl + C / 무제한출력이므로 아래까지 영향 o
#buier = "아이언맨"
#index = 1
#while True :
#    print("{0}, 커피가 준비되었습니다. 호출{1} 회".format(buier, index))
#    index += 1
passenger = "토르"
person = "unknown"
while person != passenger :
     print("{0}, 커피가 준비 되었습니다.".format(passenger))
     person = input("이름이 어떻게 되세요?")
