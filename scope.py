# x가 없어서 작동안함
def func(a):
    return a + x


def func2(a):
    x = 2
    return a + x


def func3(a):
    global g
    g = 3
    return a + g


# 하지만 글로벌로 설정한 x가 존재하면 그걸 씀
x = 1
print(func(10))
print(func2(20))
print(func3(30))
print(g)