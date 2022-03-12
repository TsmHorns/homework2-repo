val = input("Enter in your palindrome ->")

def palindrome(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]

variable = palindrome(val)
if variable:
    print(val + " is a palindrome")
else:
    print(val + " is not a palindrome")