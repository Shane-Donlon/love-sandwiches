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
    print("Please enter sales data from the last market")
    print("Data should be six numbers, separated by a comma")
    print("Example: 10,20,30,40,50,60 \n")
    data_str = int(input("Please enter sales data"))
    
    
get_sales_data()