import sys
import time
from itertools import combinations


def load_words(filename):
    with open(filename) as word_file:
        valid_words = word_file.read().split()
    return valid_words


def build_table(word_list):
    table = {}
    for word in word_list:
        key = ''.join(sorted(word))
        table.setdefault(key, []).append(word)
    return table


def lookup(jumble_variant, table):
    key = ''.join(sorted(jumble_variant))
    return dict.fromkeys(table.get(key, []))


if __name__ == '__main__':

    start_time = time.time()

    try:
        language_table = build_table(load_words(sys.argv[1]))
        jumble = sys.argv[2]
    except:
        print('There was an error. The first argument should point to a word-list')
        print('file and the second should be a jumble of characters')
        print('Using default word list and "dog" as input')
        language_table = build_table(load_words('words_alpha.txt'))
        jumble = 'dog'

    loaded_time = time.time()

    # Create dict of permutations, use dict to prevent duplicates
    unique_combis = {jumble: None}
    for j in range(len(jumble), 1, -1):
        temp = combinations(jumble, j)
        for i in temp:
            unique_combis.setdefault(''.join(i), None)

    # Use lookup table to get matching anagrams for each permutation
    # Use a dict (set would also work) to prevent duplicates
    words = {}
    for combi in unique_combis:
        temp = lookup(combi, language_table)
        words.update(temp)

    total_time = time.time() - loaded_time
    load_time = loaded_time - start_time

    # Report
    for word in list(words.keys()):
        print(word)

    print('')
    print('Loading took', load_time, 'seconds')
    print('Finished in', total_time, 'seconds after initial loading and processing')
    print('')

