"""
2022. 01. 07.

내용: 암호화 / 아스키코드 쓰임
    chr : 정수를 문자로
    ord : 문자를 정수로
"""

# print(chr(ord('A') * 3))


# 암호화
pw = "a1b2c3"
en_pw = ""
de_pw = ""

for i in pw:
    en_pw += chr(ord(i) * 9)
    
print("기존 비밀번호 : %s" %pw)
print("암호화된 비밀번호: {pw}".format(pw = en_pw))

# 복호화
for i in en_pw:
    de_pw += chr(ord(i) // 9)
    
print("암호화된 비밀번호 : {en_pw}\n복호화된 비밀번호 : {de_pw}".format(en_pw=en_pw, de_pw=de_pw))