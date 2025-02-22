# find the longest word

def longest_word(sentence:str)->str:
    words = sentence.split()
    temp_dict = {}
    for word in words:
        print(word)
        temp_dict[len(word)] = word
    return temp_dict[max(temp_dict.keys())]



def longest_word1(word_completer: str) -> str:
    words = word_completer.split()
    max_length = max(len(word) for word in words)
    return max(words, key=len)
print(longest_word1("The quick brown fox jumps over the lazy dog"))


def reverse_word(word: str) ->str:
    return word[::-1]

print(reverse_word("hello"))

def is_palindrome(word: str) -> bool:
    return word == word[::-1]

print(is_palindrome("racecar"))

def replace_word(sentence: str,word: str, new_word:str) -> str:
    return  sentence.replace(word,new_word)

print(replace_word("The quick brown fox jumps over the lazy dog", "quick", "slow"))
print(replace_word("The quick brown fox jumps over the lazy dog", "quick", "slow"))
print(replace_word("The quick brown fox jumps over the lazy dog", "quick", "slow"))
