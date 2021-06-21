minutes = 0
hours = 0

print("hi, let's get productive! 🌼")
howlong = str(input("how long do you want to work for? if you want to enter your time in hours, type 'h'. if you want to type your value in minutes, type 'm' "))
if (howlong == "h" or howlong == "H"):
    hours = int(input("enter the amount of hours you'd like to work for "))
elif (howlong == "m" or howlong == "M"):
    minutes = int(input("enter the amount of minutes you'd like to work for "))
else:
    print("please restart. next time please enter either 'h' or 'm' ")

hours_to_min = hours*60
min_to_hours = minutes/60

if (howlong == "h"):
    print("okay so you'd like to work for", hours_to_min, "minutes")
    print("let's calculate how many breaks you'll get!")
elif (howlong == "m"):
    print("okay so you'd like to work for approxiatmately", min_to_hours, "hours")
    print("let's calculate how many breaks you'll get!")

cycles = 0

if (howlong == "h"):
    cycles = hours_to_min//30
    work_time = cycles*25
    break_time = cycles*5
    sum = work_time + break_time
    remainder = hours_to_min - sum
    print("you'll get", cycles, "cycles with", work_time, "minutes of work time and", break_time, "minutes of break time")
    print("one cycle means one work session (25 minutes) and one break session (5 minutes)")
    if (remainder != 0):
        print("you'll also get a remainder of", remainder)