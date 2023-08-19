# Convert a 12-hour clock system to 24-hour clock-system
# make a clock format (hh: mm  AM or PM) as input in 12 hour clock system
#  output in 24-hour clock system
hour = 18
minute = 24
period = "PM"

def convert(hour, minute, period):
    if period == "PM":
        hour += 12
    hour %= 24
    return f"{hour:02d}:{minute:02d}"
result = convert(hour, minute, period)
print(result)

