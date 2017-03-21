# !/user/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xl.he'


###################################################
# python 循环语句
####################################################
# while
# for
# 嵌套（while & for)

####################   while   ###################3
# while 语句时还有另外两个重要的命令 continue，break 来跳过循环，
# continue 用于跳过该次循环，break 则是用于退出循环
def whileShow() :
    numbers = [1,2,4,5,6,7,8,9,10]
    even = []
    odd = []
    while len(numbers) > 0 :
        number = numbers.pop()
        print  'numbers=',numbers
        print 'nember',number
        if (number % 2 == 0):
            even.append(number)
        else :
            odd.append(number)
        print 'even = ',even
        print 'odd = ',odd
        raw_input('please input the enter to continue ...')

######################### if #################################
# for循环可以遍历任何序列的元素，例如列表，字符串
def forShow():
    s='hello xuliang!'
    for i in s:
        print i
    l=['head','hand','foot']
    for n in l:
        print n


# 循环控制语句
'''
break	    在语句块执行过程中终止循环，并且跳出整个循环
continue  	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
pass  	    pass是空语句，是为了保持程序结构的完整性。
'''
#########################   break   #######################
'''
break语句用来终止循环语句
break语句用在while和for循环中。
break语句将终止所在循环，跳出执行循环外的下一语句'''

def breakShow():
    for letter in 'Python':  # First Example
        if letter == 'h':
            break
        print 'Current Letter :', letter


    var = 10  # Second Example
    while var > 0:
        print 'Current variable value :', var
        var = var - 1
        if var == 5:
            break

    print "Good bye!"

##########################  Continue    #################################
'''
Python continue 语句跳出本次循环，而break跳出整个循环'''
def continueShow():
    for letter in 'Python':     # 第一个实例
       if letter == 'h':
          continue
       print '当前字母 :', letter

    var = 10                    # 第二个实例
    while var > 0:
       var = var -1
       if var == 5:
          continue
       print '当前变量值 :', var
    print "Good bye!"

##############  pass ##########################
'''
pass 是空语句，不做任何事情，一般用做占位语句，保持
程序结构的完整性。
'''
def passShow():
    for letter in 'Python':
       if letter == 'h':
          pass
          print '这是 pass 块'
       print '当前字母 :', letter

    print "Good bye!"