c='thanks'
def  jass():
    print (c)
while(True):
    try:
        a=str(input("enter month  letter= "))
        if(a=="january"or a=="february" or a=="december"):
            print("winter")
        elif(a=="march"or a=="april" or a=="may"):
            print("spring")
        elif(a=="jun"or a=="jul" or a=="aug"):
            print("summer")
        elif(a=="sep"or a=="oct" or a=="nov"):
            print("autumn")     
    except :
        print("abe unde")
    finally:
        jass()
