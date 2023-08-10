# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
# const
CREDS = Credentials.from_service_account_file("creds.json")
# const
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# const
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# const
SHEET = GSPREAD_CLIENT.open("love-sandwiches")

def get_sales_data():
    ''' Get sales figures from input'''

    while True:
        print("Please enter sales data from the last market")
        print("Data should be six numbers, separated by a comma")
        print("Example: 10,20,30,40,50,60 \n")
        data_str = input("Please enter sales data: \n")
        
        sales_data = data_str.split(",")
        if validate_data(sales_data):

            print(f"Data is valid")
            break
    
    return sales_data
        
def validate_data(values):
    """Inside the try, converts all string values to int, raises value error if cannot be done or if input != 6 values"""
    
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")
    
    except ValueError as e:
        print(f"invalid data: {e} please try again. \n")
        return False
    
    return True

# def update_sales_worksheet(data):
#     """update sales worksheet, new row with list data provided"""
#     print("updating sales worksheet....")
#     sales_worksheet = SHEET.worksheet("sales")
#     sales_worksheet.append_row(data)
#     print("sales Worksheet updated successfully \n")
    
def update_worksheet(data, sheet):

    print(f"updating {sheet.capitalize()}")
    worksheet_to_update = SHEET.worksheet(sheet)
    worksheet_to_update.append_row(data)
    print(f"{sheet.capitalize()} updated successfully")
    
def calculate_surplus_data(sales_row):
    """Calculates if there was surplus
    - Positive surplus indicates was
    - Negative indicates sold out"""
    
    print(f"Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    stock_row = [int(i) for i in stock_row]
    surplus_data= []
    for stocks, sales in zip(stock_row, sales_row):
        surplus = stocks - sales
        surplus_data.append(surplus)
    return surplus_data

# def add_surplus_data_to_worksheet(data):
#     """Adds surplus data to worksheet in a new row"""
#     surplus_sheet = SHEET.worksheet("surplus")
#     surplus_sheet.append_row(data)

def get_last_5_sales():
    sales = SHEET.worksheet("sales")
    columns_array = []
    for ind in range(1,7):
        column = sales.col_values(ind)
        columns_array.append(column[-5:])
    
    return columns_array

def calc_stock_data(data):
    """Calculates average of last 5 sales"""
    print("Calculating stock data... \n")
    new_stock_data = []
    for columns in data:
        int_column = [int(num) for num in columns]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        stock_num = round(stock_num)
        new_stock_data.append(stock_num)
    return new_stock_data
def main():
    """Runs all program functions"""
    data = get_sales_data()
    sales_data = [int(number) for number in data]
    # update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    # add_surplus_data_to_worksheet(new_surplus_data)
    update_worksheet(sales_data, "sales")
    update_worksheet(new_surplus_data, "surplus")
    get_last_5_sales()
    sales_columns = get_last_5_sales()
    stock_data = calc_stock_data(sales_columns)
    update_worksheet(stock_data, "stock")
    
print("Welcome...")
main()