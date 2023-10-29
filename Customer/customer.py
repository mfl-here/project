import csv


flag = False
def login(UID,PASS):
    global flag
    with open(r"C:\Users\Fathima\Desktop\coding\PROJECT+2\project\Customer\customer_login.csv","r") as fr:
        data = csv.reader(fr)
        while True:
            for i in data:
                if UID == i[0]:
                    if PASS ==i[1]:
                        flag = True
                        print("Login successfull")
                        break
            else:
                print("Invalid user id or password")
                flag = False
            if flag == True:
                break

def signup():
    global flag
    lc=uc=sp=d=ss=0
    with open (r"C:\Users\Fathima\Desktop\coding\PROJECT+2\project\Customer\customer_login.csv","a",newline="") as f:
        with open(r"C:\Users\Fathima\Desktop\coding\PROJECT+2\project\Customer\customer_login.csv","r") as fr:
            data = csv.reader(fr)
            w = csv.writer(f)
            l = []
            for i in data:
                l = i
                break
            #print(l)
            if "UserID" not in l:
                w.writerow(["UserID","Password"])                
            else:
                pass
            while True:
                uid = input("Enter User id:")
                for i in data:
                    if uid in i[0]:
                        print("UserID exist.Enter another id")
                        break
                else:
                    break
            while True:
                A = True
                pas =input("Enter Password:")
                for i in pas:
                    if i.isupper():
                       uc+=1
                    elif i.islower():
                        lc+=1
                    elif i.isdigit():
                        d+=1
                    elif i.isspace():
                        print("Password cannot contain space.Try again")
                        break
                    else:
                        sp+=1
                if pas == uid:
                    print("Password cannot be same as user id")
                elif len(pas)<8:
                    print("Password must atleast contain 8 character.")
                elif uc == 0:
                    print("Password must contain atleast 1 uppercase")
                elif lc == 0:
                    print("Password must contain atleast 1 lowercase")
                elif d ==0:
                    print("Password must contain atleast 1 digit")
                elif sp==0:
                    print("Password must contain a special character")
                else:
                    cpas = input("Confirm password:")
                    if pas != cpas:
                        print("Password not matching.Try again")
                    else:
                        w.writerow([uid,pas])
                        print("Account created")
                        flag = True
                        break
def cust_page():
    while True:
        if flag == False:
            print("**************************CUSTOMER**************************")
            print("i) Login    ii) Sign up    iii)Exit")
            opt = int(input("Enter Your Option :"))
            if opt == 1:
                user_id = input("Enter User ID :") #Fahad24@123
                password = input("Enter your password :")#Fahadxyz@123
                login(user_id,password)
            elif opt == 2:
                signup()
            elif opt == 3:
                break
            else:
                print("Invalid option")
            
            if flag == True:
                print("i) Search \nii)Filter search")
                search_opt = int(input("Enter the option :"))
                if search_opt == 1:
                    search_bar = input("Search here: ")
                    #dbms here
                elif search_opt == 2:
                    print("~~~~~~~PRICE RANGE~~~~~~~")
                    print("i) 5,000Rs - 10,000Rs \nii) 10,000Rs - 20,000Rs \niii) 20,000Rs - 30,000Rs \niv) 30,000Rs - 50,000Rs \nv) Above 50,000Rs")
                    price_opt = int(input("Enter an option :"))
                    print("~~~~~~~COMPANY~~~~~~~")
                    print("i)Apple \nii) Google \niii) Nothing \niv) One Plus \nv) Oppo \nvi) Samsung \nvii) Vivo \nviii) Xiaomi")
                    company_opt = int(input("Enter an option :"))
                    print("~~~~~~~OS~~~~~~~")
                    print("i)ios \nii)Android")
                    os_opt = int(input("Enter an option :"))
                    print("~~~~~~~NETWORK~~~~~~~")
                    print("i) 4G \nii) 5G")
                    network_opt = int(input("Enter an option :"))
                    print("~~~~~~~STORAGE~~~~~~~")
                    print("i) 16GB \nii) 32GB \niii) 64GB \niv)128GB \nv)256GB")
                    storage_opt = int(input("Enter an option :"))
                    print("~~~~~~~RAM~~~~~~~")
                    print("i) 4GB \nii) 6GB \niii) 8GB \niv) Above 8GB")
                    ram_opt = int(input("Enter an option :"))
                    print("~~~~~~~BATTERY~~~~~~~")
                    print("i) 3000mAh - 4000mAh \nii) 4000mAh - 5000mAh \niii) Above 5000mAh")
                    battery_opt = int(input("Enter an option :"))
                    print("~~~~~~~REAR CAMERA~~~~~~~")
                    print("i) Upto 12MP \nii) 12MP \niii) 16MP \niv) 20MP \nv)24MP \nvi) 30MP \nvi) Above 30MP ")#Depending on dbms
                    rear_opt = int(input("Enter an option :"))
                    print("~~~~~~~FRONT CAMERA~~~~~~~")
                    print("i)")#depending on dbms
                    front_opt = int(input("Enter an option :"))


