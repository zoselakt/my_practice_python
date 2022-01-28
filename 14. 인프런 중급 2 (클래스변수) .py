class car():
    """
    car class
    author : kim
    date : 2022. 01. 04.
    """
    # 클래스 변수(모든 인스턴스가 공유) / 부모 클래스와 함수 사이 설정
    car_count = 0  
    
    def __init__(self, company, details): 
        self._company = company
        self._details = details
        car.car_count += 1 # 클래스변수 : 총 인스턴스가 3까지 있어 출력값 3
        
    def __str__ (self):  # 객체를 문자열로 표기 / 다른 자료형간 인터페이스 제공목적
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self): # 객체를 문자열로 표기하나 객체를 이해할수 있는 평문으로 표현 / 해당객체를 인간이 이해할수 있는 표현으로 나타내기 위한 용도
        return "repr : {} - {}".format(self._company, self._details)
    
    def detail_info(self):
        print("current id : {} ".format(id(self)))
        print("car detail info : {} {}" . format(self._company, self._details.get("price")))
    
car1 = car("Ferrari", {"color": "white", "horsepower" : 400, "price" : 8000})
car2 = car("bmw", {"color": "black", "horsepower" : 270, "price" : 5000})
car3 = car("audi", {"color": "silver", "horsepower" : 300, "price" : 6000})


# 실행
car1.detail_info()
car.detail_info(car1)
car2.detail_info()
car.detail_info(car2)

# 클래스변수 공유확인 : 인스턴스 네임스페이스에 없으면 상위클래스에서 찾는다. ▶ 동일한 이름으로 변수 생성가능 (인스턴스 검색 후 네임스페이스에 있으면 변수생성 가능)
print(car.car_count)
print(car1.car_count)
print(car2.car_count) 
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))
print(dir(car2))