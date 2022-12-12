

fru=['banana','orange','mango','lemon']
print(fru)

a=input("any modify in list")
if (a in fru):
    print("The item is already in the list")
else:
   fru.append(a)
   print(fru)
for i in range(0,len(fru)):
    fru[i]=fru[i].upper()
print(fru)
