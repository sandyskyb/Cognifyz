def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

# Test the function
print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
