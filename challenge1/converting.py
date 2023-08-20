# Convert a 12-hour clock system to 24-hour clock-system
# make a clock format (hh: mm  AM or PM) as input in 12 hour clock system
#  output in 24-hour clock system
hour = int(input("Enter the hour(1-12): "))
minute = int(input("Enter minute(0-59): "))
period = input(input("Enter period(am or pm): "))

def convert(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour ==12:
        hour = 0
    return f"{hour:02d}:{minute:02d}"
result = convert(hour, minute, period)
print(result)

