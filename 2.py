y=int(input("enter a year"))
if (y % 400 == 0):
    print("leap year")
elif( y % 100 ==0):
    print("not leap year")
elif(y % 4==0):
    print("leap year")
else:
    print("not a leap year")