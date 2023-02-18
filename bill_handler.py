from date_time import get_current_date_time

curr_date, curr_time = get_current_date_time()

def get_rented_costume_indexes(name_of_customer, address_of_customer, phone_number_of_customer):
    file_name = f"borrow-{name_of_customer}--{phone_number_of_customer}--{address_of_customer}.txt"
    file = open(file_name, "r")
    data = file.readlines()
    file.close()
    line_with_indexes = data[1].split(":")
    line_with_indexes = line_with_indexes[1].split(",")

    return line_with_indexes

def get_rented_costume_quantities(name_of_customer, address_of_customer, phone_number_of_customer):
    file_name = f"borrow-{name_of_customer}--{phone_number_of_customer}--{address_of_customer}.txt"
    file = open(file_name, "r")
    data = file.readlines()
    file.close()
    line_with_indexes = data[2].split(":")
    line_with_indexes = line_with_indexes[1].split(",")

    return line_with_indexes

def get_rent_date(name_of_customer, address_of_customer, phone_number_of_customer):
    file_name = f"borrow-{name_of_customer}--{phone_number_of_customer}--{address_of_customer}.txt"
    file = open(file_name, "r")
    data = file.readlines()
    file.close()
    line_with_date = data[8].split(":")
    line_with_date = line_with_date[1].strip()
    return line_with_date

def get_customer_details():
    valid = True
    while valid:
        name_of_customer = input("What is your name? ").lower()
        address_of_customer = input("What is your address? ").lower()
        phone_number_of_customer = input("What is your phone number? ").lower()
        if (name_of_customer).strip() == "" or (address_of_customer).strip() == "" or (phone_number_of_customer).strip() == "":
            print("Please enter valid details.")
            continue
        else:
            return name_of_customer, address_of_customer, phone_number_of_customer

def get_bill_details_for_selected_Costumes(data, selected_costume_indexes, selected_costume_quantities):
    name_of_customer, address_of_customer, phone_number_of_customer = get_customer_details()
    IDs = ""
    QTYs = ""
    for i in range(len(selected_costume_indexes)):
        if i == len(selected_costume_indexes)-1:
            endValue = ""
        else:
            endValue = ","
        IDs += f"{selected_costume_indexes[i]}{endValue}"
        QTYs += f"{selected_costume_quantities[i]}{endValue}"

    rent_bill_structure = f"""
Selected Costume IDs: {IDs}
Selected Costume Quantities: {QTYs}
    +{"-" * 30}
    Customer name: {name_of_customer}
    Customer address: {address_of_customer}
    Customer phone number: {phone_number_of_customer}

    Rent date: {curr_date}
    Rent time: {curr_time}

    Rent details:
    +{"-" * 30}

    """

    grand_total = 0
    for i in range(len(selected_costume_indexes)):
        price_of_current_costume = float((data[selected_costume_indexes[i]][2]).replace("$", ""))
        total = price_of_current_costume * selected_costume_quantities[i]
        rent_bill_structure += f"""
        Name Of Costume: {data[selected_costume_indexes[i]][0]}
        Brand: {data[selected_costume_indexes[i]][1]}
        Price: {data[selected_costume_indexes[i]][2]}
        Quantity: {selected_costume_quantities[i]}
        Total: {total}


    +{"-" * 30}
        """
        grand_total += total
    
    rent_bill_structure += f"Grand Total: {grand_total}"
    
    return rent_bill_structure,name_of_customer, address_of_customer, phone_number_of_customer


def get_bill_details_for_return_Costumes(data, indexes, quantities, rentDate, name_of_customer, address_of_customer, phone_number_of_customer, fine_amount, days_rented):
    return_bill_structure = f"""
Rent date: {rentDate}
Return Date: {curr_date}
    +{"-" * 30}
    Customer name: {name_of_customer}
    Customer address: {address_of_customer}
    Customer phone number: {phone_number_of_customer}

    Rent days: {days_rented}
    Fine amount: {fine_amount}

    Rent details:
    +{"-" * 30}

    """

    for i in range(len(indexes)):
        return_bill_structure += f"""
        Name Of Costume: {data[int(indexes[i])][0]}
        Brand: {data[int(indexes[i])][1]}
        Price: {data[int(indexes[i])][2]}
        Quantity: {quantities[i]}

    +{"-" * 30}
        """
    
    
    return return_bill_structure, name_of_customer, address_of_customer, phone_number_of_customer