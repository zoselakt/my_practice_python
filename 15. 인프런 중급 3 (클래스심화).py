class car():
    """
    car class
    author : kim
    date : 2022. 01. 05.
    클래스, 스테틱, 인스턴스 메소드
    """

    price_per_raise = 1.0
    
    def __init__(self, company, details): 
        self._company = company
        self._details = details
                
    def __str__ (self):  # 객체를 문자열로 표기 / 다른 자료형간 인터페이스 제공목적
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self): # 객체를 문자열로 표기하나 객체를 이해할수 있는 평문으로 표현 / 해당객체를 인간이 이해할수 있는 표현으로 나타내기 위한 용도
        return "repr : {} - {}".format(self._company, self._details)
    
    # 인스턴스메소드 / self는 객체의 고유한 속성 값을 사용 /self를 받음
    def detail_info(self):  
        print("current id : {} ".format(id(self)))
        print("car detail info : {} {}" . format(self._company, self._details.get("price")))
        
    def get_price(self):
        return "before car price → company : {}, price{}".format(self._company, self._details.get("price"))
    def get_price_culc(self):
        return "after car price → company : {}, price{}".format(self._company, self._details.get("price") * car.price_per_raise)
    
    # 클래스 메소드 / cls: 부모클래스(car) / 직접 정보대신 사용에 좋음. / cls 를 받음
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("please enter 1 or more")
            return
        cls.price_per_raise = per
        print("succeed!")
    
    # 스테틱 메소드 / 아무것도 받지 않음
    @staticmethod 
    def is_bmw(inst): # inst 안써도 됨
        if inst._company == "bmw":
            return "this car is {}".format(inst._company)
        return "not bmw"
    
car1 = car("Ferrari", {"color": "white", "horsepower" : 400, "price" : 8000})
car2 = car("bmw", {"color": "black", "horsepower" : 270, "price" : 5000})

# 전체정보
car1.detail_info()
car.detail_info(car1)
car2.detail_info()
car.detail_info(car2)

# 가격정보 (직접정보 / 별로 좋지 않은 접근 방식)
print(car1._details.get("price"))
print(car2._details["price"])

# 가격 정보(인상전 메소드)
print(car1.get_price())
print(car2.get_price())

car.price_per_raise = 1.4 # 클래스 메소드 안 받음

# 가격정보 (인상후 - 클래스 메소드 미사용)
print(car1.get_price_culc())
print(car2.get_price_culc())

car.raise_price(1.6) # 클래스 메소드 받음

# 가격정보 (인상후 - 클래스 메소드 사용)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 스테틱 메소드 호출
# 방법 1 / 인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 방법 2 / 클래스로 호출
print(car.is_bmw(car1))
print(car.is_bmw(car2))
