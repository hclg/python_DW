# import matplotlib.pyplot as plt
# import numpy as np
# data = np.arange(0, 1.1,0.01)
# print(data)
# plt.title('lines')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xlim((0,1))
# plt.ylim((0,1))
# plt.xticks([0,0.2,0.4,0.6,0.8,1])
# plt.yticks([0,0.2,0.4,0.6,0.8,1])
# plt.plot(data, data**2) #添加y = x^2曲线
# plt.plot(data,data**4) #添加y = x^4曲线
# plt.legend(['y=x^2','y=x^4'])
# plt.savefig('y=x^2.png')
# plt.show()
# 设置 pyplot 的动态 rc参数
def fig_withoutrc():
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(0, 4*np.pi) ## 生成x轴数据
    y = np.sin(x) ## 生成y轴数据
    plt.title('sin')
    plt.rcParams['lines.linestyle']='-'
    plt.plot(x,y,label="sin(x)") ###绘制sin曲线图
    plt.savefig('sin.png')
    plt.show()

# fig_withoutrc()

def fig_without():
    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams['font.family']=['STFangsong']
    plt.rcParams['lines.linestyle']='-'
    plt.rcParams['lines.marker'] = 'p'
    plt.rcParams['lines.linewidth'] = 3

    plt.title('y=sin(x)+1 和 z=cos(2x)+1 的曲线图')
    plt.xlabel('x轴')
    plt.ylabel('y轴')
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)+1
    z = np.cos(2*x)+1
    plt.plot(x, y);
    plt.plot(x, z);
    plt.savefig('y和z的曲线图.png')
    plt.show()

fig_without()