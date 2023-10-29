from Administrator import Admin
from Customer import customer as cust

while True:
    print("******************************<  >******************************")
    print("i) Login as Customer \nii) Login as Administrator")
    opt = int(input("Enter the option :"))
    if opt == 1:
        cust.cust_page()
    elif opt == 2:
        Admin.admin_page()
