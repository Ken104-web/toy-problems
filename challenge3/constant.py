def  get_constant_value(element):
    return ord(element) - ord("a") + 1

def high_constant_value(s):
    constant_value = []
    current_value = 0

    for element in s:
        if element in "aeiou":
            constant_value.append(current_value)
            current_value = 0
        else:
            current_value += get_constant_value(element)
    constant_value.append(current_value)
    return max(constant_value)

#  Assigning inputs
string = input("Enter a string in lowercase: ")
result = high_constant_value(string)
print(f"The highest value substring is: {result}")
