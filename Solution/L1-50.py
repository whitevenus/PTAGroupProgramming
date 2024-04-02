# 获取输入
import math

input_str = input()
l, n = int(input_str.split(" ")[0]), int(input_str.split(" ")[1])

# 输出
if n <= 26:
    for j in range(l - 1):
        print("z", end="")
    print(chr(ord('z') - n + 1), end="")
else:
    for i in range(1, l + 1):
        if math.pow(26, i) < n < math.pow(26, i + 1):
            num = n
            for j in range(i, 0, -1):
                num1 = int(num // math.pow(26, j))
                num2 = int(num % math.pow(26, j))
                num = num2
                print(chr(ord('z') - num1), end="")
                if num2 == 0:
                    print("z", end="")
                elif num2 < 26:
                    print(chr(ord('z') - num2 + 1), end="")

