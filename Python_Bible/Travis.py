known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Goergie","Hanna"]

print(len(known_users))


while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the list y/n?: ").lower()

        if remove =='y':
            known_users.remove(name)
            print(known_users)
    else:
        print("Hmm i don't think i have met you {}".format(name))
        add_me = input("Would you like to be added (y/n)?: ").lower()
        if add_me == "y":
            known_users.append(name)
            print(known_users)
            
            
