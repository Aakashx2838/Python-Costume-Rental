from rent_costume_main import rent_costume
from return_costume_main import return_costume
from rent_costume_main import show_costumes

def main():
    print("""
  _____  ______ _   _ _______       _         _____ ______ _______      _______ _____ ______ 
 |  __ \|  ____| \ | |__   __|/\   | |       / ____|  ____|  __ \ \    / /_   _/ ____|  ____|
 | |__) | |__  |  \| |  | |  /  \  | |      | (___ | |__  | |__) \ \  / /  | || |    | |__   
 |  _  /|  __| | . ` |  | | / /\ \ | |       \___ \|  __| |  _  / \ \/ /   | || |    |  __|  
 | | \ \| |____| |\  |  | |/ ____ \| |____   ____) | |____| | \ \  \  /   _| || |____| |____ 
 |_|  \_\______|_| \_|  |_/_/    \_\______| |_____/|______|_|  \_\  \/   |_____\_____|______|                                                                   
                                                                                             
    """)
    print()
    print("1. Show available costumes")
    print("2. Rent a costume")
    print("3. Return a costume")
    print("4. Exit")
    print()

    valid = True
    while valid:
        try:
            choice = int(input("What would you like to do? (1,2,3,4): "))
            if choice == 1:
                print(show_costumes()) 
            elif choice == 2:
                valid = False
                rent_costume()
            elif choice == 3:
                valid = False
                return_costume()
            elif choice == 4:
                valid = False
                quit()
            else:
                print("Invalid choice")
                print()
                continue
            print()
        except ValueError:
            print("Invalid choice")
            print()
            continue

main()