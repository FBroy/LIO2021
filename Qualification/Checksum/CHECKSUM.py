#This method changes all letters into numbers
def lettersToNumbers(code):
    letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    index = 0
    while index < len(code):
        if (code[index] in letters):
            code = code[:index] + str(letters.index(code[index])//2 + 10) + code[index+1:]
        index += 1
    return code


#This method moves the first 4 characters to the end of the code
def moveBeginning(code):
    beginning = code[0] + code[1] + code[2] + code[3]
    return code[4:] + beginning


#This method does all the checks for a given code
def runNormalCheck(code):
    #Check if the length is between 5 and 34 and if the checksum is between 2 and 98
    if not(5 <= len(code) <= 34 and\
         2 <= int(code[2] + code[3]) <= 98):
        return "NO"
    
    code = moveBeginning(code)
    code = lettersToNumbers(code)

    #Check if the length of the code is smaller than or equal to 66 and check if the remainder of the code by 97 is 1
    if not(len(code) <= 66 and\
         int(code)%97 == 1):
        return "NO"

    return "OK"
    

#This method brute-forces every possibility of the '?' and returns every valid code, or 'impossible' if none are found
def runBruteForceCheck(code):
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    validCodes = []
    #If the '?' is in the checksum, only try numbers
    if code[2] == '?' or code[3] == '?':
        for i in range(10):
            tmp = code
            tmp = tmp.replace('?', str(i))
            if runNormalCheck(tmp) == "OK":
                validCodes.append(tmp.upper())
    #Otherwise try letters and numbers
    else:
        for i in characters:
            tmp = code
            tmp = tmp.replace('?', i)
            if runNormalCheck(tmp) == "OK":
                validCodes.append(tmp.upper())
    
    #If no valid code was found, return 'impossible'
    if len(validCodes) == 0:
        return "impossible"
    #Otherwise return the valid codes
    return validCodes


#This method brute-forces every possibility for the checksum and return the code with the correct checksum
def getCorrectChecksum(code):
    for i in range(100):
        if i < 10:
            number = ['0', str(i)]
        else:
            number = [d for d in str(i)]
        
        tmp = code[:2] + number[0] + number[1] + code[4:]
        if runNormalCheck(tmp) == "OK":
            return tmp.upper()
    
    return "This should never happen"


#Start of the program
amount = int(input())
valid = []
for i in range(amount):
    code = input()
    code = code.replace(" ", "")
    #If there is a '?' in the code, brute force every single possibility and keep valid ones
    if '?' in code:
        output = runBruteForceCheck(code)
    #Otherwise run all checks for the given code
    else:
        output = runNormalCheck(code)

    #If the code is invalid, brute-force the checksum and return the correct code
    if output == "NO":
        valid.append(getCorrectChecksum(code))
    #Otherwise just add the output to the list
    else:
        valid.append(output)


#Print the output
for i in valid:
    if isinstance(i, list):
        for j in range(len(i)):
            if j == len(i)-1:
                print(i[j])
            else:
                print(i[j], end=' ')
    else:
        print(i)