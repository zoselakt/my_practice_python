# 예외처리 : 오류가생겼을때(잘못된 값을 입력했을때) 출력됨
# try : 수행되어질 코드(정상수행시 이부분만 수행)
# except : 수행되다가 오류가 발생할때 실행시킬 코드 (정의된 예외상황일때만 실행)
try:
    print("나누기전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    print ("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError :
    print("에러! 잘못된값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err :
    print("알수없는 에러가 발생하였씁니다.")
    print(err)
    
# 에러발생시키기
try:
    print("한자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를입력하세요 : "))
    num2 = int(input("두 번째 숫자를입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2} ".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")

# 사용자 정의 예외처리 : 어떤 에러 데이터를 입력했는지 출력
class bignumbererror(Exception):
    pass
try:
    print("예외 처리 한자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를입력하세요 : "))
    num2 = int(input("두 번째 숫자를입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise bignumbererror ("입력값 : {0}, {1}" .format(num1, num2))
    print("{0} / {1} = {2} ".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
except bignumbererror as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
    print(err)
    
# finally : 계산 마지막 무조건 finally 구문이 출력됨
# try문 내에있는 명령이 잘실행되는지 에러가 발생하는지 상관없이 출력
# 없는 파일을 열려고 한다던지 리스트에 없는 값을 잘못출력시키려고 하는지
# 완성도를 높이는데 사용
finally:
     print("계산기를 이용해 주셔서 감사합니다.")

# 오류메세지
# syntaxError : 잘못된 문법
# NameError : 참조변수 없음
# ZeroDivisionError : 0으로 나눌 수 없음
# indexError : 인덱스 범위 벗어남
# ValueError : 참조 값이 없음
# KeyError : 키 없음 에러(주로 딕셔널리 사용시)
# AttributeError : 모듈, 클래스의 잘못된 속성 사용함
# FileNotFoundError : 파일못찾음
# TypeError : 타입 안 맞음