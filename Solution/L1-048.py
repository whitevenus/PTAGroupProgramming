# 获取输入
a_shape_str = input()
r_a, c_a = a_shape_str.split(" ")

a = []
for i in range(int(r_a)):
    a.append(input().split(" "))

b_shape_str = input()
r_b, c_b = b_shape_str.split(" ")

b = []
for i in range(int(r_b)):
    b.append(input().split(" "))


# 计算输出
if int(c_a) != int(r_b):
    print("Error: {} != {}".format(c_a, r_b))
else:
    print(r_a, c_b)
    for i in range(int(r_a)):
        c = []
        for j in range(int(c_b)):
            total = 0
            for k in range(int(r_b)):
                num = int(a[i][k]) * int(b[k][j])
                total += num
            c.append(str(total))
        print(" ".join(c))



