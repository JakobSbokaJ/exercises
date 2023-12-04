alice = 'alice.txt'
gatsby = 'gatsby.txt'
scarlet = 'scarlet.txt'

def theAppearances(file):
    try:
        with open(file) as f_obj:
            contents = f_obj.read()
            contents = str(contents)
    except FileNotFoundError:
        print(f"Sorry, {file} does not exist.")
    else:
        print(f"The word \"the\" appears {contents.lower().count('the')} times in {file}")

theAppearances(alice)
theAppearances(gatsby)
theAppearances(scarlet)