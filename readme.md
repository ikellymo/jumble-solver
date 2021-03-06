# Jumble Solver 
## Intro 
This is an exploration of solutions to the 
[jumble](https://en.wikipedia.org/wiki/Jumble) algorithm 
and associated timing improvements. The repo contains three
code versions, each with improving execution time and 
decreasing complexity. 
## Jumble
The idea behind the solver is to input a string that is a
jumble of characters and algorithmically determine all
possible anagrams, or words that can be made from different
permutations of the input string. The number of possible 
permutations goes as $$n!$$, when all the elements are 
selected. All these permutations can then be checked 
against a table of words, so that only real words are 
reported. 

Optionally, all the possible substring combination of 
the input jumble can considered as well to determine the 
smaller anagrams that can be made from the input. *This 
solver implements this.*
## Approach & Complexity
**Version 0.1** implements the algorithm mostly described 
[here](https://en.wikipedia.org/wiki/Jumble_algorithm) and
generates all the possible permutations by inserting each
character in all possible positions in an already existing 
list of permutations, careful to seed the next round with
a single character. For an input of 123:
```
1   2   3
-----------
1   21  321 
        231
        213
    12  312
        132
        123
    2   32
        23
        3  
```
The number of permutations for each combination blows up 
at a rate a bit greater than **n!**. More specifically, 
n!+(n-1)!+(n-2)!... 
```python
for j in range(0, len(jumble)):
    # Add the next letter in the jumble to each position of each existing permutation
    for perm in perms:  # len(jumble):num_permutations - 1:1, 2:4, 3:15, 4:64, 5:325, 6:1956, 7:13699
        for p in range(0, len(perm) + 1):
            temp.append(perm[:p] + jumble[j] + perm[p:])

    temp.append(jumble[j])

    for new_perm in temp:
        if new_perm not in perms:
            perms.append(new_perm)
```
What's even worse here is that each character loop includes
a search through the existing list of permutations, 
so this quickly turns into **O(n(n!))** or worse. 

**Version 0.2** eliminates the last ``in`` operation and 
instead removes duplicates in an efficient type conversion 
line``permutations = list(dict.fromkeys(permutations))`` therefore
dropping one order of n from the time complexity but 
still retains a time complexity of **O(n!)**. 

**Version 0.3** was written because the above code still
would not execute for jumble length input of 20. Since factorials
blow up so quickly, for example 20! = 2.4x10^18, this version essentially caps the execution time to the length
of the word list, rather than the number of permutations on
the input. This is done by pre-compiling the word-list into a 
dictionary, keyed by the anagram of the word, sorted. Many thanks
to Raymonds answer [here](https://stackoverflow.com/questions/20510084/python-algorithm-jumble-solver#comment30661251_20510084)

Combinations still need to be generated however, which has 
time complexity of **O(n choose r)**, which by [definition](https://en.wikipedia.org/wiki/Combination#:~:text=Combinations%20refer%20to%20the%20combination,with%20repetition%20are%20often%20used.), 
is better than O(n!) due to the factorial in the denominator.

## Results
| Jumble     | n  | v0.1      | v0.2      | v0.3               |               |           |
|------------|----|-----------|-----------|--------------------|---------------|-----------|
|            |    | total [s] | total [s] | pre-processing [s] | execution [s] | total [s] |
| dog        | 3  | 0.000035  | 0.000038  | 0.574487           | 0.000076      | 0.574563  |
| cake       | 4  | 0.000113  | 0.000117  | 0.568251           | 0.000079      | 0.568330  |
| create     | 5  | 0.013637  | 0.001580  | 0.573747           | 0.000180      | 0.573927  |
| formula    | 7  | 1.094946  | 0.011275  | 0.550776           | 0.000292      | 0.551068  |
| waterway   | 8  | 4.757625  | 0.076176  | 0.566327           | 0.000515      | 0.566842  |
| formulate  | 9  |           | 0.943021  | 0.565326           | 0.001112      | 0.566438  |
| dictionary | 10 |           | 9.709259  | 0.562932           | 0.001889      | 0.564821  |


![img.png](img.png)