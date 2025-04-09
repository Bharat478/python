

# # if else condition

# a = int(input("Enter any number:"))

# if (a>18):
#     print("Your age is more than 18")

# elif (a<0):
#     print("Don't Enter negative number")
# else :
#     print("Your age is less than 18")


# Problem 1 find greater number from entered by the user

a =int(input("Enter first Number :"))

b =int(input("Enter second Number :"))

c =int(input("Enter third Number :"))

d =int(input("Enter fourth Number :"))


if (a>b and a>c and a>d):
    print("first entered number is greater i.e",a)
elif(b>a and b>c and c>d):
    print("second entered number is greater i.e",b)
elif(c>d and c>b and c>d):
    print("third entered number is greater i.e",c)
elif(d>a and d>b and d>c):
    print("fourth entered number is greater i.e",d)


