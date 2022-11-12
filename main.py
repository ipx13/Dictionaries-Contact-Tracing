def menu():
    print("\n===== Menu =====\n"
          "1 -> Add a profile\n"
          "2 -> Search for a profile\n"
          "3 -> Check database summary and statistics\n"
          "4 -> Exit")

main_dict = {"name": "name", "info": "info"}
print(main_dict)

print("\n===== Contact Tracing Program =====\n"
          "Welcome to my contact tracing program!")

while True:
    menu()
    try:
        choice_mainmenu = int(input("\nWhat would you like to do? "))
    except:
        print("Please enter only an integer! Choose between choices 1-4.")
    else:
        if choice_mainmenu in [1, 2, 3, 4]:
            if choice_mainmenu == 1:
                print("\n===== Adding a profile =====\n\n"
                      "Please enter your full name (e.g.: Juan Delacruz).")
                name = input("Full name: ")
                print("\nPlease enter your age.")
                while True:
                    try:
                        age = int(input("Age: "))
                    except:
                        print("Please enter an integer for your age.\n")
                        continue
                    else:
                        if age >= 100:
                            print("\nOh my, aren't you too old to be going outside?")
                        elif age <= 2:
                            print("\nOh, so you're saying that you're just", age, "year/s old? Can you even read or write just yet?\n")
                            continue
                        break
                print("\nPlease enter your address.")
                address = input("Address: ")
                print("\nPlease enter your phone number.")
                while True:
                    try:
                        number = int(input("Phone number: "))
                    except:
                        print("Please enter only integers for your phone number.\n")
                    else:
                        break
                temp_dict = {
                    "name_{}".format(name): name,
                    "info_{}".format(name): {
                        "age": age,
                        "address": address,
                        "number": number
                    }
                }
                print(temp_dict)
                main_dict.update(temp_dict)
                print("main dict:", main_dict)

            elif choice_mainmenu == 2:
                name_search = input("Full name: ")

                matches_dict = {}
                counter = 0
                for i in main_dict:
                    if name_search == main_dict[i]:
                        matches_dict.update(i)
                        counter += 1
                if counter == 0:
                    print("no match found")

                '''for j in matches_dict:
                    for k in main_dict:
                        if k'''

            elif choice_mainmenu == 3:
                print("this is 3")
            elif choice_mainmenu == 4:
                print("this is 4")
            continue
        else:
            print("Please choose among the choices. Enter an integer between 1-4.")
            continue
    break