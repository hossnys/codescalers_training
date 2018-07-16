
x=input("please enter your password")
if x == "p@ssw0rd":
    print ("you are authorized")
else:
     for i in range(2):
        if x == "p@ssw0rd":
            print("you are authorized")
            exit()
        else:
            x=input("please enter your password correctly")

     print("access denied")
