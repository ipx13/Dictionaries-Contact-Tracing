def menu():
    print("\n===== Menu =====\n"
          "1 -> Add a profile\n"
          "2 -> Search for a profile\n"
          "3 -> Exit")

main_dict = {}

print("\n===== Contact Tracing Program =====\n"
          "Welcome to my contact tracing program!")

while True:
    menu()
    try:
        choice_mainmenu = int(input("\nWhat would you like to do? "))
    except:
        print("Please enter only an integer! Choose between choices 1-3.")
    else:
        if choice_mainmenu in [1, 2, 3]:
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

                print("\nPlease enter your vaccination status.")
                while True:
                    vaccination = input("Are you fully vaccinated? (Y or N): ")
                    if vaccination in ["Y", "N"]:
                        break
                    else:
                        print("Please enter only either Y or N.")
                        continue

                temp_dict = {"{}".format(name): {
                                "name" : name,
                                "age": age,
                                "address": address,
                                "number": number,
                                "vaccination": vaccination
                }}

                main_dict.update(temp_dict)

            elif choice_mainmenu == 2:
                print("\n===== Search in Dictionary =====")
                name_search = input("Full name: ")
                for i in main_dict:
                    if name_search == i:
                        print("\nMatch found!\n")
                        print("Name:", main_dict[i]["name"])
                        print("Age:", main_dict[i]["age"])
                        print("Address:", main_dict[i]["address"])
                        print("Phone Number:", main_dict[i]["number"])
                        print("Vaccination Status:", main_dict[i]["number"])

            elif choice_mainmenu == 3:
                print("Thank you for using this program!")
                break
            continue
        else:
            print("Please choose among the choices. Enter an integer between 1-3.")
            continue
    break