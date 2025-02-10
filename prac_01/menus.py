"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name:")
while name == "":
    print("Please enter your name")
    name = input("Enter name:")
print(MENU)
choice = input(">>>").lower()
while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
    elif choice == "g":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>>").lower()
print("Finished.")