# -*- coding: utf-8 -*-
"""
2022. 01. 07.

내용 : 실수의 오류

"""
print (0.1 + 0.2 == 0.3) # → false
print("%f" %0.3)

#%% 실수의 오류 해결
import math

print(math.isclose(0.1 + 0.2, 0.3)) # → true

#%% 실수의 오류해결
from decimal import Decimal

print(float(Decimal("0.1") + Decimal("0.2"))) # → 0.3