def panagram(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"     # here we are initializing the alphabets to "alpha"
    for i in alpha:
        if i not in s.lower():               # "lower()" this will convert string to lowercase
            print("not panagram")
            break
    else:
        print("panagram")



if __name__=="__main__":
    phrase = str(input("Enter a phrase"))
    panagram(phrase)