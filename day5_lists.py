'''
ages=[18,27,36,34,14,25,67,18,46,76,25,18,19]

print (ages[0])
print (ages[-1])

mid=len(ages)//2

if mid%2==0:
    print (ages[mid-1 : mid+2])
else:
    print (ages[mid-2 : mid+1])

ages.sort()
print (ages)

n=ages.count(18)
print (n)

ages_copied= ages.copy()
print (ages_copied)

print (id(ages))
print (id(ages_copied))


'''


def analyze_ages(ages):
    minors=0
    adults=0
    seniors=0

    for x in ages:
        if x<18:
            minors +=1
        elif x<60:
            adults +=1
        else:
            seniors +=1
    return {
        "Minors ":minors,
        "Adults ":adults,
        "Seniors ":seniors
    }

ages=[18,27,36,34,14,25,67,18,46,76,25,18,19]
result=analyze_ages(ages)
print (result)

