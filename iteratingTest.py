beanCs = [3, 2, 1]
combinations = []
for i in range(len(beanCs)):
    for j in range(i + 1, len(beanCs)):
        combination = (beanCs[i], beanCs[j])
        combinations.append(combination)

print(combinations)
