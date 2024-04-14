
#tabe baraye menu asli 
def print_menu():
    print("1. Show phone numbers")
    print("2. Add a phone number")
    print("3. Remove a phone number")
    print("4. Search a phone number")
    print("5. Quit")
    print()
    
numbers = {}
menu_choice = "0"
print_menu()

#gozine khuruj 5 has
#dar gheyre in surat edame barname
while menu_choice != "5":
    menu_choice = str(input("Choose an option (1-5): "))

    #namayeshe liste shomareha
    if menu_choice == "1":
        print("Phone numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()

    #ezafe kardane shomare
    elif menu_choice == "2":
        print("Adding a phone number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
        
        f = open("PhoneBook.txt", "a")
        mystring = ""
        for x in numbers:
            mystring = x +" " + numbers[x] + "\n"
        f.write(mystring)
        f.close()
        print("Phone number was successfully added")
        print()

    #hazf kardane shomare
    elif menu_choice == "3":
        print("Removing a phone number")
        name = input("Name: ")
        if name in numbers:
            with open("PhoneBook.txt", "r") as fp:
                lines = fp.readlines()

            with open("PhoneBook.txt", "w") as fp:
                for line in lines:
                    if line.strip("\n") != name + " " + numbers[name]:
                        fp.write(line)
            del numbers[name]
            print("Phone number was successfully removed")
        else:
            print(name, "was not found")
            print()

    #jostojuye shomare
    elif menu_choice == "4":
        print("Searching a phone number")
        name = input("Name: ")
        if name in numbers:
            print("Number: ", numbers[name])
            print()
        else:
            print(name, "was not found")
            print()       

    #edame barname   
    elif menu_choice != "5":
        print_menu()
