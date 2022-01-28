# 내장함수

# input : 사용자 입력을 받는 함수
# language = input("무슨언어를 좋아하세요?")
# print("{0} 은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지표시
# print(dir())
# import random # 외장함수
# print(dir())
# import pickle
# print(dir)

# print(dir(random))

# 1st = [1, 2, 3]
# print(dir(list))

# name = "jim"
# print(dir(name))

# 외장함수

# glob : 경로 내 폴더 / 파일 목록 조회(윈도우dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리 (경로)
# folder = "sample_dir" # 폴더가있으면 출력 " " 내용 출력
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭제
    # print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더생성
#     print(folder, "폴더를 생성하였습니다.")

#time : 시간관련 함수
#import time
# print(time.localtime())
#print(time.strftime("%Y - %M - %d %H : %M : %S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) # 100 일 후
print("우리가 만난지 100일은", today + td)