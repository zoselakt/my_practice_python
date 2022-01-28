# 메소드 오버로딩 ( 밑에 설명있음)
class unit :
    def __init__(self, name, hp, speed) : 
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        

class attackunit(unit):
    def __init__(self, name, hp, damage, speed):
        unit.__init__(self, name, hp, speed)
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

class flyable : 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
             .format(name, location, self.flying_speed))

# 메소드 오버로딩 : 동일 클래스 내에서 이미 정의된 함수를 다른 동명의 메소드를 정의하는 것. 즉 같은 이름의 메소드를 여러개 선언하는것.
#                  다양한 매개변수를 받아 처리하기 위함.  
#                 flyableattackunit에 move로 새롭게 재정의하여 함수하나로 처리가능
# ex) 현재 발키리는 fly 함수로 되어 move 함수로 한번에 지정 불가

class flyableattackunit(attackunit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attackunit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
        flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중유닛 이동]")
        self.fly(self.name, location)
        
#발키리
valkyrie = flyableattackunit("발키리", 200, 6 , 5)
valkyrie.fly(valkyrie.name, "3시")
valkyrie.damaged(25)

# 벌쳐
vulture = attackunit("벌쳐", 80, 10, 20)
# 배틀크루저
battlecruiser = flyableattackunit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

# pass : 일단 아무것도안하고 넘어가기
# class buildingunit(unit):
#     def __init__ (self, name, hp, location):
#         pass
# # 서플라이 디팟
# supply_depot = buildingunit("서플라이 디팟", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()


# super : self 는 쓰면 안됨. / 다중상속 시 특정 상속만 상속되게함. / 
# 마지막에 상속되는 것만 __init__ 함수를통해 호출이된다.
# 부모클래스에서 사용된 함수의 코드를 자식 클래스 함수에서 재사용할때 사용
# 상솓을 한 클래스의 함수를 추가적으로 모두 적지 않고도 사용할수 있음.

# 문제점 : 다중상속시 다중 초기화를 할 수 없음.
# class unit :
#     def __init__ (self):
#         print("unit 생성자")

# class flyable:
#     def __init__ (self):
#         print("flyable 생성자")
    
# class flyableunit(flyable, unit):
#     def __init__ (self):
#         super (). __init__ () # 이 부분을 다중상속시 사용 x

# # 드랍쉽
# dropship = flyableunit()
