# 파이썬 데이터를 파일형태(객체)로 저장 (다른사람에게 보낼때 사용)
# 다음 데이터유형으로 pickle 할 수 있다
#- Boolean / integer / float / string / tuple / list / set / dictionary
# r :읽기 / w: 쓰기 / x: 쓰기(파일이 있으면 오류) / a: 쓰기(파일이 있으면 뒤에 내용추가)
# + : 읽기쓰기 / t : 텍스트모드 / b: 바이너리 모드 : 바이트단위 데이터 기록에 사용 / 컴퓨터가 처리하는 파일형식
import pickle
profile_file = open("profile.pickle", "wb") # wb : (write) binary 
profile = {"이름" : "박명수", "나이": 30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
profile_file.close()

# pickle 화 된 파일을 읽기 (불러오기)
profile_file = open("profile.pickle", "rb") # rb : (read) binary
profile = pickle.load(profile_file )
print(profile)
profile_file.close()

# with : pickle과 유사하나 close로 끝맺음 안해도됨
import pickle

with open("profile.pickle", "rb") as profile_file : #rb (리드 바이너리)
    print(pickle.load(profile_file)) # close 없어도 출력됨

with open("study.txt", "w", encoding="utf8") as study_file :
    study_file.write("파이썬을 열심히 공부하고있습니다.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())