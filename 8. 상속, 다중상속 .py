# 상속 : 다음 차례에 이어 주거나 이어 받음
class unit : # 부모 클래스
    def __init__(self, name, hp) : 
        self.name = name
        self.hp = hp

class attackunit(unit): # 자식 클래스 / unit 클래스를 이어받음
    def __init__(self, name, hp, damage):
        unit.__init__(self, name, hp)
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
            
# 다중상속
class flyable : 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
             .format(name, location, self.flying_speed))
        
# 공중공격유닛 (attackunit 과 flyable 상속받음) ← 다중상속
class flyableattackunit(attackunit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attackunit.__init__(self, name, hp, damage)
        flyable.__init__(self, flying_speed)
        
# 공중유닛 생성
valkyrie = flyableattackunit("발키리", 200, 6 , 5)
valkyrie.fly(valkyrie.name, "3시")

valkyrie.damaged(25)