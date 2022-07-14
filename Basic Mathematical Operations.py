def basic_op(operator, value1, value2):
    if operator == '+':
        return float(value1 + value2)
    elif operator == '-':
        return float(value1 - value2)
    elif operator == '*':
        return float(value1 * value2)
    elif operator == '/':
        return float(value1 / value2)
    else:
        print("Error")
