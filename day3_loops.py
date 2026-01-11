# To print right angled triangle using stars
'''
rows = int(input("Enter the number of rows :"))

for i in range(1, rows+1):
    for j in range(i):
        print ("*", end= " ")
    print()
'''

# To print numbers using for loop
'''n= int(input("Enter a number: "))

for i in range(n+1):
    print(i)
'''


# Age Validation
'''while True:
    age= int(input("Enter your age: "))
    if age >= 1 and age <= 100:
        print("Valid age.")
    else:
        print("Invalid age. Please enter a valid age.")
'''

#Check voting eligibility
while True:
  a = int(input("enter your age: "))
  if a >= 18:
    print("You are eligible to vote.")
  else:
    print("You are not eligible to vote.")