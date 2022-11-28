# while True:
#     pass
# else:
#     pass

def numbers (num):
    for i in range(num):
        print((-3) ** i, end=" ")
        
numbers(5)

def dict_nums(num):
    result = dict()
    for i in range(1, num + 1):
        result[i] = (3 * i) + 1
    return result

print(dict_nums(6))

string1 = "i love Pythlon"
string2 = "lo"
print(string1.count(string2))

kq = string1.split("lo")
print(kq)