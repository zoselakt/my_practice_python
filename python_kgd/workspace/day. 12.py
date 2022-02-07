"""
2022.01.10.

내용 : 예외처리
"""

# try:
#     int(input("정수 입력 : "))

# except Exception as e:
#     print("정수만 입력하세요.")
#%%
try:
    print(10 / 0)

except ZeroDivisionError as e:
    print("0으로 나눌수 없습니다.")
#%%
class NickNameError(Exception):
    pass

def checkNickName(name):
    if name == "바보":
        raise NickNameError
        
nickname = input("닉네임 : ")

try:
    checkNickName(nickname)
    print("닉네임 생성성공!")
except NickNameError:
    print("비속어는 사용할 수 없습니다.")