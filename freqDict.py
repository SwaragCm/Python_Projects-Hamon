def freq(string):
    dictionary = {}
    for i in string:                # iterates over each character in the string
        if i in dictionary:         # checks current character i is already a key in the dictionary.
            dictionary[i] += 1      # if it is their corresponding value is incremented by 1.
        else:
            dictionary[i] = 1       # if not their it sets the value 1
    print(dictionary)

if __name__ == "__main__":
    string = input("Enter a string: ")
    freq(string)


