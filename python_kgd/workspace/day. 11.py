"""
2022.01.10.

내용: 클래스
"""
class car:
# =============================================================================
#     brand = ""
#     color = ""
#     price = 0
# =============================================================================
    
    def __init__(self, brand="", color="", price=0):
        self.brand = brand
        self.color = color
        self.price = price
        
    def engineStart(self):
        print(self.brand + "시동 on")
        
    def enginestop(self):
        print(self.brand + "시동 off")
        
momCar = car("benz", "yellow", 35000)
dadyCar = car("bmw", "black", 600000)
myCar = car()

momCar.engineStart()
dadyCar.enginestop()
#%% 
# 상속
class A:
    def __init__(self, data =10):
        self.data = data
        
    def printData(self):
        print(self.data)
        
    def show(self):
        print("부모 메소드")
        
class B(A):
    # pass

# b = B()
# b.printData()
# b.show()

    def __init__(self, data, data2):
        # A. __init__(self, data)
        super().__init__(data)
        self.data2 = data2
        
# =============================================================================
#     def printData2(self):
#         print(self.data, self.data2)
# =============================================================================
        
b = B(30, 20)
b.printData2()
#%%
# 상속예제
class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
        
    def engineStart(self):
        print(self.brand + "시동 on")
        
    def engineStop(self):
        print(self.brand + "시동 off")
        
class SuperCar(Car):
    def __init__(self, brand, color, price, mode):
        super().__init__(brand, color, price)
        self.brand = brand
        self.color = color
        self.price = price
        self.mode = mode
    
    def engineStart(self):
        print(self.brand + "음성시동 on")
        
    def openRoof(self):
        print("opne top")
        
    def closeRoof(self):
        print("close top")
        
ferrari = SuperCar("ferrari", "red", 35000, "daily")

ferrari.engineStart()
ferrari.engineStop()
ferrari.openRoof()
ferrari.closeRoof()