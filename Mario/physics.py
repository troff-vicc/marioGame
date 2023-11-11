def completionMatrix1(matrix):
    # создание 1го уровня
    # тип текстуры 1 - фон, 2 - кирпич, 3 - вопрос, 4 - труба
    matrix = [
        #0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 0
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 6
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],# 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 9
        [0, 0, 3, 0, 0, 2, 3, 2, 3, 2, 0, 0, 0, 0, 0, 0],# 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],# 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 13
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],# 14
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 15
    ]

    '''briks = [
        [6, 10],
        [8, 10],
        [10, 10]
    ]
    questions = [
        [2, 10],
        [7, 10],
        [9, 10],
        [8, 7]
    ]
    pipes = [[14, 11],[15, 12],[14, 13],[15, 13]]
    floors = [[x, 14] for x in range(16)] + [[x, 15] for x in range(16)]

    for brik in briks:
        matrix[brik[1]][brik[0]] = 2
    for question in questions:
        matrix[question[1]][question[0]] = 3
    for pipe in pipes:
        matrix[pipe[1]][pipe[0]] = 4
    for floor in floors:
        matrix[floor[1]][floor[0]] = 1'''
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