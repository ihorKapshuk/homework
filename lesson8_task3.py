def make_operation(operator, *args):
    return_value = 0
    for i in range(len(args)):
        if operator == "+":
            return_value += args[i]
        elif operator == "-":
            if i == 0:
                return_value = args[i]
            else:
                return_value -= args[i]
        elif operator == "*":
            if i == 0:
                return_value = args[i]
            else:
                return_value *= args[i]
        else:
            break
    return return_value
print(make_operation("+", 7, 7, 2))
print(make_operation("-", 5, 5, -10, -20))
print(make_operation("*", 7, 6))