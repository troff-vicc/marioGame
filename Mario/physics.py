def completionMatrix1(matrix):
    for j in range(3):
        for i in range(len(matrix[13 + j])):
            matrix[13 + j][i] = 1
    matrix[10][4] = 2
    matrix[10][7] = 2
    matrix[10][9] = 2
    matrix[10][11] = 2
    matrix[10][12] = 2
    matrix[8][11] = 2
    matrix[10][8] = 3
    matrix[10][10] = 3
    matrix[7][9] = 3
    return matrix
def completionMatrix0(world):
    matrix = []
    for o in range(16):
        a = []
        for _ in range(16):
            a.append(0)
        matrix.append(a)
    if world == 1:
        matrix = completionMatrix1(matrix)
    return matrix
def main():
    matrix = completionMatrix0(1)
    return matrix
if __name__ == '__main__':
    a = main()
    for i in a:
        print(i)