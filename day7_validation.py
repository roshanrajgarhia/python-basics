ages=[]

while True:
    user_input= input("Enter the age (or type 'done')")
    if user_input.lower()=='done':
        if not ages:
            print ("Atleast one age is required. Try again!")
            continue
        break

    if not user_input.isdigit():
        print ("Enter a valid number as age.")
        continue

    age= int(user_input)

    if age <= 0 or age >= 120:
        print ("Age is out of range")
        continue
    
    ages.append(age)

    

print ("Valid ages: ",ages)

def analyze_ages(ages):
    minors=adults=seniors=0

    for x in ages:
        if x<18:
            minors +=1
        elif x<60:
            adults +=1
        else:
            seniors +=1
    
    total = len(ages)
    avg =sum(ages)/total

    if avg<18:
        print ("Mostly Minors")
    elif avg<60:
        print ("Mostly adults")
    else:
        print ("Mostly Seniors")
    

    return {
        "Minors":minors,
        "Adults":adults,
        "Seniors":seniors,
        "Total Valid Ages":total,
        "Average":avg
    }
result= analyze_ages(ages)
print (result)




        