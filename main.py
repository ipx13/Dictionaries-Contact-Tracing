def menu():
    print("\n===== Menu =====\n"
          "1 -> Add a profile"
          "2 -> Search for a profile"
          "3 -> Check database summary and statistics"
          "4 -> Exit")

print("\n===== Contact Tracing Program =====\n"
          "Welcome to my contact tracing program!")

while True:
    try:
        choice_mainmenu = int(input("What would you like to do?"))
    except:
        print("Please enter only an integer! Choose between choices 1-4.")
    else:
        if choice_mainmenu in [1, 2, 3, 4]:
            if choice_mainmenu == 1:
                print("gottem")
                break
            elif choice_mainmenu == 2:
                print("this is 2")
            elif choice_mainmenu == 3:
                print("this is 3")
            elif choice_mainmenu == 4:
                print("this is 4")
        else:
            print("Please choose among the choices. Enter an integer between 1-4.")
            continue
        break
