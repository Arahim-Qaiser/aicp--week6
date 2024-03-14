ADULT_PRICE_ONE_DAY = 20
ADULT_PRICE_TWO_DAYS = 30
CHILD_PRICE_ONE_DAY = 12
CHILD_PRICE_TWO_DAYS = 18
SENIOR_PRICE_ONE_DAY = 16
SENIOR_PRICE_TWO_DAYS = 24
FAMILY_PRICE_ONE_DAY = 60
FAMILY_PRICE_TWO_DAYS = 90
GROUP_PRICE_ONE_DAY = 15
GROUP_PRICE_TWO_DAYS = 22
LION_FEEDING_PRICE = 2
PENGUIN_FEEDING_PRICE = 2
EVENING_BBQ_PRICE = 5  
def display_ticket_options():
    print("\n** One-Day Tickets **")
    print("{:<25s}{:>20s}".format("Ticket type", "Cost"))
    print("{:<25s}{:>20s}".format("One Adult", "${:.2f}".format(ADULT_PRICE_ONE_DAY)))
    print("{:<25s}{:>20s}".format("One Child", "${:.2f}".format(CHILD_PRICE_ONE_DAY)))
    print("{:<25s}{:>20s}".format("One Senior", "${:.2f}".format(SENIOR_PRICE_ONE_DAY)))
    print("{:<25s}{:>20s}".format("Family Ticket", "${:.2f}".format(FAMILY_PRICE_ONE_DAY)))
    print("{:<25s}{:>20s}".format("Group of 6 (per person)", "${:.2f}".format(GROUP_PRICE_ONE_DAY)))
    
    print("\n** Two-Day Tickets **")
    print("{:<25s}{:>20s}".format("Ticket type", "Cost"))
    print("{:<25s}{:>20s}".format("One Adult", "${:.2f}".format(ADULT_PRICE_TWO_DAYS)))
    print("{:<25s}{:>20s}".format("One Child", "${:.2f}".format(CHILD_PRICE_TWO_DAYS)))
    print("{:<25s}{:>20s}".format("One Senior", "${:.2f}".format(SENIOR_PRICE_TWO_DAYS)))
    print("{:<25s}{:>20s}".format("Family Ticket", "${:.2f}".format(FAMILY_PRICE_TWO_DAYS)))
    print("{:<25s}{:>20s}".format("Group of 6 (per person)", "${:.2f}".format(GROUP_PRICE_TWO_DAYS)))
    
    print("\n** Extra Attractions (Optional) **")
    print("{:<25s}{:>20s}".format("Attraction", "Price"))
    print("{:<25s}{:>20s}".format("Lion Feeding", "${:.2f}".format(LION_FEEDING_PRICE)))
    print("{:<25s}{:>20s}".format("Penguin Feeding", "${:.2f}".format(PENGUIN_FEEDING_PRICE)))
    print("{:<25s}{:>20s}".format("Evening BBQ (With Two-Day Tickets Only)", "${:.2f}".format(EVENING_BBQ_PRICE)))



def process_booking():
    booking_number = 1000 
    total_cost = 0
    
    
    ticket_data = {
        "Adult": 0,
        "Child": 0,
        "Senior": 0,
        "Family": 0,
        "Group": 0
    }
    
   
    attraction_data = {
        "Lion Feeding": 0,
        "Penguin Feeding": 0,
        "Evening BBQ": 0
    }
    
    print("\n*** New Booking ***")
    
   
    for ticket_type in ticket_data.keys():
        if ticket_type == "Family":
            while True:
                try:
                    family_adults = int(input("Enter the number of adults in the family ticket: "))
                    family_children = int(input("Enter the number of children in the family ticket: "))
                    if family_adults < 0 or family_children < 0:
                        print("Ticket quantity cannot be negative.")
                        continue
                    ticket_data["Adult"] += family_adults
                    ticket_data["Child"] += family_children
                    ticket_data["Family"] += 1
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif ticket_type == "Group":
            while True:
                try:
                    group_size = int(input("Enter the size of the group: "))
                    if group_size < 6:
                        print("Group size must be 6 or more.")
                        continue
                    ticket_data["Group"] += group_size
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            while True:
                try:
                    quantity = int(input(f"Enter the number of {ticket_type} tickets: "))
                    if quantity < 0:
                        print("Ticket quantity cannot be negative.")
                        continue
                    ticket_data[ticket_type] += quantity
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
    

    while True:
        try:
            lion_feeding = int(input("Enter the number of Lion Feeding tickets: "))
            penguin_feeding = int(input("Enter the number of Penguin Feeding tickets: "))
            evening_bbq = int(input("Enter the number of Evening BBQ tickets: "))
            if lion_feeding < 0 or penguin_feeding < 0 or evening_bbq < 0:
                print("Attraction quantity cannot be negative.")
                continue
            attraction_data["Lion Feeding"] += lion_feeding
            attraction_data["Penguin Feeding"] += penguin_feeding
            attraction_data["Evening BBQ"] += evening_bbq
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
  
    for ticket_type, quantity in ticket_data.items():
        if ticket_type in ["Adult", "Child", "Senior", "Family", "Group"]:
            total_cost += quantity * (ADULT_PRICE_TWO_DAYS if quantity > 0 else 0)
    total_cost += lion_feeding * LION_FEEDING_PRICE
    total_cost += penguin_feeding * PENGUIN_FEEDING_PRICE
    if ticket_data["Adult"] > 0 or ticket_data["Senior"] > 0:
        total_cost += evening_bbq * EVENING_BBQ_PRICE
    
    # Check for better value options
    if ticket_data["Group"] >= 6 and (ticket_data["Group"] % 2 == 0 or ticket_data["Group"] % 3 == 0):
        group_size = ticket_data["Group"]
        num_families = group_size // 6 if group_size % 2 == 0 else group_size // 6 + 1
        num_remaining_people = group_size % 6 if group_size % 2 == 0 else group_size % 6 + 6
        family_cost = num_families * FAMILY_PRICE_TWO_DAYS
        remaining_cost = num_remaining_people * ADULT_PRICE_TWO_DAYS
        if family_cost + remaining_cost < total_cost:
            print("Choosing a combination of family tickets and individual tickets might be cheaper for your group.")
            print(f"Recommended combination: {num_families} family tickets ({family_cost} zł), "
                  f"{num_remaining_people} individual tickets ({remaining_cost} zł - total cost: {family_cost + remaining_cost} zł).")
    
   
    print("\n*** Booking Summary ***")
    for ticket_type, quantity in ticket_data.items():
        if quantity > 0:
            print(f"{quantity} {ticket_type} tickets")
    for attraction, quantity in attraction_data.items():
        if quantity > 0:
            print(f"{quantity} {attraction} tickets")
    print(f"Total cost: {total_cost} zł")
    
   
    booking_number += 1
    print(f"Your booking number is: {booking_number - 1}\n")


def main():
    display_ticket_options()
    
    while True:
        choice = input("Would you like to make a booking (y/n)? ").lower()
        if choice != 'y':
            break
        process_booking()

    print("Thank you for using the Wildlife Park booking system!")


if __name__ == "__main__":
    main()

