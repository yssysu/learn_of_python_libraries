import random as rd

# 生成随机小数
''' 1
    random():
        返回一个随机的浮点数，在[0,1)之间
'''
print(rd.random())

''' 2
    uniform(a,b):
        生成在a，b之间的随机小数
'''
print(rd.uniform(1,50))


# 生成随机整数
''' 1
    randrange(start,stop,step)
        生成一个从start开始到stop为止，以step为步长生成的序列中的一个整数
        只填写一个数值的时候，默认为stop
'''
print(rd.randrange(1,100,5))

''' 2
    randint(a,b):
    随机生成一个在a，b之间的整数，包含上下限，即可能生成b
'''
num1 = rd.randint(1,6)
print(num1)

# example:生成一段序列号
strings = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*('
numbers = [1,2,3,4,5,6,7,8,9]
def proNum():
    s1 = 0
    s1_sum = rd.choice(strings)
    for i in range(10):
        s1 = rd.choice(strings)+f"{rd.randint(0, 9)}"
        s1_sum += s1
    print(s1_sum)
proNum()

# 与序列有关
''' 1
    choice():
        从列表/其他序列中随机选择一个元素
'''
names = ['ys','yd','yf']
name_random = rd.choice(names)
print(f'{name_random}')

''' 2
    shuffle():
        将原序列打断并返回一个新的序列，
        注意，这里返回的新序列是直接作用在原序列上，即原序列被改变了
        所以返回值为None
'''
days = [1,2,3,4,5,6,7,8]
print(days) # 随机变换
print(rd.shuffle(days)) # <None>

''' 3
    sample(序列，k=n):
        返回从总体序列中选取的唯一元素的长度为k的列表 
        // 理想情况下的序列指代的是列表或元组
        序列指要进行排序的一串，k代表要返回列表的长度
        序列既可以是数值，也可以是字符串
'''
months = [1,2,3,4,5,6,7,8]
print(rd.sample(months,k=6))
names = ['wy','tx','al']
print(rd.sample(names,k=2))



