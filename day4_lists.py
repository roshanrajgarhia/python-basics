age =[18,24,46,12,45,23,76,45,87,9,25]
'''
minor= 0
adult=0
senior=0
for x in age:
    if x<18:
        print("Minor")
        minor += 1
    elif x>=18 and x<60:
        print("Adult")
        adult += 1
    else:
        print("Senior")
        senior += 1


print("Minors: ", minor)
print("Adult: ", adult)
print("Senior: ", senior)
'''
a=0
b=0
for x in age:
    if x%2==0:
        a=a+1
        
    else:
        b=b+1
        
print("even ages: ",a)
print("odd ages: ",b)