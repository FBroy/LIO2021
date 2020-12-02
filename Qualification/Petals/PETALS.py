int(input())
letters = sorted(list(input()))

blue = letters.count("b")
red = letters.count("r")
white = letters.count("w")

#Find the minimum and the add the differences of the other 2 colors by the minimum ((c1-min) + (c2-min))
if (blue < red and blue < white):
    print(red-blue + white-blue)
elif (red < blue and red < white):
    print(blue-red + white-red)
else:
    print(blue-white + red-white)