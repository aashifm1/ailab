def vacuum(rooms):
    current = input("\nEnter starting room: ") 
    while 0 in rooms.values():
        print("\nCurrent position:", current)
        choice = int(input("\nWhat to do (1-clean/2-move): "))
        if choice == 1:
            if rooms[current] == 1:
                print("\nThe room is already clean.")
            else:
                rooms[current] = 1  # Corrected assignment
                print(f"\nRoom {current} is now cleaned.")
        elif choice == 2:
            shift = input("Which room to move to?: ")
            if shift in rooms:
                current = shift
            else:
                print("\nInvalid room. Try again.")
        else:
            print("\nInvalid choice. Try again.")
            
    print("\nAll rooms are cleaned.")

rooms = {'a': 1, 'b': 0, 'c': 1}
vacuum(rooms)
