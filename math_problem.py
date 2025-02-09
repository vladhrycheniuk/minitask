def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    operators = list(map(lambda x: x.split()[1], problems))
    if not all(op in ['+', '-'] for op in operators):
        return "Error: Operator must be '+' or '-'."

    numbers = []
    for i in problems:
        num = i.split()
        numbers.extend([num[0], num[2]])

    if not all(x.isdigit() for x in numbers):
        return 'Error: Numbers must only contain digits.'

    if any(len(x) > 4 for x in numbers):
        return 'Error: Numbers cannot be more than four digits.'

    upper_row = ''
    lower_row = ''
    solutions = ''
    
    val = list(map(lambda x: eval(x), problems))

    dashes = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2

        upper_row += numbers[i].rjust(space_width)
        lower_row += operators[i // 2] + numbers[i + 1].rjust(space_width - 1)
        dashes += '-' * space_width
        solutions += str(val[i // 2]).rjust(space_width)

        if i != len(numbers) - 2:
            upper_row += ' ' * 4
            lower_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    if show_answers:
        return '\n'.join((upper_row, lower_row, dashes, solutions))
    return '\n'.join((upper_row, lower_row, dashes))

# test
#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
