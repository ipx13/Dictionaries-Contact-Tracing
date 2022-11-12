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
        else:
            print("Please choose among the choices. Enter an integer between 1-4.")
            continue
        break
