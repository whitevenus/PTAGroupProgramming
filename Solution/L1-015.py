# 高精度四舍五入
from decimal import Decimal, ROUND_HALF_UP

# 获取输入
input_str = input()

# 输出
input_num, input_symbol = int(input_str.split(" ")[0]), input_str.split(" ")[1]
number = Decimal(input_num / 2)
rounded_number = number.quantize(Decimal(0), rounding=ROUND_HALF_UP)
for i in range(int(rounded_number)):
    for j in range(input_num):
        print(input_symbol, end="")
    print()
