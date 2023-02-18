import datetime
def get_current_date_time():
    now = datetime.datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")
    return current_date, current_time
