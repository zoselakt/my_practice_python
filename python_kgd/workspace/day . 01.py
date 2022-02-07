"""
2022.01.07.

내용 : 서식문자 (format)
    반드시 따옴표 안에서 작성한다.
"""

# %d : decimal : 정수 (10진수)
# %o : octal : 정수 (8진수)
# %x: hexadecimal : 정수(16진수)
# %f : float : 실수
# %c : character : 문자
# %s : string : 문자

name = "한동석"
age = 30
height = 190.1
hobby = "피아노"
data = 10

print("이름 : %s" %name)
print("나이 : %d살" %age)
print("키 : %.2fcm" %height)
print("취미 : %s" % hobby)
print("data : %o")

#%%
num1 = int(input("정수 1 : "))
num2 = int(input("정수 2 : "))

addResult = num1 + num2
subResult = num1 - num2
mulResult = num1 * num2
divResult = num1 // num2
modResult = num1 % num2

print("%d + %d = %d" %(num1, num2, addResult))
print("%d - %d = %d" %(num1, num2, subResult))
print("%d * %d = %d" %(num1, num2, mulResult))
print("%d // %d = %d" %(num1, num2, divResult))
print("%d %% %d = %d" %(num1, num2, modResult))
