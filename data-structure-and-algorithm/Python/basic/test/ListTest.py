"""
Operation           Big-O Efficiency
indexx[]            O(1)
index assignment    O(1)
append              O(1)
pop()               O(1)
pop(i)              O(n)
insert(i,item)      O(n)
del operator        O(n)
iteration           O(n)
contains (in)       O(n)
get slice [x:y]     O(k)
del slice           O(n)
set slice           O(n+k)
reverse             O(n)
concatenate         O(k)
sort                O(nlogn)
multiply            O(nk)
"""

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

# import the timeit module
# import the Timer class defined in the module
from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension",t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range", t4.timeit(number=1000), "milliseconds")

# 同样是执行1000次创建一个包含1-1000的列表，四种方式使用的时间差距很大！
# 使用append比逐次增加要快很多，另外，使用python的列表产生式比append要快，
# 而第四种方式更加快！