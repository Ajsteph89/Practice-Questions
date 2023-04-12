# write a program to determine if a year is a leap year
# A leap year is divisible by 4 but not 100 unless it is divisible by 400


def leap(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 400 == 0) and (year % 100 == 0):
        return True
    else:
        return False

print(leap(1996))