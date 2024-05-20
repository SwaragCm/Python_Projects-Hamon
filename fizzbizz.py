def fizzbizz(n):
    for i in range(1,n+1):
        if i % 15 ==0:
            print("fizzbizz")
        elif i % 3 ==0:
            print("fizz")
        elif i % 5 ==0:
            print("bizz")
        else:
            print(i)


if __name__=="__main__":
    n=int(input("Enter a number"))
    fizzbizz(n)



# def fizzbizz(n):
#     for i in range(1,n+1):
#         if i % 3 ==0:
#             print("fizz")
#         elif i % 5 ==0:
#             print("bizz")
#         elif i % 15 ==0:
#             print("fizzbizz")
#         else:
#             print(i)


# if __name__=="__main__":
#     n=int(input("Enter a number"))
#     fizzbizz(n)
