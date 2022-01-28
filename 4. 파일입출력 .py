# 파일입출력 (왼쪽 항목에 txt 추가)  
# 항상 open 했으면 close로 끝맺음 해야함.

# " w " : write
score_file = open(" score.txt ", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# "a" : 이미있는 내용에 덮어쓰기 / 줄바꿈이 따로 없으니 추가 할때는 \n 추가
score_file = open(" score.txt ", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# "r"(read) : score.txt 화면에 있는 모든 내용을 아래 터미널에 출력
score_file = open(" score.txt ", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 한줄 만 출력
score_file = open(" score.txt ", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
print(score_file.readline()) # 4줄이라 4번사용
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 몇줄인지 모를때
score_file = open(" score.txt ", "r", encoding="utf8")
while True : 
    line = score_file.readline()
    if not line : 
        break
    print(line)
score_file.close()

# list 형태로 저장
score_file = open(" score.txt ", "r", encoding="utf8")
lines = score_file.readline()
for line in lines : 
    print(line, end="")
score_file.close()