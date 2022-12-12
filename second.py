c='thanks'
def  jass():
    print (c)
while(True):
    try:
        a=int(input("enter a= "))
        b=int(input("enter b= "))
        if(a>b):
            print(a,"is grester then ",b)
        elif(a<b):
            print(a,"is less then ",b)
        elif(a==b):
            print("both are same")    
        else:
            print("undifine")
    except :
        print("abe unde")
    finally:
        jass()
