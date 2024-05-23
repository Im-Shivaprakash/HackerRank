#Leap Year using Loop

def is_leap(year):
    if year%4==0 and year!=2100:
        return True
    else:
        return False