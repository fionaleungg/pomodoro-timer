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
elif (howlong == "m"):
    print("okay so you'd like to work for approxiatmately", min_to_hours, "hours")

cycles = 0
time = 0

short_break = 0
if (howlong == "h"):
    time = hours_to_min
    while (time > 0):
        print("time to study!")
        time = time - 25
        print("time for a break!")
        time = time - 5
        short_break = short_break + 1
        if (short_break % 4 == 0):
            print("congrats! you've earned yourself a 30 minute break!")
            time = time - 30
elif (howlong == "m"):
    time = minutes
    while (time > 0):
        print("time to study!")
        time = time - 25
        print("time for a break!")
        time = time - 5
        short_break = short_break + 1
        if (short_break % 4 == 0):
            print("congrats! you've earned yourself a 30 minute break!")
            time = time - 30