import requests
import json

def convert(command):

    command = command.replace("convert", "")
    command = command.replace(" ", ";")
    command += ";"
    stat = ""
    for b in range(len(command)):
        if b == 0:
            pass
        else:
            stat += command[b]
    list_of_words = []
    word = ""
    for x in stat:
        if x != ";":
            word += x
        elif x == ";":
            list_of_words.append(word)
            word = ""
    
    from_currency = list_of_words[1].upper()
    to_currency = list_of_words[3].upper()
    amount = list_of_words[0]

    curr = from_currency + "_" + to_currency
    url = f"https://free.currconv.com/api/v7/convert?q={curr}&compact=ultra&apiKey=9a5237a4882ccba9195f"
    response = json.loads(requests.get(url).text)
    result = int(amount) * int(response[curr])
    ret = f"{amount} {from_currency} are equal to {result} {to_currency}"
    return ret
