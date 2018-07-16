addressbook = {"samir": "01003295601", "peter": "01003333222"}


def addUser():
    x= input("please enter your name: ")
    y= input("please enter youe phone: ")
    addressbook[x] = y
    print('user added')


def delUser():
    x= input("please enter the name you want to delete: ")
    del addressbook[x]


def listUsers():
    print("here is the address book contents:\n")
    print(addressbook.keys(), addressbook.values())

def searchUser():
    x = input("pleas enter the user or phone you search about: ")
    if x in addressbook:
        print("your name is there: "+ x +": " +addressbook[x])
    else:
        print("your name is not there")

while True:
    z= int(input("please choose your operation number.\n1:add user\n2:delete user\n3:list users\n4:search for user\n"))
    if z == 1:
        addUser()
    elif z == 2:
        delUser()
    elif z == 3:
        listUsers()
    elif z == 4:
        searchUser()
    else:
        z = int(input("please choose your operation number.\n1:add user\n2:delete user\n3:list users\n4:search for user\n"))

