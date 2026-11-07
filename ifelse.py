# a = 12
# b = 76

# if b > a:
#     print("b is greater than a")

# x=2
# y=7

# if y > x:
#     print("y is greater than x")
# f=78
# if f > 0:
#     print("the number is positive")
#     print('positive number')
#     print("the number is not negative")
# signed_out = True 
# if signed_out:
#     print("you are signed out")
#     x=99
#     y=99
#     if x>y:
#       print ("x is greater than y")
#     elif x==y:
#      print("x is equal to y")
# score=78
# if score >= 80:
#     print("Grade 1")
# elif score >= 70:
#    print('Grade 2')
# elif score >= 60:
#    print('Grade 3')

# day = 3
# if day == 1:
#   print("Monday")
# elif day == 2:
#   print("Tuesday")
# elif day == 3:
#   print("Wednesday")
# elif day == 4:
#   print("Thursday")
# elif day == 5:
#   print("Friday")
# elif day == 6:
#   print("Saturday")
# elif day == 7:
#   print("Sunday")

# x=5
# y=56
# if x>y:
#      print("x is greater than y")
# elif x==y:
#      print("x is equal to y")
# else:
#        print("x is less than y") 

# if x>y:
#      print("x is greater than y")
# else:
#    print("x is less than y")

# temperature = 22
# if temperature > 30:
#   print("It's hot outside!")
# elif temperature > 20:
#   print("It's warm outside")
# elif temperature > 10:
#   print("It's cool outside")
# else:
#   print("It's cold outside!")

# username="Matthew"
# if len(username)>0:
#    print(f"Welcome, {username}!")
# else:
#   print("Error 234: Username cannot be empty")


# Login or Signup
# an array of names
names = ["Matthew", "John"]
active = True
while (active):
    print("Attendance: ", names)
    print("--------------------------")

    name = input("Enter your name: ")
    if name == "c":
        print(f'Total Attendance is: {len(names)}')
        print("Have a nice day\n")
        active = False
        continue
    if name in names:
        print(f"Welcome {name}. Your name is in the List")

    else:
        print(f"Sorry, {name} is not in the list. Please signup!")
        new_name = input("Please enter your name to signup: ")
        if new_name == "":
            print("You did not enter a name. Please try again")
        else:
            names.append(new_name)
            print(f"Welcome {new_name}. Your name has been added to the List")


#comment block
'''
Ask for username:
if username is not in list in database
show Signup Form
'''
'''elif username is in database then show password'''

"""if password is correct, then show Welcome page or homepage"""
'''Else if password is wrong, show Error message :Invalid Credentials, then logout'''
