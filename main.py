# https://en.wikipedia.org/wiki/Jumble_algorithm


import sys, time


def load_words(filename):
    with open(filename) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':

    try:
        language = load_words(sys.argv[1])
        jumble = sys.argv[2]
    except:
        print('There was an error. The first argument should point to a word-list')
        print('file and the second should be a jumble of characters')
        print('Using default word list and "dog" as input')
        language = load_words('words_alpha.txt')
        jumble = 'dog'

    start_time = time.time()

    # Create list of permutations
    perms = []
    temp = []

    for j in range(0, len(jumble)):

        # Add the next letter in the jumble to each position of each existing permutation
        for perm in perms:  # len(jumble):num_permutations - 1:1, 2:4, 3:15, 4:64, 5:325, 6:1956, 7:13699
            for p in range(0, len(perm) + 1):
                temp.append(perm[:p] + jumble[j] + perm[p:])

        temp.append(jumble[j])

        for new_perm in temp:
            if new_perm not in perms:
                perms.append(new_perm)

        temp = []

    # print('all permutations:', perms)
    # print('# perms = ', len(perms))

    # Check all permutations against list of valid words, and add valid words to a final list
    words = []

    for perm in perms:
        if perm in language:
            words.append(perm)

    total_time = time.time() - start_time

    print('valid words: ', words)

    print('time: ', total_time)
