def partitions(n, I=1):
    yield (n,)
    for i in range(I, int(n / 1.5)):
        for p in partitions(n - i, i):
            yield (i,) + p


r1 = list(partitions(5))

print(r1)
