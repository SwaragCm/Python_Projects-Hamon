import string

def panagram(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"  #here we are initializing the alphabets to "alpha" variable with the help of "string" which we import above
    print(alpha)
    for i in alpha:
        if i not in s.lower():          #this will convert string variable to lowercase
            print("not panagram")
            break
    else:
        print("panagram")



if __name__=="__main__":
    phrase=str(input("Enter a phrase"))
    panagram(phrase)