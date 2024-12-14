
from random import randint
import time
def longest_sub(array_len, array):
    inf = float('inf')
    F = [inf] * (array_len + 1)
    F[0] = -inf
    for i in range(array_len):
        left = 0
        right = array_len
        while right - left > 1:
            middle = (left + right) // 2
            if F[middle] >= array[i]:
                right = middle
            else:
                left = middle
        F[right] = array[i]
    result = F[1:F.index(inf)]
    return len(result), result
print(longest_sub(9, [3, 29, 5, 5, 28, 6, 7, 5, 89]))
start = time.time()
print(longest_sub( 300000, [randint(-10**9, 10**9) for _ in range(300000)]))
print(time.time() - start)