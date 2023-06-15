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


toMake = 10

halfBeans = [0.5] * int(toMake / 0.5)


def findBeans(thisSol, allSols, graph, parent):
    # If the solution has already been found, don't add it and don't check its children
    if thisSol in allSols:
        return allSols
        
    colour = "red" if thisSol in allSols else "green"

    node_id = str(len(allSols) + 1)

    graph.add_node(node_id, label=", ".join(map(str, thisSol)), fillcolor=colour, style="filled")
    if parent:
        graph.add_edge(parent, node_id)
    allSols.append(thisSol)
        
    # If the solution just added was at the bottom of the tree, it has no children
    if len(thisSol) == 1:
        return allSols

    # Get all the child nodes of the current solution and explore them recursively
    theseSols = getDifferentSums(thisSol)
    for i in theseSols:
        findBeans(i, allSols, graph, parent=node_id)

    return allSols

# Create a new graph
graph = pgv.AGraph()

# Create the root node
root_id = "0"
graph.add_node(root_id, label="Making " + str(toMake))

# Find and add beans recursively
t0 = time.time()
solutions = findBeans(halfBeans, [], graph, parent=root_id)
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
# print(solutions)

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
print(t1-t0, "seconds")
