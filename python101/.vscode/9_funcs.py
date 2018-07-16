# BASIC IDEA OF FUNCTIONS and DOMAIN -> RANGE



# SQUARE


# ABS


# IS NEGATIVE



# IS EVEN NUMBER (HANDS ON)



# FACTORIAL EXTRA ASSIGNEMENT
import string
#x={string.ascii_lowercase}


def encode ():
    reslist = []
    alist = input("enter your text to be encoded")
    for i in alist:
        u = string.ascii_lowercase.index(i)
        reslist.append(u)
    print (reslist)
    return
def decode ():
    alist = input("enter your text to be decoded")
    reslist = []
    for i in alist:
        i = int(i)
        char = string.ascii_lowercase[i]
        reslist.append(char)
    result= ''.join(reslist)
    print(result)
    return
m = input("choose your request no. please \n 1: choose 1 for encode \n 2: choose 2 for decode \n")
if int(m) == 1:
        encode()
else:
        decode()

#
#encode(m)
#decode(m)