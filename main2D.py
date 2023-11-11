def square(fn):
    global xy, l
    import physics
    s = 2
    f = False
    matrix, matrixMario = physics.main(fn)
    for lin in range(len(matrix)):
        for u in range(len(matrix[lin])):
            o = matrix[lin][u]
            for i in range(35):
                for j in range(176):
                    x = 5 * u
                    y = 2 * lin
                    if s*2.5//2 + x > j and  x - s*2.5//2 < j and s//2 + y > i and y - s//2 < i:
                        #k = (abs(xl - j) // 3 + abs(yl - i) // 3) // 2
                        if o == 0:
                            xy[j][i] = l[len(l)-1]
                        elif o == 1:
                            xy[j][i] = l[0]
                        elif o == 2:
                            xy[j][i] = l[5]
                        elif o == 4:
                            xy[j][i] = l[1]
    for lin in range(len(matrixMario)):
        try:
            h1 = matrixMario[lin].index(4)
            h0 = lin + 8
            f = True
        except:
            None
        if f:
            break
    for i in range(35):
        for j in range(176):
            x = 5 * h1 // 16
            y = 2 * h0 // 16
            if x == j and y == i:
                xy[j][i] = '▅'
def main():
    import time
    global xy, l
    #l = ':!/r(1Z4H9$8W@'
    l = '█▇▆▅▄▃▂ '
    xy = []
    for _ in range(176):
        y = []
        for _ in range(35):
            y.append(l[7])
        xy.append(y)
    c = 0
    #square(400, 17, 15, c*17, c*3)
    while True:
        square(c)
        for i in range(35):
            summ = ''
            for j in range(0, 172):
                summ += xy[j][i]
            print(summ)
        c+=1
        time.sleep(0.5)
if __name__ == '__main__':
    main()