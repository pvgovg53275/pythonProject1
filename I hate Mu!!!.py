# 导入绘图库
import matplotlib.pyplot as plt
import numpy as np 

'''
颜色参数
c:"r",'g',"b","k","c"
十六进制   #00FF00

线条类型:
实线: solid  '-'
虚线: dotted ':'
破折线: dashed  '--'
点划线:dashdot "-."


描点类型
'o': 实心圆
'v': 倒三角
'^':  正三角
'1'-'4'
maker
'''



# 创建绘图点
x=np.arange(1,5,0.1) 
y=np.sin(x)
# 开始绘图
plt.plot(x,y,color="#FF0000",linestyle='-')

# x标签
plt.xlabel("x")
# y标签
plt.ylabel("y")

# 显示图
plt.show()
