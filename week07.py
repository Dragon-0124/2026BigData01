import numpy as np
import random

# l1 = [1, 2, 3.1, "list", [4, 5, 6]] # 정수, 실수, 문자열, 리스트
# NumPy 배열은 모든 요소의 크기가 같아야 하는데, 리스트[4, 5, 6]는 크기가 달라 오류 발생
# ㄴ arr = np.array(l1, dtype=object)로 dtype를 맞춰주거나 크기가 다른 요소를 제거해야 함
l1 = [1, 2, 3.1, "list"]
array01 = np.array(l1)
print(l1)
print(array01)

array02 = np.arange(1, 10)
print(array02)


array03 = np.ones((2, 4), dtype=int)
print(array03)
print(array03.T)


l2 = list()
l3 = list()

for i in range(3):
   l2.append(random.random())
print(l2)

for item in l2:
   l3.append(item*10)
print(l3)

array04 = np.array(l2)
print(array04 * 10)
print(array04 > .5)



# numpy 배열 주요 통계 함수
print(np.mean(array02))
print(np.median(array02))
print(np.max(array02))
print(np.min(array02))
print(np.var(array02)) # variance
print(np.std(array02)) # standard deviation