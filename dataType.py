# !/user/bin/python
# -*- coding: utf-8 -*-
#  model： dataType
#  addr:    http://www.runoob.com/python/python-strings.html

############################################################
#                   数据类型
# key: int long list tuple dictionary complex
#############################################################

########## number #############
# int
# long
# float
# complex
###    number l类型转换
'''
int()
long()
float()
str()
tuple()
list()
char()
hex()
'''
###    number 数学函数
'''
abs()
cmp()
log()
max()
min()
'''

###   随机数函数
#random() #随机生成下一个实数。它在[0,1)

#  三角函数
#cos()
#sin()
#tan()

### 数学常量
# pi
# e

############# str ############################3
###  python访问字符串
#[]截取字符串

###  字符串更新
#字符串修改
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
var1 = 'Hello World!'
print "更新字符串 :- ", var1[:6] + 'Runoob!'
'''

###   转义字符
print 'hello world!'
print 'xl.he'

###   python字符串运算符
'''
+:字符串连接
*：重复输出
[]:索引获取
[:]:截取字符串
in:成员运算符，->True or False
not in:
r/R: pirnt r'\n' >> \n
'''

###   字符串格式化
#
'''
python字符串格式化符号:
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
格式化操作符辅助指令:
符号	功能
*	定义宽度或者小数点精度
-	用做左对齐
+	在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	显示的数字前面填充'0'而不是默认的空格
%	'%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''
name='xl.he'
weight=21
print 'my name is %s and weight %d kg!'%(name,weight)

###   python的字符串内建函数 ###############################
###
###   http://www.runoob.com/python/python-strings.html
#############################################################
#string.join(seq)
#以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
#string.maketrans(intab, outtab])
#maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
#string.split(str="", num=string.count(str))
#以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串




raw_input('please input enter to exit!')







