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

            # print(newBeancombos, i, j)

            newBeancombos.remove(j)

            newBeancombos.insert(0, i + j)

            # print(newBeancombos)
            if newBeancombos not in differentSums:
                newBeancombos.sort(reverse=True)
                differentSums.append(newBeancombos)

    return differentSums


toMake = 0

beanCombos = [[0.5] * int(toMake / 0.5)]

# beanCombos = [[1, 0.5, 0.5]]

print("og beanCombos", beanCombos)


# def processChildren(thisBean, allBeanCombos):
#     if all([int(x) == toMake for x in beanCombos]):
#         return


# processChildren(beanCombos[0])


def expoloreChild(thisSum, allSums):
    if thisSum not in allSums:
        allSums.append(thisSum)
    else:
        return allSums
    if len(thisSum) == 1:
        return allSums

    # print("this sum", thisSum, "allSums", allSums)
    # print("allSums", allSums)

    theseSums = getDifferentSums(thisSum)
    for i in theseSums:
        expoloreChild(i, allSums)


allSums = []
for i in beanCombos:
    print("first beans", i)
    expoloreChild(i, allSums)


# for i in beanCombos:
#     sums = getDifferentSums(i)
#     # print(sums)
#     allSums += sums
#     for j in sums:
#         sums2 = getDifferentSums(j)
#         # print(sums2)
#         allSums += sums2
#         for k in sums2:
#             sums3 = getDifferentSums(k)
#             # print(sums3)
#             allSums += sums3


print()
print(allSums)
# beanCombos = [1, 0.5, 0.5]

print()
print()

allSums.sort(key=len, reverse=True)

allTexts = []
for i in allSums:
    print(i)
    allTexts.append(formatText(i))

print()
allTexts.sort(key=len, reverse=True)
for i in allTexts:
    # print(i)
    print(i)
print(len(allSums))

exit()

itt = 10

endState = False

allBeanCombos = []

while not endState:
    for i in beanCombos:
        beanCombos = getAllDifferentSums(beanCombos)

    for i in beanCombos:
        if i not in allBeanCombos:
            allBeanCombos.append(i)

    if all([int(x) == toMake for x in beanCombos]) or itt > 10:
        endState = True
    else:
        itt += 1

print(allBeanCombos)
# for i in beanCombos:
#     print(i)
#     print(formatText(i))
# if len(different) == 1:
#     newCombos = beanCombos.copy()
#     newCombos.insert(0, different[0] * 2)
# else:
#     for i in different:
#         newDifferent = different.copy()
#         newDifferent.remove(i)
#         for j in newDifferent:
#             print(i, j)
#             newCombos = beanCombos.copy()
#             newCombos.remove(i)
#             newCombos.remove(j)

#             newCombos.insert(0, i + j)
#             print(newCombos)


def getDifferentValues(arr):
    return list(set(arr))


# print(formatText(beanCombos))
