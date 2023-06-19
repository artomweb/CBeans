def get_permutations(t):
    permutations = []
    for i in range(len(t)):
        for j in range(len(t)):
            if i != j:
                permutations.append((t[i], t[j]))
    return permutations
my_tuple = (1, 2, 3)
result = get_permutations(my_tuple)
print(result)