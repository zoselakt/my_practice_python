# 다른 파일 생성후 진행
# 패키지 : 모듈을 모아 놓은 단위 / 미리 파일을 만든후 그 파일의 수식을 간단하게 불러오기하여 출력가능 
#     관련된 여러 개의 모듈을 계층적인 몇개의 디렉토리로 분류해서 저장하고 계층화한다.

import travel.thailand  # thiland 부분은 항상 모듈이나 패키지만 가능 클래스나 함수는 불가능
trip_to = travel.thailand.thailandpackage()
trip_to.detail()

from travel.thailand import thailandpackage
trip_to = thailandpackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.vietnampackage()
trip_to.detail()

# all :  공개범위설정 / __init__ 파일에 설정해야함 , 설정안할시 오류출력
from travel import *
trip_to = vietnam.vietnampackage()
trip_to = thailand.thailandpackage() # 정상작동 되는 구문임.
trip_to.detail()

#모듈을 직접실행 / 호출할 파일 (vietnam) 에서 작성
# if __name__ == "__main__":
#     print("thailand 모듈을 직접 실행")
#     trip_to = thailandpackage()
#     trip_to.detail()
# else:
#     print("thailand 외부에서 모듈호출")

# 컴퓨터 내 패키지, 모듈 파일 위치 검색 / 이파일이 내컴퓨터에서 어디에 있는지 출력
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand)) # 정상작동되는 구문