def show_bill(file_name):
    file = open(file_name,"r")
    print(file.read())
    file.close()

def create_rent_bill(bill_details_for_selected_Costumes):
    rent_bill_structure,name_of_customer, address_of_customer, phone_number_of_customer = bill_details_for_selected_Costumes

    rent_file_name = f"borrow-{name_of_customer}--{phone_number_of_customer}--{address_of_customer}.txt"
    try:
        rent_file = open(rent_file_name, "x")
        rent_file.write(rent_bill_structure)
        rent_file.close()
        show_bill(rent_file_name)
        return True
    except FileExistsError:
        return False

def create_return_bill(bill_details_for_return_Costumes):
    return_bill_structure, name_of_customer, address_of_customer, phone_number_of_customer = bill_details_for_return_Costumes

    return_file_name = f"return-{name_of_customer}--{phone_number_of_customer}--{address_of_customer}.txt"
    try:
        return_file = open(return_file_name, "x")
        return_file.write(return_bill_structure)
        return_file.close()
        show_bill(return_file_name)
        return True
    except FileExistsError:
        return False