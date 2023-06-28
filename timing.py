import time
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
import math


def formatText(beanCs):
    outputArr = []
    for bean in beanCs:
        thisOut = ""
        if bean == 0.5:
            thisOut += "half a bean"
        else:
            if (bean % 1) == 0.5:
                thisOut += str(int(bean)) + " and a half"
            else:
                thisOut += str(int(bean))

            if bean > 1:
                thisOut += " beans"
            else:
                thisOut += " bean"

        outputArr.append(thisOut)

    return ", ".join(outputArr)

def compute_addition_possibilities(arr):
    n = len(arr)
    possibilities = set()

    for i in range(n - 1):
        for j in range(i + 1, n):
            sum1 = arr[i] + arr[j]
            sum2 = [sum1] + [x for idx, x in enumerate(arr[j + 1:], start=j + 1) if idx != i]
            possibilities.add(tuple(sum2))

    return possibilities


from itertools import permutations


def getDifferentSums(beanCs):
    differentSums = set()
    sumVariations = set()
    

    for i in range(len(beanCs)):
        for j in range(i + 1, len(beanCs)):
            newSum = beanCs[i] + beanCs[j]

            if newSum in sumVariations:
                break
            
            sumVariations.add(newSum)

            newBeanCombos = (newSum, ) + beanCs[:i] + beanCs[i + 1:j] + beanCs[j + 1:]
            differentSums.add(tuple(sorted(newBeanCombos)))


    return differentSums




def findBeans(thisSol, allSols):
    # If the solution has already been found, don't add it and don't check its children
    if thisSol in allSols:
        return allSols

    allSols.add(thisSol)

    # If the solution just added was at the bottom of the tree, it has no children
    if len(thisSol) == 1:
        return allSols

    # Get all the child nodes of the current solution and explore them recursively
    theseSols = getDifferentSums(thisSol)
    for i in theseSols:
        findBeans(i, allSols)


    return allSols


# timings = []

# start = 0
# stop = 25

# for i in range(start, stop + 1):
#     halfBeans = tuple([0.5] * int(i / 0.5))
#     t0 = time.time()
#     solutions = findBeans(halfBeans, set())
#     t1 = time.time()
#     timings.append([i, (t1-t0) * 1000])
#     print([i, (t1-t0) * 1000])


# print(timings)


# dfTImings = np.array(timings)
# np.savetxt("foo.csv", dfTImings, delimiter=",")

# new_list = range(start, stop+1)
# plt.xticks(new_list)

# plt.plot(dfTImings[:, 0], dfTImings[:, 1])

# plt.xlabel("Count to")
# plt.ylabel("Execution time (ms)")

# plt.show()

toMake = 20

halfBeans = tuple([0.5] * int(toMake / 0.5))
t0 = time.time()
solutions = findBeans(halfBeans, set())
t1 = time.time()

# print(list(solutions))
print(len(solutions))
print((t1 - t0) * 1000, "ms")

# print(getDifferentSums((1, 2, 3)))


# print(getDifferentSums([1, 0.5, 0.5]))



# Example usage
# arr = [ 1.5, 0.5, 0.5, 1]

# print(getDifferentSums(tuple(arr)))



# t0 = time.time()
# pairs = set()
# for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             pairs.add((arr[i], arr[j]))
# t1 = time.time()

# print(pairs)
# print((t1 - t0) * 1000, "ms")

# t0 = time.time()
# combs = set(combinations(arr, 2))
# t1 = time.time()
# print(combs)
# print((t1 - t0) * 1000, "ms")

# beanCombos = [1.5, 1, 0.5, 0.5, 0.5]

# print(getDifferentSums(beanCombos))