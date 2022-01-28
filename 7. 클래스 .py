# 클래스 
# - 데이터를 묶어 하나의 클래스를 만들어서 여러 변수를 기입하여 코드하나로 여러개체 작성할수 있다.
# self / 속성 / 메소드 / 인스턴스

# class 기본구조
# class + 클래스 이름 : 
#    def __init__(메소드) (self, 매개변수1, 매개변수2 ) :
#       self.속성 = 매개변수 1 (인스턴스 주소)
#       self.속성 = 매개변수 2 (인스턴스 주소)
# 변수1 = 클래스이름 (인스턴스)
# 변수2 = 클래스이름 (인스턴스)

# __init__ : 생성자 / 클래스 작성시 필수적인 요소 / initialize로 인스턴스(객체)를 초기화함.
# self (self + 매개변수 / parameter) : 인스턴스화된 객체의 주소
# 인스턴스 : 클래스를 기반으로 만들어진 객체

# 멤버변수 / 클래스 내 변수
class unit :
    def __init__(self, name, hp, damage) : 
        #여기서부터
        self.name = name
        self.hp = hp
        self.damage = damage
        #여기까지의 내용
        print("{0} 유닛이 생성되었습니다. ".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
marine1= unit("마린", 40, 5)
marine2= unit("마린", 40, 5)
tank = unit("탱크", 150, 35)

# 클로킹이라는 변수는 class 에 없으니 외부에서 할당할수 있다.
wraith1 = unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
wraith1.clocking = True
if wraith1.clocking == True :
    print("{0}는 현재클로킹 상태입니다.".format(wraith1.name))

# 메소드
class attackunit:
    def __init__(self, name, hp, damage):
         self.name = name
         self.hp = hp
         self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
            
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 유닛생성
firebat1 = attackunit("파이어뱃", 50, 16)
firebat1.attack("5시")
# 유닛 공격
firebat1.damaged(25)
firebat1.damaged(25)