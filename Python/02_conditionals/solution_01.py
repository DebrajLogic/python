year = 2012


if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('Leap year')
else:
    print("Not a leap year")

print(2016 % 400)
