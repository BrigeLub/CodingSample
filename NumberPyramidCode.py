#Purpose: Number Pyramid
#Author: Brigitte Lubker
#Date: 5/13/2020

i=1
#testing conditions
while True:
    try:
        num = int(input("Enter the number of lines (1 - 9): "))
        if num >= 1 and num <= 9:
            break
        else:
            print("Error: you must enter a value between 1 and 9. Try again.")
            continue
    
    except:
        print ("Invalid input. A integer value was expected. Try again.")
        continue

#conditions all good- first makes space for pyramid 
#then prints backwards (r to l)
#then forwards (l to r)
if num>0 and num<=9:
    print("\n")
    for i in range(1,num+1):
        for i2 in range(1,num-i+1):
            print(end=" ")
        for i2 in range(i,0,-1):
            print("{0}".format(i2),end="")
        for i2 in range(2,i+1):
            print("{0}".format(i2),end="")
        print()