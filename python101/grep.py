import sys
file= open(sys.argv[2],'r')
for line in file.readlines():
    if sys.argv[1] in line:
        print(line.strip())
