films = {
    "A":[3,5],
    "B":[18,2],
    "C":[15,5],
    "D":[12,5]
    }

while True:

    choice = input("Which film would you like to see?:").strip().title()

    if choice in films:
        age = int(input("how old are you?:").strip())

        if age >= films[choice][0]:
            

            if films[choice][1] >0:
             print("Enjoy the movie")
             films[choice][1] = films[choice][1]-1
            else:
             print("sorry we are sold out")

        else:
            print("You are too young to see that film")
    else:
        print("Film not available")
