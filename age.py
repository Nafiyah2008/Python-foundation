try:
    age = int(input("Enter the age:"))
    if age % 2 == 0 :
     print("Age is even")
    else:
     print("Age is odd")
except ValueError :
         print("The age is not valid")
