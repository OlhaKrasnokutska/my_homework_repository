from typing import List
def get_triangle(rows: int) -> List[List[int]]:
    triangle = [[1] * (i + 1) for i in range(rows)]

    for i in range(2, rows):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle

def print_triangle(triangle: List[List[int]]):
    for row in triangle:
        space = len(triangle) - len(row)
        print(f"{' ' * space} {' '.join(map(str, row))}")

triangle = get_triangle(5)
print_triangle(triangle)
