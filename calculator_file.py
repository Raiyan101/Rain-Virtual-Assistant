def calculate(command):

    list_of_nums = [0,1,2,3,4,5,6,7,8,9, "-"]
    num1 = ""
    num2 = ""
    first_started = False
    first_done = False
    second_done = False
    second_started = False
    for b in command:
        if first_done == False:
            for x in list_of_nums:
                if b == str(x):
                    first_started = True
                    num1 = num1 + b

            if b == " " and first_started:
                first_done = True

        elif first_done and second_done != True:

            for x in list_of_nums:
                if b == str(x):
                    num2 = num2 + b
                    second_started = True

            if b == " " and second_started:
                second_done = True
    result = None
    if "multiply" in command or "x" in command or "multiplied" in command or "into" in command:
        result = float(num1) * float(num2)
    elif "divide" in command or "/" in command:
        result = float(num1) / float(num2)
    elif "add" in command or "+" in command or "plus":
        result = float(num1) + float(num2)
    elif "subtract" in command or "-" in command or "minus" in command:
        result = float(num1) - float(num2)
        
    return result