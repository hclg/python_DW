import numpy as np
arr1 = np.array([1, 2, 3, 4])
print("input", arr1)
arr2 = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,0]])
print(arr2)
print("shape: ", arr2.shape)
print("dtype: ", arr2.dtype)
arr2.shape = 4,3
print("shape: 4, 3", arr2)
arr2 = np.arange(0, 10, 1)
print(arr2);
