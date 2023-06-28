import time


def partitions(n):
    yield (n / 2,)
    for i in range(1, n // 2 + 1):
        for p in partitions(n - i):
            yield tuple(sorted((i / 2,) + p))


n = 10
t0 = time.time()
results = list(partitions(n * 2))
t1 = time.time()
print(len(results))
print((t1 - t0) * 1000, "ms")



t0 = time.time()
iParts = set(partitions(20))
t1 = time.time()

# print(iParts)


# print(results)
print(len(iParts))

print((t1 - t0) * 1000, "ms")
