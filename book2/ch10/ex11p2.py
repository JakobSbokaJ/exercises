numFile = 'numbers.json'

try:
    with open(numFile, 'r') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f"{numFile} does not exist.")
else:
    print(f"I know your favorite numbers! They are {contents}")