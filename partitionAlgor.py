import time
def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

n = 50
print(f"Partitions of {n} with integer and 0.5 sums:")
t0 = time.time()
partitions = list(partitions(n))
t1 = time.time()
# print(partitions)
print(len(partitions))
print(t1-t0, "seconds")