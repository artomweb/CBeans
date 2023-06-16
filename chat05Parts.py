import time


def partitions(n):
    seen = set()
    yield (n,)
    for i in range(1, int(n // 0.5) + 1):
        for p in partitions(n - (i * 0.5)):
            partition = tuple(sorted(round(x, 1) for x in (i * 0.5,) + p))
            if all(element >= 0.5 for element in partition) and partition not in seen:
                seen.add(partition)
                yield partition


n = 25
t0 = time.time()
results = list(partitions(n))
t1 = time.time()

# print(results)
print(len(results))

print((t1 - t0) * 1000, "ms")
