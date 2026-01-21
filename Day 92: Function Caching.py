import functools
import time


@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * 5


print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

# memoization based on cache
# No need to compute again because results are already stored in cache
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
