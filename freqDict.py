def freq(string):
    dictionary = {}
    for i in string:
        if i in dictionary:         
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    print(dictionary)

if __name__ == "__main__":
    string = input("Enter a string: ")
    freq(string)


