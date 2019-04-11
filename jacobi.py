# -*- coding: utf-8 -*-

def Jacobi(mx, mr, n=100, c=0.0001):
    if len(mx) == len(mr):  # 若mx和mr长度相等则开始迭代 否则方程无解
        x = []  # 迭代初值 初始化为单行全0矩阵
        for i in range(len(mr)):
            x.append([0])
        count = 0  # 迭代次数计数
        while count < n:
            nx = []  # 保存单次迭代后的值的集合
            for i in range(len(x)):
                nxi = mr[i][0]
                for j in range(len(mx[i])):
                    if j != i:
                        nxi = nxi + (-mx[i][j]) * x[j][0]
                nxi = nxi / mx[i][i]
                print(nxi)
                nx.append([nxi])  # 迭代计算得到的下一个xi值
            lc = []  # 存储两次迭代结果之间的误差的集合
            for i in range(len(x)):
                lc.append(abs(x[i][0] - nx[i][0]))
            if max(lc) < c:
                return nx  # 当误差满足要求时 返回计算结果
            x = nx
            count = count + 1
            print(count)
        return False  # 若达到设定的迭代结果仍不满足精度要求 则方程无解
    else:
        return False

def Gauss1(mx,mr,n=100,c=0.001):
    if len(mx) == len(mr):      #若mx和mr长度相等则开始迭代 否则方程无解
        x = []   #迭代初值 初始化为单行全0矩阵
        for i in range(len(mr)):
            x.append([0])
        count = 0    #迭代次数计数
        while count < n:
            print(count)
            p = 0
            for i in range(len(x)):
                nxi = mr[i][0]
                t = x[i][0]
                for j in range(len(mx[i])):
                    if j != i:
                        nxi = nxi+(-mx[i][j])*x[j][0]
                nxi = nxi/mx[i][i]
                x[i][0] = nxi
                if abs(x[i][0]-t) > p:
                    p = abs(x[i][0] - t)
                if p < c:
                    return x
            count = count + 1
            print(x)
        return x
    else:
        return False


# 调用 Jacobi(mx,mr,n=100,c=0.001) 示例
ma = [[-8, 1, 1], [1, -5, 1], [1, 1, -4]]
mb = [[1], [16], [7]]
#print(Jacobi(ma, mb, 100, 0.001))
print(Gauss1(ma, mb, 20))