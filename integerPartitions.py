import time
def partition(number, memo={}):
    if number in memo:
        return memo[number]

    answer = set()
    answer.add((number,))

    for x in range(1, int(number * 2)):
        for y in partition(number - x / 2, memo):
            answer.add(tuple(sorted((x / 2,) + y)))

    memo[number] = answer
    return answer



# Example usage
n = 2
print(f"Partitions of {n} with integer and 0.5 sums:")
t0 = time.time()
partitions = list(partition(n))
t1 = time.time()
# print(partitions)
print(len(partitions))
print(t1-t0, "seconds")
