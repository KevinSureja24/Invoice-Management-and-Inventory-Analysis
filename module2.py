# Billing Logic
# Importing necessary libraries
import mysql.connector as a
import datetime
import decimal  # Import the decimal module
from tabulate import tabulate

# Establishing Connection
con = a.connect(host="localhost", user="root", password="1234", database="Stock")
if con.is_connected():
    print("Successfully connected.")
else:
    print("Something went wrong.")

c = con.cursor(buffered=True)

# Function to generate bill
# Function - 1
def generate_bill():
    total_bill = 0  # Initialize total bill
    while True:
        product_id = int(input("Enter product id (or type '0' to finish): "))
        if product_id == 0:
            break

        # Fetch product details from main table
        c.execute("SELECT * FROM main WHERE product_id = %s", (product_id,))
        product_data = c.fetchone()

        if product_data:
            product_name = product_data[1]
            category = product_data[2]
            per_unit_price = product_data[3]

            quantity = decimal.Decimal(input("Enter product quantity: "))  # Convert input to decimal.Decimal
            sales_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format

            total_price = per_unit_price * quantity
            total_bill += total_price  # Accumulate total price for each item

            # Update quantity and total price in main table
            updated_quantity = product_data[4] - quantity  # Subtract purchased quantity from existing quantity
            updated_total_price = product_data[5] - total_price  # Subtract purchased total price from existing total price
            c.execute("UPDATE main SET quantity = %s, total_price = %s WHERE product_id = %s", (updated_quantity, updated_total_price, product_id))
            con.commit()

            # Add entry to the sales table
            c.execute("INSERT INTO sales (product_id, product_name, category, per_unit_price, quantity, total_price, sales_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", (product_id, product_name, category, per_unit_price, quantity, total_price, sales_date))
            con.commit()

        else:
            print("Product not found. Please enter a valid product ID.")

    # Insert details into the bill table
    bill_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Current date in YYYY-MM-DD format
    c.execute("INSERT INTO bill (total_bill, bill_date) VALUES (%s, %s)", (total_bill, bill_date))
    con.commit()
    print("Billing completed.")
    print("Total Bill:", total_bill)
    main()  # Go back to the main menu or your desired flow

# Function to check sales
# Function - 2
def check_sales():
    sql = "SELECT * FROM sales"
    c.execute(sql)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Sales ID','Product ID', 'Product Name', 'Category', 'Per Unit Price', 'Quantity', 'Total Price', 'Sales Date'], tablefmt='psql'))
    print("=" * 150)
    main()

# Function to check bills
# Function - 3
def check_bill():
    sql = "SELECT * FROM bill"
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
    print("""
        1. Generate Bill      2. Check Sales      3. Check Bill      4. Back to Home
    """)
    print("-" * 150)
    choice = input("Enter the task no. :- ")
    if choice == '1':
        generate_bill()
    elif choice == '2':
        check_sales()
    elif choice == '3':
        check_bill()
    elif choice == '4':
        back_to_main_menu()
    else:
        print("_" * 150)
        print("                                                                     Wrong Choice                                                          ")
        print("                                                                      Try Again                                                            ")
        print("-" * 150)
        main()

