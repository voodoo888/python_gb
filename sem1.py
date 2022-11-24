def func1(a, b):
    if (a == b ** 2) or (b == a ** 2):
        print("YES")
    else:
        print("NO")


func1(5, 25)
func1(4, 16)
func1(25, 5)
func1(8, 9)


def func2(a, b, c, d, e):
    list1 = [a, b, c, d, e]
    return max(list1)


print(func2(1, -2, -8, 4, -5))

def func3(a):
    for i in range(-a, a + 1):
        print(i, end=" ")

func3(5)


def func4(a):
    b = round(a)
    if b == a:
        print("NO")
    else:
        a = round(a * 10) % 10
        print(a)


func4(5)


def func5(a):
    if (a % 5 == 0 or a % 10 == 0 or a % 15 == 0) and (a % 30 != 0):
        print("YES")
    else:
        print("NO")

func5(75)