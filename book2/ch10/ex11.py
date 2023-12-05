import json
numList = []
numFile = 'numbers.json'

while True:
    num = input("Input one of your favorite numbers (q to quit): ")
    if num != "q":
        numList.append((num))
    else:
        break
        

with open(numFile, 'w') as file_obj:
    json.dump(numList, file_obj)