def beans_make_n(n, current_solution, solutions):
    # Base case: If n is 0, we have found a valid solution
    if n == 0:
        sorted_solution = sorted(current_solution)  # Sort the solution
        solutions.append(', '.join(sorted_solution))
        return
    
    # Recursive case: Try different combinations of beans
    if n >= 2:
        new_solution = current_solution + ['2 beans']
        beans_make_n(n-2, new_solution, solutions)
    if n >= 1.5:
        new_solution = current_solution + ['1 and a half beans']
        beans_make_n(n-1.5, new_solution, solutions)
    if n >= 1:
        new_solution = current_solution + ['1 bean']
        beans_make_n(n-1, new_solution, solutions)
    if n >= 0.5:
        new_solution = current_solution + ['half a bean']
        beans_make_n(n-0.5, new_solution, solutions)

def get_unique_solutions(solutions):
    # Remove duplicates from the list of solutions
    unique_solutions = list(set(solutions))
    return unique_solutions

n = 11  # Change the value of n here to calculate solutions for a different number

all_solutions = []
beans_make_n(n, [], all_solutions)
unique_solutions = get_unique_solutions(all_solutions)

unique_solutions.sort(key=len, reverse=True)


print(f"All possible solutions for 'How many beans make {n}?' are:")
for solution in unique_solutions:
    print(solution)
