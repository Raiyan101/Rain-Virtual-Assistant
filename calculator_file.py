def calculate(command):
    result = None
    try:
        try:
            command = command.replace("multiply", "")
            if "by" in command:
                command = command.replace("by", "")
            elif "to" in command:
                command = command.replace("to", "")
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
            command = command.replace("add", "")
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
            command = command.replace("subtract", "")
            if "from" in command:
                command = command.replace("from", "")
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

            result = int2 - int1
            if result != None:
                return result

        except:
            pass

        try:
            command = command.replace("divide", "")
            if "by" in command:
                command = command.replace("by", "")
            elif "to" in command:
                command = command.replace("to", "")
            elif "from" in command:
                command = command.replace("from", "")
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