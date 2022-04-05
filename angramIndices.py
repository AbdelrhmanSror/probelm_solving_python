# given a word w and string s , find all indices in s which are the starting locations of anagrams of w
# e.g. given w is ab and s is abxaba return [0,3,4]


# naive solution would take o(s*w) time
def anagram_indices(w, s):
    # sum of unicode of the word
    sum_of_word = sum([ord(char) for char in w])
    result = []
    for i in range(len(s)):
        if sum_of_word == sum([ord(char) for char in s[i:i + len(w)]]):
            result.append(i)
    return result


# optimized solution that takes o(s) time
def anagram_indices_optimized(w, s):
    # variable to keep track of the start of word
    current_start_index = 0
    # current length of newly constructed word
    current_word_count = 0
    # current sum of unicode of chars of the newly constructed word
    current_word_sum = 0
    # sum of unicode of the word given to compare
    sum_of_word = sum([ord(char) for char in w])
    result = []
    for i in range(len(s)):
        current_word_count += 1
        current_word_sum += ord(s[i])
        if current_word_count == len(w):
            if current_word_sum == sum_of_word:
                result.append(current_start_index)
            current_word_count -= 1
            current_word_sum -= ord(s[current_start_index])
            current_start_index += 1
    return result


if __name__ == '__main__':
    print(anagram_indices_optimized("ab", "abxaba"))
