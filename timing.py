import pygraphviz as pgv
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
    differentSums = []

    for i in beanCs:
        beanCombosCopy = beanCs.copy()
        beanCombosCopy.remove(i)
        for j in beanCombosCopy:
            newBeancombos = beanCombosCopy.copy()
            newBeancombos.remove(j)

            # newBeancombos is now an array of all the beans except from the two being summed
            newBeancombos.insert(0, i + j)

            newBeancombos.sort(reverse=True)

            if newBeancombos not in differentSums:
                differentSums.append(newBeancombos)

    return differentSums




def findBeans(thisSol, allSols):
    # If the solution has already been found, don't add it and don't check its children
    if thisSol in allSols:
        return allSols
        
    allSols.append(thisSol)
        
    # If the solution just added was at the bottom of the tree, it has no children
    if len(thisSol) == 1:
        return allSols

    # Get all the child nodes of the current solution and explore them recursively
    theseSols = getDifferentSums(thisSol)
    for i in theseSols:
        findBeans(i, allSols)

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

halfBeans = [0.5] * int(15 / 0.5)
t0 = time.time()
solutions = findBeans(halfBeans, [])
t1 = time.time()

print(solutions)
print(t1-t0)