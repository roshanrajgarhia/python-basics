'''
CHALLENGE 1:    
while True:
    try:
        user_input=(input("Enter a number or type 'done' to exit: \n"))
        if user_input.lower()=='done':
          print ("Exiting the program...!!")
          break
        num1=int(user_input)
        num2=int(input("Enter another number: \n"))
        result=num1/num2
    
    except ValueError:
     print ("Enter a valid number")
    except ZeroDivisionError:
     print ("The second number could not be 0")
    else:
     print (f"Result: {result}")
    finally:
     print ("Program finished safely!!")
'''

#CHALLENGE 2
'''
myList=[]
while True:
    try:
      user_input=input("Enter the number or type 'done' to exit \n")

      if user_input.lower()=='done':
        if not myList:
           print ("The list could not be empty. Enter atleast one number.")
           continue
        break
      num=int(user_input)
      myList.append(num)
    except ValueError:
       print ("Invalid input. Please enter numbers only.")
    
total= len(myList)
sum_nums= sum(myList)
avg= sum_nums/total
print (myList)
print (f"The total number of numbers is {total}")
print (f"The sum of numbers is {sum_nums}")
print (f"The average of numbers is {avg:.2f}")
print (f"The maximum number is {max(myList)}")
print (f"The minimum number is {min(myList)}")
'''

#CHALLENGE 3

filename= input("Enter the name of the file: \n")

try:
   with open (filename, "r") as file:
      lines= file.readlines()

      if not lines:
         print ("File is empty")

      else:
         try:
          number= [int(line.strip()) for line in lines]

          total = len (number)
          total_sum= sum(number)
          avg= total_sum/total
          max_num= max(number)
          min_num= min(number)

          print (f"Total: {total}")
          print (f"Sum: {total_sum}")
          print (f"Avg: {avg}")
          print (f"Max: {max_num}")
          print (f"Min: {min_num}")

         except ValueError:
            print ("Incorrect value entered")
except FileNotFoundError:
   print ("File Not Found")      
   
         
     

         
    