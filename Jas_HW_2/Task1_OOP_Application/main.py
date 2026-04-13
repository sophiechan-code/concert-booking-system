import sys
from system.booking_system import BookingSystem


def test_data(system: BookingSystem):
    system.add_artist("BLACKPINK", "YG Entertainment")
    system.add_artist("BTS", "HYBE")
    system.add_artist("Terence Lam", "TLP")
    
    system.create_concert("BLACKPINK", "2024-12-25", "Seoul Olympic Stadium", max_tickets=2, price=2000.0)
    system.create_concert("BTS", "2024-11-20", "Wembley Stadium", max_tickets=50000, price=2050.0)
    system.create_concert("Terence Lam", "2025-08-19", "Hong Kong Hung Hum Stadium", max_tickets=30000, price=1888.0)

    system.add_fan("Terence", "terence@cls.com", is_vip=False)
    system.add_fan("Hins", "hins@test.com", is_vip=True, vip_level="Platinum")
    system.add_fan("Jas", "jas@test.com", is_vip=True, vip_level="Gold")


def main():
    print("=========================================")
    print("          Concert Booking System         ")
    print("=========================================")
    
    system = BookingSystem()
    test_data(system)
    
    while True:
        print("\n--- Main Menu ---")
        print("1. View All Concerts")
        print("2. View Concerts Sorted by Price")
        print("3. Register as Fan")
        print("4. Book a Ticket")
        print("5. View Waitlist / Priority Queue")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            system.view_all_concerts(sort_by_price=False)
            
        elif choice == '2':
            system.view_all_concerts(sort_by_price=True)
            
        elif choice == '3':
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            vip_choice = input("Are you a VIP? (y/n): ")
            
            if vip_choice.lower() == 'y':
                flag = False
                while not flag:
                    level_input = input("VIP Level (Gold/Platinum): ").strip()
                    temp = level_input.lower()

                    if temp in ["gold", "platinum"]:
                        level = temp.capitalize()
                        fan = system.add_fan(name, email, is_vip=True, vip_level=level)
                        flag = True
                    else:
                        print("Invalid VIP level. Please enter Gold or Platinum.")
            else:
                fan = system.add_fan(name, email, is_vip=False)
            print(f"Done! Welcome {fan.get_name()}")
            print(fan.display_info())
            
        elif choice == '4':
            print("\nAvailable Fans:")
            for i, f in enumerate(system.fans, 1):
                print(f"{i}. {f.display_info()}")
                
            fan_idx = int(input("Select Fan ID: ")) - 1
            if fan_idx < 0 or fan_idx >= len(system.fans):
                print("Invalid fan selection")
                continue
                
            print("\nAvailable Concerts: ")
            concerts = system.view_all_concerts()
            if not concerts:
                continue
                
            concert_idx = int(input("Select Concert ID: ")) - 1
            if concert_idx < 0 or concert_idx >= len(concerts):
                print("Invalid concert")
                continue
                
            fan_obj = system.fans[fan_idx]
            concert_obj = concerts[concert_idx]

            system.request_booking(fan_obj, concert_obj)
            
        elif choice == '5':
            print("\nQueue:")
            system.process_waitlist()
            
        elif choice == '6':
            print("Thank you for using the system!")
            sys.exit(0)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
