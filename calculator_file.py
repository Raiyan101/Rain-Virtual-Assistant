def calculate(command):
    if "hey" in command:
        command = command.replace("hey", "")
    result = None
    try:
        try:
            if "x" in command:
                command = command.replace("x", "")
            elif "multiply" in command:
                command = command.replace("multiply", "")
            elif "multiplied" in command:
                command = command.replace("multiplied", "")
            
            if "what" in command:
                command = command.replace("what", "")

            if "is" in command:
                command = command.replace("is", "")

            if "by" in command:
                command = command.replace("by", "")
            elif "to" in command:
                command = command.replace("to", "")
            elif "with" in command:
                command = command.replace("with", "")
            elif "into" in command:
                command = command.replace("into", "")

            command = command.replace(" ", ";")
            new_command = ""
            for x in range(len(command)):
                if x != 0:
                    new_command += command[x]
            
            new_command += ";"
            list_of_numbers = []
            word = ""
            for n in new_command:
                if n != ";":
                    word += n
                elif n == ";":
                    list_of_numbers.append(word)
                    word = ""

            int1 = None
            int2 = None
            for number in list_of_numbers:
                if number != "" and int1 == None:
                    int1 = float(number)
                elif number != "" and int2 == None:
                    int2 = float(number)
            result = int1 * int2
            if result != None:
                return result

        except:
            pass

        try:
            #command = command.replace("add", "")

            if "what" in command:
                command = command.replace("what", "")
            if "is" in command:
                command = command.replace("is", "")

            if "added" in command:
                command = command.replace("added", "")

            if "add" in command:
                command = command.replace("add", "")

            if "into" in command:
                command = command.replace("into", "")

            if "in" in command:
                command = command.replace("in", "")
            elif "plus" in command:
                command = command.replace("plus", "")
            elif "+" in command:
                command = command.replace("+", "")
            elif "to" in command:
                command = command.replace("to", "")
            elif "by" in command:
                command = command.replace("by", "")
            
            command = command.replace(" ", ";")
            new_command = ""
            for x in range(len(command)):
                if x != 0:
                    new_command += command[x]
            
            new_command += ";"
            list_of_numbers = []
            word = ""
            for n in new_command:
                if n != ";":
                    word += n
                elif n == ";":
                    list_of_numbers.append(word)
                    word = ""

            int1 = None
            int2 = None
            for number in list_of_numbers:
                if number != "" and int1 == None:
                    int1 = float(number)
                elif number != "" and int2 == None:
                    int2 = float(number)
            result = int1 + int2
            if result != None:
                return result

        except:
            pass

        try:

            if "subtracted" in command:
                command = command.replace("subtracted", "")

            if "subtract" in command:
                command = command.replace("subtract", "")
        
            if "what" in command:
                command = command.replace("what", "")
            if "is" in command:
                command = command.replace("is", "")

            if "from" in command:
                command = command.replace("from", "")
            elif "by" in command:
                command = command.replace("by", "")
            elif "minus" in command:
                command = command.replace("minus", "")
            elif "-" in command:
                command = command.replace("-", "")

            command = command.replace(" ", ";")
            new_command = ""
            for x in range(len(command)):
                if x != 0:
                    new_command += command[x]
            
            new_command += ";"
            list_of_numbers = []
            word = ""
            for n in new_command:
                if n != ";":
                    word += n
                elif n == ";":
                    list_of_numbers.append(word)
                    word = ""

            int1 = None
            int2 = None
            for number in list_of_numbers:
                if number != "" and int1 == None:
                    int1 = float(number)
                elif number != "" and int2 == None:
                    int2 = float(number)

            result = int2 - int1
            if result != None:
                return result

        except:
            pass

        try:
            if "divided" in command:
                command = command.replace("divided", "")
            elif "divide" in command:
                command = command.replace("divide", "")
            elif "/" in command:
                command = command.replace("/", "")

            if "what" in command:
                command = command.replace("what", "")

            if "by" in command:
                command = command.replace("by", "")
            elif "to" in command:
                command = command.replace("to", "")
            elif "from" in command:
                command = command.replace("from", "")

            if "is" in command:
                command = command.replace("is", "")
            command = command.replace(" ", ";")
            new_command = ""
            for x in range(len(command)):
                if x != 0:
                    new_command += command[x]
            
            new_command += ";"
            list_of_numbers = []
            word = ""
            for n in new_command:
                if n != ";":
                    word += n
                elif n == ";":
                    list_of_numbers.append(word)
                    word = ""

            int1 = None
            int2 = None
            for number in list_of_numbers:
                if number != "" and int1 == None:
                    int1 = float(number)
                elif number != "" and int2 == None:
                    int2 = float(number)
            result = int1 / int2
            if result != None:
                return result
        
        except: 
            pass

        if result == None:
            pass

    except:
        pass
