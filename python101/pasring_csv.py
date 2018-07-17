import sys, os
import csv

filename = input("please enter your file name: ")
if os.path.isfile(filename) and os.path.exists(filename):
    x= open(filename,"r")
    file = csv.DictReader(x)
    array=[]
    for line in file:
        # import ipdb; ipdb.set_trace()
        x = (line['age'])
        array.append(int(x))
        array.sort()
    result= array[-1]
print("oldest one is: "+str(result))

