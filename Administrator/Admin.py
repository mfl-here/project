import csv

flag = False
def login(AID,PASS):
    global flag
    with open(r"C:\Users\Fathima\Desktop\coding\+2 Project\Administrator\admin_login.csv","r") as fr:
        data = csv.reader(fr)
        while True:
            for i in data:
                if AID == i[0]:
                    if PASS ==i[1]:
                        flag = True
                        break
            else:
                print("Invalid user id or password")
                flag = False
            if flag == True:
                break

def signup():
    global flag
    ad = input("Enter your admin ID :")
    ps = input("Enter password: ")
    login(ad,ps)
    if flag == True:
        lc=uc=sp=d=ss=0
        with open (r"C:\Users\Fathima\Desktop\coding\+2 Project\Administrator\admin_login.csv","a",newline="") as f:
            with open(r"C:\Users\Fathima\Desktop\coding\+2 Project\Administrator\admin_login.csv","r") as fr:
                data = csv.reader(fr)
                w = csv.writer(f)
                l = []
                for i in data:
                    l = i
                    break
                #print(l)
                if "Admin ID" not in l:
                    w.writerow(["Admin ID","Password"])                
                else:
                    pass
                while True:
                    aid = input("Enter Admin ID:")
                    for i in data:
                        if aid in i[0]:
                            print("ID exist.Enter another id")
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
                    if pas == aid:
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
                            w.writerow([aid,pas])
                            print("Account created")
                            flag = True
                            break
def Remove():
    ad = input("Enter your admin ID :")
    ps = input("Enter password: ")
    login(ad,ps)
    if flag == True:
         with open (r"C:\Users\Fathima\Desktop\coding\+2 Project\admin_login.csv","a",newline="") as f:
            with open(r"C:\Users\Fathima\Desktop\coding\+2 Project\admin_login.csv","r") as fr:
                data = csv.reader(fr)
                delete_id = input("Enter the Admin id to be removed :")
                #need to complete

def admin_page():
    while True:
        if flag == False:
            print("*******************LOGIN PAGE*******************")
            print("i)Login \nii)Add new admin \niii)Remove Admin \niv)Exit")
            opt = int(input("Enter an option :"))
            if opt == 1:
                Admid = input("Enter admin ID :")#Fahad@123
                Admpass = input("Enter password :")#Fahad@1234
                login(Admid,Admpass)
            elif opt == 2:
                signup()
            elif opt == 3:
                Remove()
            if flag == True:
                print("*******************ADMIN PAGE*******************")
                print("i) Add a new product \nii) Update a product \niii) Delete a product \niv) ")
                #Need to complete


