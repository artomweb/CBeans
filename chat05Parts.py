import time


def partitions(n):
    result = {(n,)}
    for i in range(1, int(n * 2)):
        for p in partitions(n - i / 2):
            result.add(tuple(sorted((i / 2,) + p)))
    return result


n = 10
t0 = time.time()
results = list(partitions(n))
t1 = time.time()

# print(results)
print(len(results))

print((t1 - t0) * 1000, "ms")
