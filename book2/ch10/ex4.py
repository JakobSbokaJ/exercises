book = 'guest_book.txt'

with open(book,'a') as file_object:
    while True:
        name = input("Enter your name to be added to the guest list (or \"done\" to quit): ")
        if name != "done":
            print(f"Hey there, {name}! Welcome to the party!")
            file_object.write(f"{name} will be coming to the party.\n")
        else:
            break

with open(book,'r') as file_object:
    lis = file_object.read()
    print(lis)