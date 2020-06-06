def str_to_int(input_str):
    t = 0
    power = len(input_str) - 1
    for digit in input_str:
        digitVal = ord(digit) - ord('0')
        t += digitVal * (10**power)
        power -= 1
    return t
print(str_to_int("1234"))