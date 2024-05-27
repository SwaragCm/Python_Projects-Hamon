# def palindrome(s):
#     if s == s[::-1]:    # Here I'm using slicing to reverse my string and check whether that is equal to user input value
#         return True
#     else:
#         return False


# if __name__ == "__main__":
#     s = str(input("Enter a Word "))
#     print(palindrome(s))




# using loop
def palindrome(s):
    rev=""
    for i in s:
        rev = i+rev             # this will add the characters reversely
    if (rev == s):
        print ("Its a palindrome")
    else:
        print ("Not a palindrome")

if __name__ == '__main__':
    s = str(input("Enter a word: "))
    palindrome(s)