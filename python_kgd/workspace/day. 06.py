"""
2022. 01. 08

내용 : break / continue
"""
# 1~ 10까지 중 4까지만 출력 
#%% 
# 3까지 출력하고 스탑
for i in range(10):
    if i == 3:
        break
    print(i + 1)
    
# 4까지 출력하고 스탑
for i in range(10):
    print(i + 1)
    if i == 3:
        break
#%% 4 제외하고 출력
for i in range(10):
    if i == 3:
        continue
    print(i + 1)
    
#%%
# 3과 5의 배수

for i in range(1, 100):
    if i % 3 and i % 5:
        continue
    print(i)
#%%
# 100부터 1까지 중 70까지만 출력
for j in range(100, 1, -1):
    print(j)
    if j == 70:
        break    
    
