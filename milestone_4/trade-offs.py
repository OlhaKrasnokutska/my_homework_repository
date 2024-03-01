from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    n = len(li)
    for i in range(n):
        for j in range(i + 1, n):
            if li[i] + li[j] == target:
                return (li[i], li[j])

result_brute_force = find_sum(5, [1, 2, 3, 4, 5])
assert result_brute_force in {(1, 4), (2, 3)}
print(result_brute_force)

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    seen_numbers = set()
    for num in li:
        complement = target - num
        if complement in seen_numbers:
            return (complement, num)
        seen_numbers.add(num)

result_optimized = find_sum_fast(5, [1, 2, 3, 4, 5])
assert result_optimized in {(1, 4), (2, 3)}
print(result_optimized)
