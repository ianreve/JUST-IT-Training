num = 5 # global variable 

def localSub():
    print("Printing from local sub", num )  # accesssing the global variable
localSub()

def modifyGlobalVar():
    # use of gglobal keyword to  modify the global variable 
    global num
    num = 10
    print("Printing from the local sub modified value", num) # modified global variable num

modifyGlobalVar()

localSub()