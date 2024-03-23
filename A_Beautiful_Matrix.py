def beautifulMatrix(matrix):
    pos = [0, 0]
    s = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                pos = [abs(i - 2), abs(j - 2)]
                s = pos[0] + pos[1]
    return s

matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

result = beautifulMatrix(matrix)
print(result)