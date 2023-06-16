import pygraphviz as pgv
import time


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


def findBeans(thisSol, allSols, graph, parent, memo):
    # If the solution has already been found, don't add it and don't check its children
    if tuple(thisSol) in memo:
        return allSols

    colour = "red" if thisSol in allSols else "green"

    node_id = str(len(allSols) + 1)

    graph.add_node(
        node_id, label=", ".join(map(str, thisSol)), fillcolor=colour, style="filled"
    )
    if parent:
        graph.add_edge(parent, node_id)

    allSols.append(thisSol)
    memo.add(tuple(thisSol))

    # If the solution just added was at the bottom of the tree, it has no children
    if len(thisSol) == 1:
        return allSols

    # Get all the child nodes of the current solution and explore them recursively
    theseSols = getDifferentSums(thisSol)
    for i in theseSols:
        findBeans(i, allSols, graph, node_id, memo)

    return allSols


toMake = 2

halfBeans = [0.5] * int(toMake / 0.5)

# Create a new graph
graph = pgv.AGraph()

# Create the root node
root_id = "0"
graph.add_node(root_id, label="Making " + str(toMake))


memo = set()
# Find and add beans recursively
t0 = time.time()
solutions = findBeans(halfBeans, [], graph, root_id, memo)
t1 = time.time()

graph.layout(prog="dot")

# Save the graph to a file
graph.draw("graph.png")


# print(getDifferentSums([1.5, 0.5, 0.5, 0.5]))

# exit()


# graph.render(filename='graph.dot')


print("\nNumber to count to:")
print(toMake)


solutions.sort(key=len, reverse=True)
print(solutions)

print("\nSolutions in numbers:")
allTexts = []
for i in solutions:
    print(i)
    allTexts.append(formatText(i))

print("\nSolutions in words:")
allTexts.sort(key=len, reverse=True)
for i in allTexts:
    print(i)

print("\nTotal number of solutions:")
print(len(solutions))


print("\nTime:")
print(t1 - t0, "seconds")
