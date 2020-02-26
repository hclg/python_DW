# python 数据分析工具

### 1 Numpy 库

> 为python提供数组功能

#### 1.1 数组创建

> 需要导入包 numpy
* array 一维数组
* darray 多维数组
* arange

| 属性     | 说明                                |
| -------- | ----------------------------------- |
| ndim     | 返回int 表示数组维数                |
| shape    | 返回tuple 数组尺寸，n行m列，为(n,m) |
| size     | 返回int 表示数组元素总数            |
| dtype    | 返回data-type 描述数组元素的类型    |
| itemsize | 返回 int 表示每个元素的大小字节     |
```python
import numpy as np
arr1 = np.array([1, 2, 3, 4])
print("input", arr1)
arr2 = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,0]])
print(arr2)
print("shape: ", arr2.shape)
print("dtype: ", arr2.dtype)
```

#### 1.2 数组属性

* 重设数组属性
    * shape
    ```python
        # 用上面的arr2
        arr2.shape = 4,3
        print("shape: 4, 3", arr2)
        #shape: 4, 3 [[1 2 3]
        # [4 4 5]
        # [6 7 7]
        # [8 9 0]]
    ```
    