# 获取输入
input_num = input()
input_list = input().split(" ")

# 整理数据
zi_list, mu_list = [], []
for item in input_list:
    zi, mu = int(item.split("/")[0]), int(item.split("/")[1])
    zi_list.append(zi)
    mu_list.append(mu)


def gcd(a, b):
    """ 计算两个数的最大公约数 """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """ 求最小公倍数 """
    return a * b // gcd(a, b)


# 所有分母的公倍数
tmp = mu_list[0]
for mu in mu_list:
    tmp = lcm(tmp, mu)

total = 0
for index, zi in enumerate(zi_list):
    total += zi * (tmp // mu_list[index])

gcd_num = gcd(total, tmp)
res_zi, res_mu = total // gcd_num, tmp // gcd_num
num1, num2 = res_zi // res_mu, res_zi % res_mu
if num1 > 0 and num2 == 0:
    print(num1)
elif num1 == 0:
    print("{}/{}".format(num2, res_mu))
else:
    print(num1, "{}/{}".format(num2, res_mu))