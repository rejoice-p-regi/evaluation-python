#prime number
n=int(input("it is a postive number : "))
if (n<1):
    print("is not a prime number")
elif(n==1):
    print("is not a prime number")
else:
    for i in range(2,n):
        if(n%i)==0:
            print(" not prime number ")
            #print(i,"times",n//i,"is",n)
            break
    else:
        print( "prime number ")