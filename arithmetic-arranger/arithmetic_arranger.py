def arithmetic_arranger(problems, optional=None):
    num1_list = []
    num2_list = []
    dashes_list = []
    sums_list = []

    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        if '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."
        num1, sign, num2 = problem.split(' ')
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if num1.isdigit() is False or num2.isdigit() is False:
            return "Error: Numbers must only contain digits."

        if '+' in problem:
            sums = int(num1) + int(num2)
        elif '-' in problem:
            sums = int(num1) - int(num2)

        line_len = 2 + max([len(num1), len(num2), (len(str(sums)) - 1)] if optional else [len(num1), len(num2)])

        num1 = " "*(line_len - len(num1)) + num1
        num2 = sign + " "*(line_len - len(num2) - 1) + num2
        dashes = "-" * line_len
        sums = " "*(line_len - len(str(sums))) + str(sums)

        num1_list.append(num1)
        num2_list.append(num2)
        dashes_list.append(dashes)
        sums_list.append(sums)

    line1 = "    ".join(num1_list)
    line2 = "    ".join(num2_list)
    line3 = "    ".join(dashes_list)
    line4 = "    ".join(sums_list)

    if optional:
        arranged_problems = "{}\n{}\n{}\n{}".format(line1, line2, line3, line4)
    elif optional is None:
        arranged_problems = "{}\n{}\n{}".format(line1, line2, line3)
    return arranged_problems
