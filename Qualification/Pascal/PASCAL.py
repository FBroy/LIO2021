def fact(number):
    if number <= 1:
        return 1
    else:
        return number*fact(number-1)

n = input().split(" ")
n, p = int(n[0]), int(n[1])

numerator = fact(n)
denominator = fact(p)*fact(n-p)

print(int(numerator/denominator))