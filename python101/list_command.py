import sys
import os
directory= sys.argv[1]
try:
    if os.path.isdir and os.path.exists(directory):
        for i in os.listdir(directory):
            print(i)
    else:
        print("this directory or file is not exist")
except:
    NotADirectoryError("this is not a directory")
