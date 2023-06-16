def rule_asc(n):
    a = [0.0] * (n + 1)
    k = 1
    a[1] = n - 0.5
    while k != 0:
        yield tuple([round(num, 1) for num in a[1:k + 1]])
        x = a[k - 1] + 0.5
        y = a[k] - 0.5
        k -= 1
        while x < y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y





import time
n = 2
print(f"Partitions of {n} with integer and 0.5 sums:")
t0 = time.time()
partitions = list(rule_asc(n))
t1 = time.time()
print(partitions)
print(len(partitions))
print(t1-t0, "seconds")
