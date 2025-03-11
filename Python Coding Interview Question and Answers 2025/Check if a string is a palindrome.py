def is_palindrome(s):
    s = '' .join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

string = "A man, a plan, a canal: Panama"

print(is_palindrome(string))