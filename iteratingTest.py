def get_permutations(t):
    permutations = []
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            permutations.append((t[i], t[j]))
    return permutations
my_tuple = (1, 2, 3)
result = get_permutations(my_tuple)
print(result)