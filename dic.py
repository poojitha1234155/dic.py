def check_substring(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    for i in range(n1 - n2 + 1):
        match = True
        for j in range(n2):
            if s1[i + j] != s2[j]:
                match = False
                break
        if match:
            return f"Substring found at index {i}"
    return "Not a substring"

# Example
s1 = "helloworld"
s2 = "world"
print(check_substring(s1, s2))


def largest_word(s):
    max_len = 0
    max_word = ""
    current_word = ""

    for ch in s:
        if ch != " ":
            current_word += ch
        else:
            if len(current_word) > max_len:
                max_len = len(current_word)
                max_word = current_word
            current_word = ""
    
    # check last word
    if len(current_word) > max_len:
        max_word = current_word

    return max_word

# Example
s = "I love programming very much"
print(largest_word(s))

