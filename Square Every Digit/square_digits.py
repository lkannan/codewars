def square_digits(num):
    num_str = str(num)
    return int(''.join(str(int(digit)**2) for digit in num_str))