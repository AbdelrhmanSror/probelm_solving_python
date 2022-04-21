# given a list of word ,find all pairs of unique indices such that the concatenation of the two word is a palindrome.
# e.g. list [code ,edoc ,da ,d] return (0,1) (1,0) ,(2,3)


def is_palindrome(word):
    return word == word[::-1]


# naive solution o(n*n) time
def palindrome(lst):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            if is_palindrome(lst[i] + lst[j]):
                result.append((i, j))
    return result


# naive solution o(n*c^2) time and n space
def palindrome2(lst):
    dic = {}
    result = []
    for i, words in enumerate(lst):
        dic[words] = i

    for i, word in enumerate(lst):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[char_i:]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if is_palindrome(prefix) and reversed_suffix in dic:
                if i != dic[reversed_suffix]:
                    result.append((i, dic[reversed_suffix]))

            if is_palindrome(suffix) and reversed_prefix in dic:
                if i != dic[reversed_prefix]:
                    result.append((i, dic[reversed_prefix]))
    return result


if __name__ == '__main__':
    print(palindrome(["code", "edoc", "da", "d"]))
    print(palindrome2(["code", "edoc", "da", "d"]))

