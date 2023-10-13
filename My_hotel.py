hotel = {
    '1': {
        '185': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}
#Function to display guests..
def display_guests():
    print("Current Guests")
    for floor, rooms in hotel.items():
        for room, guests in rooms.items():
            print(f"Floor: {floor}, Room # {room}: {', '.join(guests)} ")



#check-in function.. if statement that says ..if room is full then make input null.
# room_in_use = False
# while room_in_use 

def check_in():

    # after check-in , check for room being occupied..
    floor = input("Floor: ")
    room = input("Room Number: ")
    
    if hotel[floor][room]:
      print("Room occupped")
      return
    else:
         guests = int(input("How many guests?: "))
         names = []
    for ppl in range(guests):
        name = input(f"Name of guest {ppl+1}: ")
        names.append(name)
    hotel[floor][room] = names
    print("Welcome to our hotel.")

#check-out function.. also make it tell user if wrong floor or room entered.
def check_out():
    floor = input("Floor: ")
    room = input("Room Number: ")
    if floor in hotel and room in hotel[floor]:
        del hotel[floor][room]
        print("Check-out complete, hope you enjoyed your visit!")
    else:
        print("Wrong floor or room number!")


#main function to handle if check in or check out happens and show how many guests.
#need an if statement..
def main():
    print("Hi , what would you like to do today?")
    print("1. Check-in?")
    print("2. Check-out?")
    print("3. Nothing.")
    print("> ", end ="")
    user_input = input()
    if user_input == "1":
       #User checks-in
       check_in()
       display_guests()
    elif user_input == "2":
        check_out()
        display_guests()
        #User check-out
    elif user_input == "3":
        print("Goodbye")
        pass
    else:
        print("Invalid input")

main()

    