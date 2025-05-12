# marks1 = int(input("Enter the number:"))
# marks2 = int(input("Enter the number:"))
# marks3 = int(input("Enter the number:"))

# total_percentage = (100)*(marks1+marks2+marks3)/300


# if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
#     print("You are passed")
# else:
#     print("You are failed")

# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("Enter your comment: ")

# if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This comment is spam")

# else:
#     print("This comment is not a spam")


# username = input("Enter Your Name: ")

# if(len(username)>10):
#     print("Your username contain more than 10 letters.", username)

# else:
#     print("Your letter doesn't contain more than 10 letters.", username)

# l = ["Harry", "Rohan", "Bharat", "Bhawan"]

# name = input("Enter Character:")

# if( name in l):
#     print("Enter Character present in list.")

# else:
#     print("Entered Character is not present in List.")

marks1 = int(input("Enter marks:"))
marks2 = int(input("Enter marks:"))
marks3 = int(input("Enter marks:"))


total_percentage = (100)*(marks1+marks2+marks3)/300

if(total_percentage>90):
    print("Divison A")
elif(total_percentage>80):
    print("Division B")
elif(total_percentage>70):
    print("Division C")
    
elif(total_percentage>60):
    print("Division D")

else:
    print("Failed")