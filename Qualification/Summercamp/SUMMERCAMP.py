amount = int(input())
names = []
for i in range(amount):
    names.append(input())

#Sort the names to have them all in order of their starting letters
names.sort()
organisedFor = []
count = 0
startingLetter = names[0][0]

#Loop through all the names and check if the starting letter changes or stays the same
for i in range(amount):
    #If the starting letter is the same, increment the count
    if (startingLetter == names[i][0]):
        count += 1
    #Otherwise update the stored startingLetter and set count to 1 (already once instance was met)
    else:
        startingLetter = names[i][0]
        count = 1

    #If there are 5 people (or more), add the letter to the list
    if count == 5:
        organisedFor.append(startingLetter)

#Output the results
print("Activities organised for: ", end='')
if (len(organisedFor) == 0):
    print("/")
else:
    for i in range(len(organisedFor)):
        if (i == len(organisedFor)-1):
            print(organisedFor[i])
        else:
            print(organisedFor[i], end='')
