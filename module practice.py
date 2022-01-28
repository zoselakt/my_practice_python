import module
module.price(3) # 3명이서 영화보러 갔음
module.price_morning(4)
module.price_soldier(5)

import module as mv
mv.price_soldier(3)
mv.price(4)
mv.price_morning(5)

from module import * # 모듈 내 함수 랜덤
price(3)
price_morning(4)
price_soldier(5)

from module import price, price_morning  # price와 price morning만 출력
price(5)
price_morning(6)

from module import price_soldier as price # 프라이스 솔져를 프라이스라고 칭하고 원래 프라이스대신 변경되어 출력됨
price(5)