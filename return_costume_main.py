from bill_handler import get_customer_details, get_rented_costume_indexes, get_rented_costume_quantities, get_bill_details_for_return_Costumes, get_rent_date
from read_database import readCostumesDatabase
from update_database import updateCostumeDatabase
from bill_file_creator import create_return_bill
newData = readCostumesDatabase()

def find_user_rented_file(name_of_customer, address_of_customer, phone_number_of_customer):
    file_name = f"borrow-{name_of_customer}--{phone_number_of_customer}--{address_of_customer}.txt"
    try:
        file = open(file_name, "r")
        file.close()
        return True
    except FileNotFoundError:
        return False

def get_fine_amount():
    try:
        days_rented = int(input("How many days did you rent the costumes for? "))
        if days_rented < 0:
            print("Invalid input!")
            return get_fine_amount()
        elif days_rented <= 5:
            fine = 0
            return days_rented, fine
        elif days_rented > 5:
            fine = (days_rented - 5) * 7
            return days_rented, fine
    except ValueError:
        print("Invalid input!")
        return get_fine_amount()

def return_costume():
    data = readCostumesDatabase()
    print("""
  _____  ______ _______ _    _ _____  _   _    _____ ____   _____ _______ _    _ __  __ ______ 
 |  __ \|  ____|__   __| |  | |  __ \| \ | |  / ____/ __ \ / ____|__   __| |  | |  \/  |  ____|
 | |__) | |__     | |  | |  | | |__) |  \| | | |   | |  | | (___    | |  | |  | | \  / | |__   
 |  _  /|  __|    | |  | |  | |  _  /| . ` | | |   | |  | |\___ \   | |  | |  | | |\/| |  __|  
 | | \ \| |____   | |  | |__| | | \ \| |\  | | |___| |__| |____) |  | |  | |__| | |  | | |____ 
 |_|  \_\______|  |_|   \____/|_|  \_\_| \_|  \_____\____/|_____/   |_|   \____/|_|  |_|______|
                                                                                                                                                                                  
    """)
    print()
    print("Please enter the details of the customer who is returning the costumes, \nand make sure to enter exact details as used while renting the costumes.")
    print()
    valid = True
    while valid:
        name_of_customer, address_of_customer, phone_number_of_customer = get_customer_details()
        print()
        isPresent = find_user_rented_file(name_of_customer, address_of_customer, phone_number_of_customer)
        if isPresent:
            print("File found!")
            indexes = get_rented_costume_indexes(name_of_customer, address_of_customer, phone_number_of_customer)
            quantities = get_rented_costume_quantities(name_of_customer, address_of_customer, phone_number_of_customer)
            rent_date = get_rent_date(name_of_customer, address_of_customer, phone_number_of_customer)
            days_rented, fine_amount = get_fine_amount()
            for i in range(len(indexes)):
                newData[int(indexes[i])][3] = str(int(newData[int(indexes[i])][3]) + int(quantities[i]))

            bill_details_for_return_Costumes = get_bill_details_for_return_Costumes(data, indexes, quantities, rent_date, name_of_customer, address_of_customer, phone_number_of_customer, fine_amount, days_rented)
            input("Press enter to continue to return bill creation")
            completion_status = create_return_bill(bill_details_for_return_Costumes)
            if completion_status:
                print("Bill created successfully!")
                updateCostumeDatabase(newData)
                valid = False
            else:
                print("Costumes from that bill already returned!")
                return_costume()
        else:
            print("File not found!")
            print("Please make sure you have rented the costumes before returning them.")
            print()      
            continue
    return_to_main_validity = True
    while return_to_main_validity:
        return_to_main_menu = input("Do you want to return to the main menu? (y/n) ").lower()
        if return_to_main_menu == "y":
            from main import main
            main()
        elif return_to_main_menu == "n":
            quit()

