'''
Created by Irish Paniza of BSC0E 2-2
Submitted to Engr. Danilo Madrigalejos for CMPE 30052
Date Submitted: 11/13/22
Description: This is a contact tracing program that utilizes dictionaries to store and manage data. The program asks for user's information that could be used to track them, which will then be added to the database. The user can also search for other people's information, given that they know their full name.
'''

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
                      "NOTE: This program could not contain duplicate names. Make sure that your full \nname is unique, or your information might get overwritten.")
                print("\nPlease enter your full name (e.g.: Juan Delacruz).")
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
                        print("Please enter only either Y or N.\n")
                        continue

                print("\nPlease enter your recent medical history.")
                while True:
                    history = input("Did you experience any symptoms like flu, colds, or fever in the last 14 days? (Y or N): ")
                    if history in ["Y", "N"]:
                        break
                    else:
                        print("Please enter only either Y or N.\n")
                        continue

                temp_dict = {"{}".format(name): {
                                "name" : name,
                                "age": age,
                                "address": address,
                                "number": number,
                                "vaccination": vaccination,
                                "history": history
                }}

                main_dict.update(temp_dict)
                print("\nSuccessfully added", name + "'s", "contact info to the database!")

            elif choice_mainmenu == 2:
                print("\n===== Search in Dictionary =====")
                name_search = input("Full name: ")
                for i in main_dict:
                    if name_search == i:
                        print("\nMatch found!\n")
                        print("Name:", main_dict[i]["name"])
                        print("Age:", main_dict[i]["age"])
                        print("Address:", main_dict[i]["address"])
                        print("Phone number:", main_dict[i]["number"])
                        print("Full vaccination status:", main_dict[i]["vaccination"])
                        print("Recently experienced flu-like symptoms:", main_dict[i]["history"])
                    else:
                        print("\nNo match found!")

            elif choice_mainmenu == 3:
                print("\nLoading...")
                print("\nThank you for using this program!")
                break
            continue
        else:
            print("Please choose among the choices. Enter an integer between 1-3.")
            continue
    break