# python 绘图库
---
> `Matplotlib` 是最著名的绘图库
### 1. 创建画布与创建子图

|函数名     |函数作用                   |
| -------- | ----------------------------------- |
|plt.figure|创建一个空白画布，可指定大小|
|figure.add_subplot| 创建并选中子图|
|plt.title|标题|
|plt.xlabel|x轴名称|
|plt.ylabel|y轴名称|
|plt.xlim|x轴的范围|
|plt.ylim|y轴的范围|
|plt.xticks|x轴刻度的数目与取值|
|plt.yticks|y轴刻度的数目与取值|
|plt.savafig|保存绘制图片|
|plt.show|本机显示图形|

* 绘制y = x^2^ 和y=x^4^图
```python
import matplotlib.pyplot as plt
import numpy as np
data = np.arange(0, 1.1,0.01)
print(data)
plt.title('lines')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((0,1))
plt.ylim((0,1))
plt.xticks([0,0.2,0.4,0.6,0.8,1])
plt.yticks([0,0.2,0.4,0.6,0.8,1])
plt.plot(data, data**2) #添加y = x^2曲线
plt.plot(data,data**4) #添加y = x^4曲线
plt.legend(['y=x^2','y=x^4'])
plt.savefig('y=x^2.png')
plt.show()
```
* 绘制 y = sin(x)图
```python
def fig_withoutrc():
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(0, 4*np.pi) ## 生成x轴数据
    y = np.sin(x) ## 生成y轴数据
    plt.title('sin')
    plt.plot(x,y,label="sin(x)") ###绘制sin曲线图
    plt.savefig('sin.png')
    plt.show()

fig_withoutrc()
```
