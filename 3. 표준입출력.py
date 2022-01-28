# 표준 입력 / 출력 / 에러
# 표준에러 sys. stderr: 에러발생시 메세지 띄움 / 어디가 어떻게 틀린지는 안나오며, 지정한 문구가 출력된다.

print("python", "java", sep=", ", end="= ") # end 다음줄도 붙여서 출력 / 출력시 문장끝 변경 
print("무엇이 더 재밌을까요?") # 띄어쓰기 : sep= 
import sys
print("python", "java", file=sys.stdout) # 표준출력 
print("python", "java", file=sys.stderr) # 표준에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8) 왼쪽정렬 8번째까지 rjust(4) 오른쪽 정렬 4번째 까지
#zfill 숫자에 00 ~ 붙힘.
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
# 출력창에 숫자, 문자치면 그대로 출력됨
answer = input("아무값이나 입력하세요 : ")
print ("입력하신 값은" + answer + "입니다.")