from read_database import readCostumesDatabase
from update_database import updateCostumeDatabase
from bill_handler import get_bill_details_for_selected_Costumes
from bill_file_creator import create_rent_bill

newData = readCostumesDatabase()

def get_user_selected_quantities(data, selected_costume_indexes):
    selected_costume_quantities = []
    for i in range(len(selected_costume_indexes)):
        valid = True
        while valid:
            try:
                get_current_costume_quantity = int(input(f"What quantity of {newData[selected_costume_indexes[i]][0]} would you like to rent? "))
                if get_current_costume_quantity > int(newData[selected_costume_indexes[i]][3]):
                    print("Sorry, we don't have that many costumes in stock.")
                    print()
                    continue
                elif get_current_costume_quantity < 1:
                    print("Please enter a positive value for quantitiy.")
                    print()
                    continue
                else:
                    selected_costume_quantities.append(get_current_costume_quantity)
                    newData[selected_costume_indexes[i]][3] = str(int(newData[selected_costume_indexes[i]][3]) - get_current_costume_quantity)
                    valid = False
            except ValueError:
                print("Invalid choice")
                print()
                continue

    return selected_costume_quantities

def get_user_selected_costumes(data):
    selected_costume_indexes = []

    valid = True
    while valid:
        try:
            cloth_option = int(input("Which cloth would you like to rent? (1-6): "))
            if cloth_option < 1 or cloth_option > 6:
                print("Invalid choice")
                print()
                continue
            elif int(data[cloth_option-1][3]) == 0:
                print("Sorry, the costume is currently out of stock")
                print()
                continue
            if cloth_option >= 1 and cloth_option <= 6:
                selected_costume_indexes.append(cloth_option-1)
                get_another_costume = True
                while get_another_costume:
                    confirmation = input("Do you want to rent another costume? (y/n) : ").lower()
                    if confirmation == "y":
                        valid = True
                        get_another_costume = False
                    elif confirmation == "n":
                        valid = False
                        get_another_costume = False
                    else:
                        print("Invalid choice")
                        print()
                        continue
        except ValueError:
            print("Invalid choice")
            print()
            continue
    return selected_costume_indexes

def show_costumes():
    data = readCostumesDatabase()
    costumesAvailable = ""
    for i in range(len(data)):
        if int(data[i][3]) <= 0:
            endValue = "Out Of Stock\n"
        else:
            endValue = data[i][3]
        costumesAvailable += f"{i+1}. {data[i][0]}, Price: {(data[i][2]).strip()}, {endValue}"
    return costumesAvailable

def rent_costume():
    data = readCostumesDatabase()
    print("""
  _____  ______ _   _ _______    _____ ____   _____ _______ _    _ __  __ ______ 
 |  __ \|  ____| \ | |__   __|  / ____/ __ \ / ____|__   __| |  | |  \/  |  ____|
 | |__) | |__  |  \| |  | |    | |   | |  | | (___    | |  | |  | | \  / | |__   
 |  _  /|  __| | . ` |  | |    | |   | |  | |\___ \   | |  | |  | | |\/| |  __|  
 | | \ \| |____| |\  |  | |    | |___| |__| |____) |  | |  | |__| | |  | | |____ 
 |_|  \_\______|_| \_|  |_|     \_____\____/|_____/   |_|   \____/|_|  |_|______|
                                                                                                                                                           
    """)
    print(show_costumes())
    print()
    print()
    selected_costume_indexes = get_user_selected_costumes(data)
    print()
    selected_costume_qantities = get_user_selected_quantities(data, selected_costume_indexes)
    print()
    bill_details_for_selected_Costumes = get_bill_details_for_selected_Costumes(data, selected_costume_indexes, selected_costume_qantities)
    completion_status = create_rent_bill(bill_details_for_selected_Costumes)
    if completion_status:
        updateCostumeDatabase(newData)
        print("Bill created successfully")
    else:
        print("Sorry, Bill creation failed, please try again with different name and phone number\nor adding an extra character to the name or phone number")
        input("Press enter to try again!")
        rent_costume()
    print()
    return_to_main_validity = True
    while return_to_main_validity:
        return_to_main_menu = input("Do you want to return to the main menu? (y/n) ").lower()
        if return_to_main_menu == "y":
            from main import main
            main()
        elif return_to_main_menu == "n":
            quit()
