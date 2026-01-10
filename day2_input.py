name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello,", name)
print("Your age is ", age)
print("You will be " , age+1, "years the next year")

if (age>=18):
    print("Can Vote")
else:
    print("You cannot vote")

if (age>=18 and age<=60):
    print("You fall in working group")
else:
    print("You do not fall in working group")
