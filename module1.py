# Inventory Management
# Importing necessary libraries
import mysql.connector as a
import datetime
from decimal import Decimal
from tabulate import tabulate


# Establishing Connection
con = a.connect(host="localhost", user="root", password="1234", database="Stock")
if con.is_connected():
    print("Successfully connected.")
else:
    print("Something went wrong.")

c = con.cursor(buffered=True)


# Function to check individual product
# Function - 1
def check_individual_product():
    product_name = input("Enter name of the product: ")
    sql = "SELECT * FROM main WHERE product_name = %s"
    data = (product_name,)
    c.execute(sql, data)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name', 'Category', 'Per Unit Price', 'Quantity', 'Total Price'], tablefmt='psql'))
    print("=" * 150)
    main()


# Function to check main stock
# Function - 2
def check_main():
    sql = "SELECT * FROM main"
    c.execute(sql)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name', 'Category', 'Per Unit Price', 'Quantity', 'Total Price'], tablefmt='psql'))
    print("=" * 150)
    main()


# Function to check grocery stock
# Function - 3
def check_grocery():
    sql = "SELECT * FROM main WHERE category = 'grocery'"
    c.execute(sql)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name', 'Category', 'Per Unit Price', 'Quantity', 'Total Price'], tablefmt='psql'))
    print("=" * 150)
    main()


# Function to check electronic stock
# Function - 4
def check_electronics():
    sql = "SELECT * FROM main WHERE category = 'electronic'"
    c.execute(sql)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name', 'Category', 'Per Unit Price', 'Quantity', 'Total Price'], tablefmt='psql'))
    print("=" * 150)
    main()


# Function to check apparels stock
# Function - 5
def check_apparels():
    sql = "SELECT * FROM main WHERE category = 'apparel'"
    c.execute(sql)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Product ID', 'Product Name', 'Category', 'Per Unit Price', 'Quantity', 'Total Price'], tablefmt='psql'))
    print("=" * 150)
    main()


# Function to add stock
# Function - 6
def add_in_purchase():
    product_name = input("Enter product name: ")
    category = input("Enter product category: ")
    per_unit_price = Decimal(input("Enter product per unit price: "))  # Convert to Decimal
    quantity = Decimal(input("Enter product quantity: "))  # Convert to Decimal
    total_price = per_unit_price * quantity
    purchase_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Check if the product already exists in the main table
    sql_check_existing = "SELECT * FROM main WHERE product_name = %s"
    data_check_existing = (product_name,)
    c.execute(sql_check_existing, data_check_existing)
    existing_product = c.fetchone()

    if existing_product:
        print("Product already exists.")
        update_choice = input("Do you want to update quantity (Q), per unit price (P), or both (B)? ").upper()
        if update_choice == "Q":
            new_quantity = Decimal(input("Enter the new quantity: "))
            updated_quantity = existing_product[4] + new_quantity  # Summing up the quantities
            updated_total_price = existing_product[5] + (new_quantity * per_unit_price)
            sql_update_main = "UPDATE main SET quantity = %s, total_price = %s WHERE product_name = %s"
            data_update_main = (updated_quantity, updated_total_price, product_name)
            c.execute(sql_update_main, data_update_main)
            
        elif update_choice == "P":
            new_per_unit_price = Decimal(input("Enter the new per unit price: "))
            updated_total_price = new_per_unit_price * existing_product[4]  # Recalculate total price based on new per unit price
            sql_update_main = "UPDATE main SET per_unit_price = %s, total_price = %s WHERE product_name = %s"
            data_update_main = (new_per_unit_price, updated_total_price, product_name)
            c.execute(sql_update_main, data_update_main)

        elif update_choice == "B":
            new_quantity = Decimal(input("Enter the new quantity: "))
            new_per_unit_price = Decimal(input("Enter the new per unit price: "))
            updated_total_price = new_quantity * new_per_unit_price
            sql_update_main = "UPDATE main SET quantity = %s, per_unit_price = %s, total_price = %s WHERE product_name = %s"
            data_update_main = (new_quantity, new_per_unit_price, updated_total_price, product_name)
            c.execute(sql_update_main, data_update_main)
        else:
            print("Invalid choice.")
            add_in_purchase()
    else:
        # If the product doesn't exist, insert it into the main table
        sql_insert_main = "INSERT INTO main (product_name, category, per_unit_price, quantity, total_price) VALUES (%s, %s, %s, %s, %s)"
        data_main = (product_name, category, per_unit_price, quantity, total_price)
        c.execute(sql_insert_main, data_main)

    # Insert into the purchase table with the obtained product_id
    product_id = existing_product[0] if existing_product else c.lastrowid
    sql_insert_purchase = "INSERT INTO purchase (product_id, product_name, category, per_unit_price, quantity, total_price, purchase_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data_purchase = (product_id, product_name, category, per_unit_price, quantity, total_price, purchase_date)
    c.execute(sql_insert_purchase, data_purchase)

    con.commit()
    print("Data Entered Successfully")
    print("-" * 25)
    main()


# Function to check purchase stock
# Function - 7
def check_purchase():
    sql = "SELECT * FROM purchase"
    c.execute(sql)
    myresult = c.fetchall()
    print(tabulate(myresult, headers=['Purchase ID', 'Product ID', 'Product Name', 'Category', 'Per Unit Price', 'Quantity', 'Total Price', 'Purchase Date'], tablefmt='psql'))
    print("=" * 150)
    main()


# Function to go back to home
# Function - 8
def back_to_main_menu():
    import module4
    module4.main()

# Main function to call above functionalities
def main():
    print("                                                              *******Tasks*******                                                               ")
    print("""
        1. Check Individual Stock      2. Check Main Stock            
        3. Check Grocery Stock         4. Check Electronics Stock     
        5. Check Apparels Stock        6. Add in Purchase Table             
        7. Check Purchases             8. Back to Home
    """)
    print("-" * 150)
    choice = input("Enter the task no. :- ")
    if choice == '1':
        check_individual_product()
    elif choice == '2':
        check_main()
    elif choice == '3':
        check_grocery()
    elif choice == '4':
        check_electronics()
    elif choice == '5':
        check_apparels()
    elif choice == '6':
        add_in_purchase()
    elif choice == '7':
        check_purchase()
    elif choice == '8':
        back_to_main_menu()
    else:
        print("_" * 150)
        print("                                                                     Wrong Choice                                                          ")
        print("                                                                      Try Again                                                            ")
        print("-" * 150)
        main()
