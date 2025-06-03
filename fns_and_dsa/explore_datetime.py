import datetime

def display_current_datetime():

    now = datetime.datetime.now()
    current_date = now.date()

    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(number_of_days):
    now = datetime.datetime.now()
    future_date = now + datetime.timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}") 

calculate_future_date(number_of_days)