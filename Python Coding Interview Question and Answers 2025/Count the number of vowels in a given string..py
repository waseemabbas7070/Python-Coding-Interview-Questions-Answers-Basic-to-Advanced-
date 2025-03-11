
def count_vowles(s):

    vowles = "aeiouAEIOU"

    return sum(1 for char in s if char in vowles)

string = "Hello,Ikram"

print(count_vowles(string))