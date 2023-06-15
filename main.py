from treelib import Node, Tree




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

            if newBeancombos not in differentSums:
                newBeancombos.sort(reverse=True)
                differentSums.append(newBeancombos)

    return differentSums


toMake = 10

halfBeans = [0.5] * int(toMake / 0.5)


def findBeans(thisSol, allSols, tree, parent):
    # If the solution has already been found, don't add it and don't check it's children
    if thisSol in allSols:
        return allSols
    else:
        node_id = str(len(allSols) + 1)
        tree.create_node(", ".join(map(str, thisSol)), node_id, parent=parent)
        allSols.append(thisSol)
        
    # If the solution just added was at the bottom of the tree, it has no children
    if len(thisSol) == 1:
        return allSols

    # Get all the child nodes of current solution and explore them recursively
    theseSols = getDifferentSums(thisSol)
    for i in theseSols:
        findBeans(i, allSols, tree, parent=node_id)

    return allSols

# tree.create_node(", ".join(map(str, halfBeans)), "0"
# )
tree = Tree()
root_id = "0"
tree.create_node("Making " + str(toMake), root_id)
solutions = findBeans(halfBeans, [], tree, parent=root_id)

tree.show()
tree.to_graphviz(filename="graph")


# print("\nNumber to count to:")
# print(toMake)

solutions.sort(key=len, reverse=True)

# print("\nSolutions in numbers:")
# allTexts = []
for i in solutions:
    # print(i)
    # allTexts.append(formatText(i))
    print(formatText(i))

# print("\nSolutions in words:")
# allTexts.sort(key=len, reverse=True)
# for i in allTexts:
#     print(i)

# print("\nTotal number of solutions:")
# print(len(solutions))
