# abs() : 숫자의 절대값을 돌려줌 / ex) abs(-99) = 99
# all(iterable) : 반복 가능한 자료형의 모든 요소가 참(true)면 참을 반환하는 함수 / 거짓이면 거짓을 반환 
#                 비어있으면 true / ex) all(1,2,3,4,5) : true, all(1,2,0,4,5) : false
# any : 반복 가능한 자료형의 단 하나라도 참(true)면 참을 반환하는 함수 / 모든 거짓인 경우에만 거짓을 반환 
#                 비어있으면 false / ex) any(1,2,3,4,5) : true, any(1,2,0,4,5) : true, any(""): false
# bin : 전달받은 자료형의 값을 이진수 문자열로 돌려준다. / ex ) bin(3) = 0b11
# bool(boolean) : 참과 거짓을 나타 내는데 쓰임 / 비어있으면 false, 숫자 0 false, 나머지 모두 :true / ex) bool(false)
# breakpoint : 디버깅을 목적으로 중단점을 설정하여 코드 에러를 수정할 때 사용 / ex) breakpoint()
# chr() : 유니코드값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수 / ex: chr(97) = a
# dir (): 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다. / ex) dir([1,2,3]) = (list내 함수) append, count ...
# divmod () : 2개의 숫자를 입력받아 나눈 몫과 나머지를 튜플형태로 돌려주는 함수 / divmod(7, 3) = 2, 1 / 7을 3으로
# enumerate () : 자료형을 입력받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다. / for i, name in enurmerate(['body', 'foo', 'bar']): - print(i. name) = 0 body, 1 foo, 2bar
# eval(): 문자열을 입력한대로 결과값을 돌려주는 함수이다. / eval('1+2') = 3 / eval(" 'hi' + 'a' ") = hia
# filter(): 첫번째 인수로함수이름을 두번째 인수로 그 함수에 차례로 들어갈 반복가능한 자료형을 받는다.
#           그리고 두번째 인수인 반복가능한 자료형 요소가 첫번째 인수인 함수에 입력되었을 때 반환값이 참인 것만 묶어서 돌려준다.
# hex() : 정수 값을 입력받아 16진수로 변환하여 돌려주는 함수이다. / hex(234) = 0xea
# id() : 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다. / a = 3, id(3) = 135072304
# int() : 정수를 입력받으면 그대로 돌려준다. / int(3.4) = 3 / int("11", 2) = 3
# isinstance() : 첫번째로 인스턴스, 두번째로 클래스 이름을 받는다. 입력받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 True, false로 돌려준다.
# len(): 입력값의 길이를 돌려주는 함수이다.
# list(): 반복가능한 자료형을 입력받아 리스트로 만들어주는 함수이다.
# map(): 함수와 반복가능한 자료형을 입력받는다. 입력받은 자료형의 각 요소를 함수f가 수행한 결과를 묶어서 돌려주는 함수이다.
# max(), min() : 최대값 또는 최소값을 돌려주는 함수
# oct(): 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
# open(): 파일 이름과 읽기 방법을 입력받아 파일 객체를 돌려주는 함수이다. 읽기 방법을 생략하면 읽기 전용모드로 파일 객체를 만들어 돌려준다 (w: 쓰기, r:읽기, a:추가모드로 열기, b:바이너리모드로 열기)
# ord(): 문자의 유니코드 값을 돌려주는 함수이다. ( ord ↔ chr ) / orc("a") = 97 
# pow(): x의 y 제곱한 결과값을 돌려주는 함수이다. / pow(2, 4) = 16
# range(): 함수는 입력받은 숫자에 해당하는 범위값을 반복 가능한 객체로 만들어 돌려준다.
# round(): 숫자를 입력받아 반올림해 주는 함수이다.
# sorted(): 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다. /sorted([3, 1, 2]) = [1, 2, 3]
# str(): 문자열 형태로 객체를 변환하여 돌려주는 함수이다.
# sum(): 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
# tuple(): 반복가능한 자료형을 입력받아 튜플형태로 바꾸어 돌려주는 함수이다.
# type(): 입력값의 자료형이 무엇인지 알려주는 함수이다.
# zip(): 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다. / list(zip([1, 2, 3], [4, 5, 6])) = [(1,4), (2, 5), (3, 6)]
