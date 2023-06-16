import time


def partition(number):
    partitions = [[] for _ in range(int(number * 2) + 1)]
    partitions[0] = [[]]

    for i in range(1, int(number * 2) + 1):
        for j in range(i, int(number * 2) + 1):
            for partition in partitions[j - i]:
                partitions[j].append(partition + [i / 2])

    return partitions[int(number * 2)]


n = 15
t0 = time.time()
partitions = partition(n)
partitions_set = [tuple(sorted(partition)) for partition in partitions]
t1 = time.time()

# print(partitions_set)
print(len(partitions_set))

print((t1 - t0) * 1000, "ms")
