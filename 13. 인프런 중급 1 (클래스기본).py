car_company_1 = "Ferrari"
car_detail_1 = [
    {"color" : "white"},
    {"horsepower" : 400},
    {"price" : 8000}    
]

car_company_2 = "bmw"
car_detail_2 = [
    {"color" : "black"},
    {"horsepower" : 270},
    {"price" : 5000}    
]

car_company_3 = "audi"
car_detail_3 = [
    {"color" : "silver"},
    {"horsepower" : 300},
    {"price" : 6000}    
]

# 리스트 구조
car_company_list = ['ferrari', "bmw", "audi"]
car_detail_list = [
    {"color": "white", "horsepower" : 400, "price" : 8000},
    {"color": "black", "horsepower" : 270, "price" : 5000},
    {"color": "silver", "horsepower" : 300, "price" : 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

# 딕셔너리 구조
car_dicts = [
    {"car_company" : "Ferrari" , "car_detail" : {"color": "white", "horsepower" : 400, "price" : 8000}},
    {"car_company" : "bmw" , "car_detail" : {"color": "black", "horsepower" : 270, "price" : 5000}},
    {"car_company" : "audi" , "car_detail" : {"color": "silver", "horsepower" : 300, "price" : 6000}}   
]

del car_dicts[1]

print(car_dicts)

class car():
    def __init__(self, company, details): # 초기화
        self._company = company
        self._details = details
        
    def __str__ (self):  # 객체를 문자열로 표기 / 다른 자료형간 인터페이스 제공목적
        return "str : {} - {}".format(self._company, self._details)

    def __repr__(self): # 객체를 문자열로 표기하나 객체를 이해할수 있는 평문으로 표현 / 해당객체를 인간이 이해할수 있는 표현으로 나타내기 위한 용도
        return "repr : {} - {}".format(self._company, self._details)
    
    def __Reduce__(self):
        pass
    
    def detail_info(self):
        print("current id : {} ".format(id(self)))
        print("car detail info : {} {}" . format(self._company, self._details.get("price")))
    
car1 = car("Ferrari", {"color": "white", "horsepower" : 400, "price" : 8000})
car2 = car("bmw", {"color": "black", "horsepower" : 270, "price" : 5000})
car3 = car("audi", {"color": "silver", "horsepower" : 300, "price" : 6000})


print(car1)
print(car2)
print(car3)

print(car1.__dict__) # 클래스 내부 속성정보확인용
print(car2.__dict__)
print(car3.__dict__)

# print(dir(car1)) # 사용가능한 명령어

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

for x in car_list:
    # print(repr)
    print(x)
    
# id 확인

print(id(car1))
print(id(car2))
print(id(car3))

# doctring
print(car.__doc__)

# 실행
car1.detail_info()
car.detail_info(car1)
car2.detail_info()
car.detail_info(car2)