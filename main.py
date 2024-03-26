stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
valid_notation = "-123456789.x10^"
Error_mess = "Error converting to scientific E notation."


# Type your code below

if "x10^" not in stdform:
    print(Error_mess)
else:
    mantissa, exponent = stdform.split("x10^")
    expo_new = exponent.lstrip("-")
    if stdform.count("x") != 1 or stdform.count("^") != 1 or stdform.count("-") > 1:
        print(Error_mess)
    if not mantissa.replace(".", "").replace("-","").isdigit():
        print(Error_mess)
    elif stdform.count(".") > 1:
        print(Error_mess)
    else:
        print(f"This number in E notation is {mantissa}E{exponent}.")
