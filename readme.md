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
## Approach
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
its n!+(n-1)!+(n-2)!... 



## Results


