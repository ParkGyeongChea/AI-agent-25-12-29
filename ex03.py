import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# print("np.__version__", np.__version__)
# print("pd.__version__", pd.__version__)
# print("OK")


num_list = [1, 2, 3, 4, 5]
print(num_list) #파이썬 기본  list
data = np.array(num_list)
print(data) #numpy array
#넘파이 어레이에는 여러가지 집계함수가 포함되어 있다.

print(data.mean())
print(data.max())