# Hi



def myReadFile(name):
    try:
        myFile = open(name)

    except(Exception):
        #raise (IOError)
        print(" Error no file !")

# if __name__ == __main__:

try:
    myReadFile('my.txt')
    #raise NameError('HiThere')
except(IOError):
    pass

try:
    while True:
        pass
except(KeyboardInterrupt):
    print("    Error While")