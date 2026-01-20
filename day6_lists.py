'''def count_even_odd(numbers):
    even=0
    odd=0

    for num in numbers:
        if num%2==0:
            even +=1
        else:
            odd +=1
    
    return {
        "Even ":even,
        "Odd ":odd
    }

numbers=[12,13,14,15,23,35,46,57,68,69]
result= count_even_odd(numbers)
print (result)
'''

def count_age_groups(ages):
    x=0
    y=0
    z=0

    for age in ages:
        if age<18:
            x +=1
        elif age<60:
            y +=1
        else:
            z +=1
    
    return{
        "Minors ":x,
        "Adults ":y,
        "Seniors ":z
    }

def average_age(ages):
    avg= sum(ages)/len(ages)
    return{
        "Average Age ":avg
    }

def analyze_age(ages):

    return{
        "Groups ":count_age_groups(ages),
        "Average ":average_age(ages)
    }

ages=[12,13,14,15,23,35,46,57,68,69,76,34,98,25]
result= analyze_age(ages)
print (result)

        