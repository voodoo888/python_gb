# type hinting <-- строгая типизация в python
import time
T = time.time()
number = round(T * 1000 % 100)
print(number)

flag = False
A = ['sdsds', 'rerer', '34']
B = ["34", '232', '4t']

for i in A:
    if i.find("3") > (-1):
        print(i)
        flag = True

print(flag)

count = 0

control_list = ['qwe', 'asd', 'qwwe', 'zxc', 'qwwe', 'ertqwe']
control_literal = 'qwe'

for i in range(len(control_list)):
    if control_list[i] == control_literal:
        count += 1
        if count == 2:
            print(i)
            break
if count < 2:
    print(-1)
