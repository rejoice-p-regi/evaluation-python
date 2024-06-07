#leap year
year=int(input("it is a postive number"))
if (year%4==0 and year%100!=0 or year%400==0):
    print("it is a leap year")
else:
    print(year,"is not a leap year")