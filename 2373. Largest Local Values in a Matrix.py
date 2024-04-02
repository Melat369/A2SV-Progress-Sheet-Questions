from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        new_matrix = []

        if rows > 2 and cols > 2:
            for i in range(rows - 2):
                row = []
                for j in range(cols - 2):
                    max_value = float('-inf')
                    for x in range(3):
                        for y in range(3):
                            max_value = max(max_value, grid[i + x][j + y])
                    row.append(max_value)
                new_matrix.append(row)

        return new_matrix