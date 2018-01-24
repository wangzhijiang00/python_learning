# 计算圆形的周长和面积
# 输入半径，计算，输出结果
import math
radiusString = raw_input("please input radius:")
radiusInteger = int(radiusString)
circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)
print "周长：",circumference,\
	", 面积：",area
print "输出完成";
