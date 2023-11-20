users = ["banana","brenana","brainana","admin","band asundertrail"]

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see today's status report?")
        else:
            print(f"Hello {user}, what would you like to do today?")
else:
    print("WE NEED USERS")