# Importing necessary libraries
import mysql.connector as a
from tabulate import tabulate
from datetime import datetime, timedelta

# Establishing Connection
con = a.connect(host="localhost", user="root", password="1234", database="Stock")

if con.is_connected():
    print("Successfully connected.")
else:
    print("Something went wrong.")

c = con.cursor(buffered=True)

# Defining function to analyze the purchase data
# Function - 1
def analyze_purchase_data(choice=None, start_date=None, end_date=None):
    if choice:
        if choice == '1':  # Day
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date + timedelta(days=1)
            print("If purchase is of more than 10,000 Rs then sales should be at least of 5,000 Rs.")
        elif choice == '2':  # Week
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=datetime.now().weekday())
            end_date = start_date + timedelta(days=7)
            print("If purchase is of more than 1,00,000 Rs then sales should be at least of 75,000 Rs.")
        elif choice == '3':  # Month
            start_date = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            next_month = datetime.now().replace(day=28) + timedelta(days=4)  # Adding 4 days to handle month-end cases
            end_date = next_month - timedelta(days=next_month.day)
            print("If purchase is of more than 1,75,000 Rs then sales should be at least of 1,50,000 Rs.")
        elif choice == '4':  # Year
            start_date = datetime.now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            end_date = datetime.now().replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
            print("If purchase is of more than 15,00,000 Rs then sales should be at least of 17,00,000 Rs.")
        elif choice == '5':  # Range
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            print("If purchase is in a particular season then check sales and purchase as well as bill and stock data and make descision accordingly.")
    else:
        start_date = None
        end_date = None

    sql = "SELECT * FROM purchase"
    if start_date and end_date:
        sql += " WHERE purchase_date BETWEEN %s AND %s"
        c.execute(sql, (start_date, end_date))
    else:
        c.execute(sql)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Purchase ID','Product ID', 'Product Name', 'Category', 'Per Unit Price', 'Quantity', 'Total Price', 'Purchase Date'], tablefmt='psql'))
    print("=" * 150)
    main()

# Defining function to analyze the sales data
# Function - 2
def analyze_sales_data(choice=None, start_date=None, end_date=None):
    if choice:
        if choice == '1':  # Day
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date + timedelta(days=1)
            print("If sale is less than 5,000 Rs. then focus more on prospecting.")
        elif choice == '2':  # Week
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=datetime.now().weekday())
            end_date = start_date + timedelta(days=7)
            print("If sale is less than 35,000 Rs. - 50,000 Rs. then build a new strategy to sale goods.")
        elif choice == '3':  # Month
            start_date = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            next_month = datetime.now().replace(day=28) + timedelta(days=4)  # Adding 4 days to handle month-end cases
            end_date = next_month - timedelta(days=next_month.day)
            print("If sale is less than 1,50,000 Rs. - 1,75,000 Rs. then create ads and promote products to increase sales.")
        elif choice == '4':  # Year
            start_date = datetime.now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            end_date = datetime.now().replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
            print("If sale is less than 18,25,000 Rs. - 20,00,000 Rs. doing well also focus on savings for the store.")
        elif choice == '5':  # Range
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            print("Observe season wise sale and do business accordingly. Also, check daily and month wise sales.")
    else:
        start_date = None
        end_date = None

    sql = "SELECT * FROM sales"
    if start_date and end_date:
        sql += " WHERE sales_date BETWEEN %s AND %s"
        c.execute(sql, (start_date, end_date))
    else:
        c.execute(sql)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Sales ID','Product ID', 'Product Name', 'Category', 'Per Unit Price', 'Quantity', 'Total Price', 'Sales Date'], tablefmt='psql'))
    print("=" * 150)
    main()

# Defining function to analyze the bill data
# Function - 3
def analyze_bill_data(choice=None, start_date=None, end_date=None):
    if choice:
        if choice == '1':  # Day
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date + timedelta(days=1)
            print("Match it with today's sales data. And, go through the stock data.")
        elif choice == '2':  # Week
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=datetime.now().weekday())
            end_date = start_date + timedelta(days=7)
            print("Match it with week's sales data. And, go through the stock data.")
        elif choice == '3':  # Month
            start_date = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            next_month = datetime.now().replace(day=28) + timedelta(days=4)  # Adding 4 days to handle month-end cases
            end_date = next_month - timedelta(days=next_month.day)
            print("Match it with month's sales data. And, go through the stock data.")
        elif choice == '4':  # Year
            start_date = datetime.now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            end_date = datetime.now().replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
            print("Match it with year's sales data. And, go through the stock data.")
        elif choice == '5':  # Range
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            print("Match it accrodingly with sales data and also go through stock data.")
    else:
        start_date = None
        end_date = None

    sql = "SELECT * FROM bill"
    if start_date and end_date:
        sql += " WHERE bill_date BETWEEN %s AND %s"
        c.execute(sql, (start_date, end_date))
    else:
        c.execute(sql)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Bill ID', 'Total Bill', 'Bill Date'], tablefmt='psql'))
    print("=" * 150)
    main()

# Function to go back to home
# Function - 4
def back_to_main_menu():
    import module4
    module4.main()

# Defining function to call other functions
def main():
    print("                                                              *******Tasks*******                                                               ")
    print("        1. Analyse Purchase Data      2. Analyse Sales Data       3. Analyse Bill Data      4. Back to Home")
    print("-" * 150)
    choice = input("Enter the task no. :- ")
    if choice == '1':
        time_frame = input("Enter time frame (1: Day, 2: Week, 3: Month, 4: Year, 5: Between given range of Dates): ")
        analyze_purchase_data(time_frame)
    elif choice == '2':
        time_frame = input("Enter time frame (1: Day, 2: Week, 3: Month, 4: Year, 5: Between given range of Dates): ")
        analyze_sales_data(time_frame)
    elif choice == '3':
        time_frame = input("Enter time frame (1: Day, 2: Week, 3: Month, 4: Year, 5: Between given range of Dates): ")
        analyze_bill_data(time_frame)
    elif choice == '4':
        back_to_main_menu()
    else:
        print("_" * 150)
        print("                                                                     Wrong Choice                                                          ")
        print("                                                                      Try Again                                                            ")
        print("-" * 150)
        main()

