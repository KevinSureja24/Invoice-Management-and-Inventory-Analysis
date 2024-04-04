# Defining functions to call all the modules
# Function to call functionalities from module1
def use_module1():
    import module1
    print("Using Module 1 Functionalities:")
    module1.main()  # Call main function from module1
    main()

# Function to call functionalities from module2
def use_module2():
    import module2
    print("Using Module 2 Functionalities:")
    module2.main()  # Call main function from module2
    main()

# Function to call functionalities from module3
def use_module3():
    import module3
    print("Using Module 3 Functionalities:")
    module3.main()  # Call main function from module3
    main()

# Defining function to exit
def ending_program():
    exit()

# Main function to interact with user
def main():
    while True:
        print("Choose Module to Use:")
        print("1. Module 1 (Inventory Management)")
        print("2. Module 2 (Billing Logic)")
        print("3. Module 3 (Analysis)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            use_module1()
        elif choice == '2':
            use_module2()
        elif choice == '3':
            use_module3()
        elif choice == '4':
            ending_program()
        else:
            print("Invalid choice. Please try again.")

# def pswd():
#     p = input("Password: ")
#     if p == "DEV":
#         print("_" * 150)
#         main()
#     else:
#         print("Wrong Password")
#         print("=*" * 75)
#         pswd()
# pswd()

main()