# How many beans make n?

A write up of code which calculates the number of solutions to the question “How many beans make n?”.

# How many beans?

There are **42** solutions to the question **"How many beans make five?”**

# Original Question

> **How many beans make five?**
> Two beans, one and a half beans, half a bean and a bean

**Background:**

This question is one often given to children where the child should reply with any combination of beans which adds up to five. It is also used to describe someone who has their wits about them or who knows their stuff. This format of the phrase comes from the late 18th/early 19th century.

“It derives from an earlier expression 'to know one's beans' which means to know one's topic or subject, whatever it may be, and which dates from the late 1600s. (The beans are thought to refer to the beans or beads on an abacus. If you did not know how to use an abacus, then you did not know your beans.)“

[https://idiomorigins.org/origin/know-how-many-beans-make-five](https://idiomorigins.org/origin/know-how-many-beans-make-five)

The number that is being “counted to” is not given, “five what?”.

## Assumptions made

1. That there are 4 fundamental beans in the original answer: “two beans”, “one and a half beans”, “half a bean” and “a bean”.

   This assumes that “half a bean and a bean” is not one indivisible unit and that it can in fact be broken up into “ half a bean” and “a bean”

   That “One and a half beans” is **not** the same as “One bean, and half a bean”.

   Therefore these beans cannot be combined. As shown in the original answer.

   In other words, these two sentences are **not** the same:

   “One bean, half a bean”

   “One and a half beans”

   Another example, these two sentences are **\*\***not**\*\*** the same:

   “Two beans, Two beans”

   “Four beans”

2. That the idea of beans and their fractional parts can be extended past 2 beans.

   The original answer included 2 and fewer beans. However, it is assumed that “2 and a half beans” etc. also exist.

3. That the answers are [commutative](https://en.wikipedia.org/wiki/Commutative_property) and therefore only distinct solutions are accepted

   For example, these two sentences will be treated as equal and only counted once:

   “One bean, two beans”

   “Two beans, One bean”

## Formatting the answers

From here onwards:

1. Words for whole beans are replaced by their digits.
2. Additional words such as “and” are removed.
3. Numbers of beans are sorted from high to low.

For example, the original answer is now:

“2 beans, 1 and a half beans, 1 bean, half a bean”

In the diagrams each solution such as “2 beans, 1 and a half beans and half a bean” is represented as “2, 1.5, 0.5” inside a rectangle.

# Calculating combinations of beans

We will step through the algorithm for calculating combinations of beans using a tree structure. Each arrow represents the addition of two values in the previous rectangle

### Combinations for 1:

We will start with the simplest case, **1**.

Starting with the most number of “half a bean”s which will make 1. There is only one possible addition that we can do as there is only one unique number, so 0.5 + 0.5 = 1.

![Untitled](How%20many%20beans%20d96229a7d72d4c9c858f2ffcff5c9c5b/Untitled.png)

### Combinations for 2

There are a few more combinations for **2**.

Again we start with the most number of half beans, which in this case is **4**.

At the beginning there is again only one possible combination of beans which is 0.5 + 0.5 = 1. After doing the addition, “1 bean” and two “half beans” remain.

On the next step, there are two additions which can be made as there are two unique numbers. We could either combine the “1 bean” and one of the “half beans” to make “1 and a half beans”. Or we could again combine two “half beans”. These two possibilities are shown in the tree.

Both of these possibilities will then add to 2. Meaning there are no more solutions.

![Untitled](How%20many%20beans%20d96229a7d72d4c9c858f2ffcff5c9c5b/Untitled%201.png)

### Combinations for 3

Highlighted are the 11 unique solutions for 3. As you can see, the number of solutions grows rapidly:

![Untitled](How%20many%20beans%20d96229a7d72d4c9c858f2ffcff5c9c5b/Untitled%202.png)

## Optimisations in the code:

For combinations of 3 there is a lot of duplication. Duplicate solutions are **not** highlighted. Once a solution is obtained that is already in the list of solutions, there is no need to check its children, as they will be the same. This can be a huge performance increase for the code.

## Code

The code is based upon recursively exploring this tree structure.

This function is how we find the children of each node in the tree. For example, starting from an array of [1, 0.5, 0.5] it will output the two options as [[1.5, 0.5], [1, 1]]

We iterate over every combination of unique pairs in the array and calculate their sum. If we haven’t seen this sum before then we can add the new solution to the array of different sums. The output is given as a set for faster lookups of “if x in sums”.

The nested for loop compares each element with all of the elements after it, this will only find all of the unique combinations if the array is sorted.

The sum variations set helps to efficiently skip through duplicate entries, for example if the input is (0.5, 0.5, 0.5, 1). Only the sums for the first 0.5 are calculated and the rest are skipped because they will be the same.

```python
def getDifferentSums(beanCs):
    differentSums = set()
    sumVariations = set()

	# For each pair of unique values in the array
    for i in range(len(beanCs)):
        for j in range(i + 1, len(beanCs)):
            newSum = beanCs[i] + beanCs[j]

			# If this sum has already been made then this solution is a duplicate
            if newSum in sumVariations:
                break

            sumVariations.add(newSum)

			# Create a new tuple with the sum and then sort it to remove non destinct duplicates
            newBeanCombos = (newSum, ) + beanCs[:i] + beanCs[i + 1:j] + beanCs[j + 1:]
            differentSums.add(tuple(sorted(newBeanCombos)))

    return differentSums
```

## Recursively navigating the tree structure:

This recursive function is used to navigate each node in the tree and returns a list of all of the solutions.

```python
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
```

We start with an array of half beans with the same length as the number of beans that we want to make. This is the first node in the tree.

```python
toMake = 20

halfBeans = tuple([0.5] * int(toMake / 0.5))

solutions = findBeans(halfBeans, set())
```

### A graph of execution time in ms **vs** number counted to

Counting to 25 takes nearly 7 seconds

![ExecutionTIme.png](How%20many%20beans%20d96229a7d72d4c9c858f2ffcff5c9c5b/ExecutionTIme.png)

# Solutions in words:

The singular bean solution such as “1 bean” can be omitted.

### The solutions for 1 to 5 are:

### 1 (2 solutions)

half a bean, half a bean\
1 bean\

### 2 (5 Solutions)

half a bean, half a bean, half a bean, half a bean\
1 bean, half a bean, half a bean\
1 and a half beans, half a bean\
1 bean, 1 bean\
2 beans\

### 3 (11 Solutions)

half a bean, half a bean, half a bean, half a bean, half a bean, half a bean\
1 bean, half a bean, half a bean, half a bean, half a bean\
1 and a half beans, half a bean, half a bean, half a bean\
1 bean, 1 bean, half a bean, half a bean\
1 and a half beans, 1 bean, half a bean\
1 and a half beans, 1 and a half beans\
2 beans, half a bean, half a bean\
2 and a half beans, half a bean\
1 bean, 1 bean, 1 bean\
2 beans, 1 bean\
3 beans\

### 4 (22 Solutions)

half a bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean\
1 bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean\
1 and a half beans, half a bean, half a bean, half a bean, half a bean, half a bean\
1 bean, 1 bean, half a bean, half a bean, half a bean, half a bean\
1 and a half beans, 1 bean, half a bean, half a bean, half a bean\
1 and a half beans, 1 and a half beans, half a bean, half a bean\
2 beans, half a bean, half a bean, half a bean, half a bean\
2 and a half beans, half a bean, half a bean, half a bean\
1 bean, 1 bean, 1 bean, half a bean, half a bean\
1 and a half beans, 1 bean, 1 bean, half a bean\
1 and a half beans, 1 and a half beans, 1 bean\
2 beans, 1 bean, half a bean, half a bean\
2 beans, 1 and a half beans, half a bean\
2 and a half beans, 1 bean, half a bean\
2 and a half beans, 1 and a half beans\
3 beans, half a bean, half a bean\
3 and a half beans, half a bean\
1 bean, 1 bean, 1 bean, 1 bean\
2 beans, 1 bean, 1 bean\
2 beans, 2 beans\
3 beans, 1 bean\
4 beans\

### 5 (42 Solutions)

half a bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean\
1 bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean\
1 and a half beans, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean\
1 bean, 1 bean, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean\
1 and a half beans, 1 bean, half a bean, half a bean, half a bean, half a bean, half a bean\
1 and a half beans, 1 and a half beans, half a bean, half a bean, half a bean, half a bean\
2 beans, half a bean, half a bean, half a bean, half a bean, half a bean, half a bean\
2 and a half beans, half a bean, half a bean, half a bean, half a bean, half a bean\
1 bean, 1 bean, 1 bean, half a bean, half a bean, half a bean, half a bean\
1 and a half beans, 1 bean, 1 bean, half a bean, half a bean, half a bean\
1 and a half beans, 1 and a half beans, 1 bean, half a bean, half a bean\
1 and a half beans, 1 and a half beans, 1 and a half beans, half a bean\
2 beans, 1 bean, half a bean, half a bean, half a bean, half a bean\
2 beans, 1 and a half beans, half a bean, half a bean, half a bean\
2 and a half beans, 1 bean, half a bean, half a bean, half a bean\
2 and a half beans, 1 and a half beans, half a bean, half a bean\
3 beans, half a bean, half a bean, half a bean, half a bean\
3 and a half beans, half a bean, half a bean, half a bean\
1 bean, 1 bean, 1 bean, 1 bean, half a bean, half a bean\
1 and a half beans, 1 bean, 1 bean, 1 bean, half a bean\
1 and a half beans, 1 and a half beans, 1 bean, 1 bean\
2 beans, 1 bean, 1 bean, half a bean, half a bean\
**2 beans, 1 and a half beans, 1 bean, half a bean ← Original Answer**\
2 and a half beans, 1 bean, 1 bean, half a bean\
2 beans, 1 and a half beans, 1 and a half beans\
2 and a half beans, 1 and a half beans, 1 bean\
2 beans, 2 beans, half a bean, half a bean\
3 beans, 1 bean, half a bean, half a bean\
3 beans, 1 and a half beans, half a bean\
2 and a half beans, 2 beans, half a bean\
3 and a half beans, 1 bean, half a bean\
1 bean, 1 bean, 1 bean, 1 bean, 1 bean\
3 and a half beans, 1 and a half beans\
2 and a half beans, 2 and a half beans\
4 beans, half a bean, half a bean\
2 beans, 1 bean, 1 bean, 1 bean\
4 and a half beans, half a bean\
2 beans, 2 beans, 1 bean\
3 beans, 1 bean, 1 bean\
3 beans, 2 beans\
4 beans, 1 bean\
5 beans\

The sequence of solution counts follows, 1, 2, 5, 11, 22, 42, 77, 135, 231, 385, 627, 1002, 1575, 2436, 3718.

This aligns to the number of ways to partition 2n into positive integers. [(OEIS LINK)](https://oeis.org/A058696)

The reason that we use 2n is because 0.5 (”half a bean”) is used, therefore instead of partitioning into integers, we are partitioning into 0.5 increments which means there are twice the number of options.

The sequence of 2n is used because between 0 and 5 there are actually 10 numbers in 0.5 increments and 10 = 2 \* 5.

This is called partition in number theory. [(wikipedia)](<https://en.wikipedia.org/wiki/Partition_(number_theory)>)

The seven integer partitions of 5 are

- 5
- 4 + 1
- 3 + 2
- 3 + 1 + 1
- 2 + 2 + 1
- 2 + 1 + 1 + 1
- 1 + 1 + 1 + 1 + 1

There are 42 integer partitions of 10. So for 0.5 increments there are 42 partitions of 5.

Below is the list of values [(OEIS LINK)](https://oeis.org/A058696/list):

| n   | a(n)    |
| --- | ------- |
| 0   | 1       |
| 1   | 2       |
| 2   | 5       |
| 3   | 11      |
| 4   | 22      |
| 5   | 42      |
| 6   | 77      |
| 7   | 135     |
| 8   | 231     |
| 9   | 385     |
| 10  | 627     |
| 11  | 1002    |
| 12  | 1575    |
| 13  | 2436    |
| 14  | 3718    |
| 15  | 5604    |
| 16  | 8349    |
| 17  | 12310   |
| 18  | 17977   |
| 19  | 26015   |
| 20  | 37338   |
| 21  | 53174   |
| 22  | 75175   |
| 23  | 105558  |
| 24  | 147273  |
| 25  | 204226  |
| 26  | 281589  |
| 27  | 386155  |
| 28  | 526823  |
| 29  | 715220  |
| 30  | 966467  |
| 31  | 1300156 |
| 32  | 1741630 |
| 33  | 2323520 |
| 34  | 3087735 |
| 35  | 4087968 |
| 36  | 5392783 |
| 37  | 7089500 |
| 38  | 9289091 |
