# Complete the function that accepts a string parameter, # # and reverses each word in the string. All spaces in the # string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# +++ START YOUR IMPLEMENTATION


def reverse_word(word):
    word_len = len(word)
    word_list = list(word)

    for i in range(word_len // 2):
        tmp = word_list[i]
        word_list[i] = word_list[word_len - 1 - i]
        word_list[word_len - 1 - i] = tmp

    s = ""
    for c in word_list:
        s += c
    return s


def reverse_words(input):
    # split the words
    words = []
    word = ""
    space = ""
    for c in input:
        if c != " ":
            if space:
                words.append(space)
            space = ""
            word += c
        else:
            if word:
                words.append(word)
            word = ""
            space += " "
    if word:
        words.append(word)

    for i, word in enumerate(words):
        words[i] = reverse_word(word)

    s = ""
    for c in words:
        s += c
    return s


# reverse each word

# --- END YOUR IMPLEMENTATION

input = "This is an example!"
print(reverse_words(input))
input = "double  spaces"
print(reverse_words(input))

assert reverse_words("This is an example!") == "sihT si na !elpmaxe"
assert reverse_words("double  spaces") == "elbuod  secaps"
