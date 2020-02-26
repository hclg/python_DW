# import numpy as np
# arr1 = np.array([1, 2, 3, 4])
# print("input", arr1)
# arr2 = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,0]])
# print(arr2)
# print("shape: ", arr2.shape)
# print("dtype: ", arr2.dtype)
# arr2.shape = 4,3
# print("shape: 4, 3", arr2)
# arr2 = np.arange(0, 10, 1)
# print(arr2);
import numpy as np
data = np.loadtxt('D:\工作缓存区\git\python_DW\Python 数据分析\iris_sepal_length.csv',delimiter=' ');
data.sort();
print('排序: ', data);
print('去重: ', np.unique(data));
print('求和: ', np.sum(data))
print('累加和: ', np.cumsum(data))
print('均值: ', np.mean(data))
print('标准差: ', np.std(data))
print('方差: ', np.var(data))
print('最小值: ', np.min(data))
print('最大值: ', np.max(data))


