# 获取输入
input_num = int(input())

num_list = []
for i in range(input_num):
    num_list.append(int(input()))


# 判断是否是素数
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 输出
for num in num_list:
    if is_prime(num):
        print("Yes")
    else:
        print("No")