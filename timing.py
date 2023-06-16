import time
import matplotlib.pyplot as plt
import numpy as np


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


def getDifferentSums(beanCs):
    differentSums = set()

    for i in range(len(beanCs)):
        for j in range(i + 1, len(beanCs)):
            newSum = beanCs[i] + beanCs[j]

            if newSum in differentSums:
                continue

            newBeancombos = beanCs[:i] + beanCs[i + 1 : j] + beanCs[j + 1 :]
            newBeancombos.insert(0, newSum)
            newBeancombos.sort(reverse=True)
            differentSums.add(tuple(newBeancombos))

    return [list(combo) for combo in differentSums]


def findBeans(thisSol, allSols, memo):
    # If the solution has already been found, don't add it and don't check its children
    if tuple(thisSol) in memo:
        return allSols

    allSols.append(thisSol)
    memo.add(tuple(thisSol))

    # If the solution just added was at the bottom of the tree, it has no children
    if len(thisSol) == 1:
        return allSols

    # Get all the child nodes of the current solution and explore them recursively
    theseSols = getDifferentSums(thisSol)
    for i in theseSols:
        findBeans(i, allSols, memo)

    return allSols


# timings = []
# for i in range(0, 20):
#     halfBeans = [0.5] * int(i / 0.5)
#     t0 = time.time()
#     solutions = findBeans(halfBeans, [])
#     t1 = time.time()
#     timings.append([i, t1-t0])
#     print([i, t1-t0])


# print(timings)

# dfTImings = np.array(timings)

# plt.plot(dfTImings[:, 0], dfTImings[:, 1])


# plt.show()

toMake = 5

halfBeans = [0.5] * int(toMake / 0.5)
memo = set()
t0 = time.time()
solutions = findBeans(halfBeans, [], memo)
t1 = time.time()

# print(solutions)
print(t1 - t0)


# print(getDifferentSums([1, 0.5, 0.5]))
