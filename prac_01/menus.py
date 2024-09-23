

name = input("Enter your name: ")
print(f"(H)ello\n(G)oodbye\n(Q)uit")
choice = input("Enter your choice: ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print(f"Invalid choice")
    print(f"(H)ello\n(G)oodbye\n(Q)uit")
    choice = input("Enter your choice: ").upper()
print(f"Finished.")