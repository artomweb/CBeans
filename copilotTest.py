import time
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



# A function to find the 0.5 partitions of an integer, for example the partitions of 1 are [(0.5, 0.5), (1,)]
# and the partitions of 2 are [(2.0,), (1.0, 1.0), (0.5, 0.5, 1.0), (0.5, 0.5, 0.5, 0.5), (0.5, 1.5)]
# the partitions of 3 are [(1.0, 2.0), (1.5, 1.5), (0.5, 0.5, 2.0), (0.5, 0.5, 0.5, 0.5, 1.0), (0.5, 2.5), (0.5, 0.5, 0.5, 1.5), (3.0,), (0.5, 0.5, 1.0, 1.0), (0.5, 1.0, 1.5), (0.5, 0.5, 0.5, 0.5, 0.5, 0.5), (1.0, 1.0, 1.0)]
# the partitions of 4 are [(0.5, 0.5, 0.5, 2.5), (0.5, 0.5, 0.5, 0.5, 0.5, 1.5), (2.0, 2.0), (1.0, 3.0), (1.5, 2.5), (0.5, 0.5, 1.0, 1.0, 1.0), (0.5, 1.5, 2.0), (4.0,), (0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5), (0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0), (0.5, 0.5, 3.0), (1.0, 1.0, 1.0, 1.0), (0.5, 3.5), (0.5, 1.0, 2.5), (1.0, 1.0, 2.0), (0.5, 1.0, 1.0, 1.5), (1.0, 1.5, 1.5), (0.5, 0.5, 0.5, 0.5, 2.0), (0.5, 0.5, 1.0, 2.0), (0.5, 0.5, 0.5, 1.0, 1.5), (0.5, 0.5, 1.5, 1.5), (0.5, 0.5, 0.5, 0.5, 1.0, 1.0)]


def partition(number, memo={}):
    if number in memo:
        return memo[number]

    answer = set()
    answer.add((number,))

    for x in range(1, int(number * 2)):
        remaining_number = number - x / 2

        if remaining_number < x / 2:
            break

        for y in partition(remaining_number, memo):
            answer.add(tuple(sorted((x / 2,) + y)))

    memo[number] = answer
    return answer

# use the above function to find the 0.5 partitions of 2
# print(partition(3))

# test the speed of the partition function for an input of 10
t0 = time.time()
solutions = partition(20)
t1 = time.time()
print(len(solutions))
print((t1 - t0) * 1000, "ms")
