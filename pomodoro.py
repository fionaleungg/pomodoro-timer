minutes = 0
hours = 0
cycles = 0
time = 0
text = 0

#intro
print("hi, let's get productive! 🌼")
howlong = str(input("how long do you want to work for? if you want to enter your time in hours, type 'h'. if you want to type your value in minutes, type 'm' "))
if (howlong == "h" or howlong == "H"):
    hours = int(input("enter the amount of hours you'd like to work for "))
elif (howlong == "m" or howlong == "M"):
    minutes = int(input("enter the amount of minutes you'd like to work for "))
else:
    print("please restart. next time please enter either 'h' or 'm' ")

#conversion
hours_to_min = hours*60
min_to_hours = minutes/60   
        
if (howlong == "h"):
    print("okay so you'd like to work for", hours_to_min, "minutes")
elif (howlong == "m"):
    print("okay so you'd like to work for approxiatmately", min_to_hours, "hours")

def study(x):
    x = "time to study"
    print(x)

def shortbreak(x):
    x = "time for a break"
    print(x)

def longbreak(x):
    x = "congrats! you've earned yourself a 30 minute break!"
    print(x)

short_break = 0
if (howlong == "h"):
    time = hours_to_min
    while (time > 0):
        study(text)
        time = time - 25
        shortbreak(text)
        time = time - 5
        short_break = short_break + 1
        if (short_break % 4 == 0):
            longbreak(text)
            time = time - 30
elif (howlong == "m"):
    time = minutes
    while (time > 0):
        study(text)
        time = time - 25
        shortbreak(text)
        time = time - 5
        short_break = short_break + 1
        if (short_break % 4 == 0):
            longbreak(text)
            time = time - 30