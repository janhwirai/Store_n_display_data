import sqlite3
con=sqlite3.connect("info.db")
c=con.cursor()
print("***********WELCOME***********")
init_data=int(input("Enter 1 to go to Main Options\nEnter 2 to check the Available Data"))

if(init_data==1):
    c.execute("CREATE TABLE info(id int,name text,email text ,mobile int,address text)")

    
    while(True):
        print("Select the following options:-\n")
        print("Enter 1 to Add new data\nEnter 2 to Delete existing data\nEnter 3 to Modify Data\nEnter 4 to Display All Data\nEnter 5 to Exit\n")
        ip=int(input())
        if(ip==1):
            print("***ADD NEW DATA***")
            n=int(input("No. of data to enter:-"))
            print("\nEnter Data:-\n")
            for i in range(n):
                info_id=int(input("\nEnter ID:"))
                c.execute("SELECT id FROM info")
                pres_id=c.fetchall()
                pres_id=[i[0] for i in pres_id]
                if (info_id in pres_id):
                    print("ID already taken!")
                else:
                    info_name=input("\nEnter Name:")
                    info_email=input("\nEnter E-Mail Id:")
                    info_mobile=input("\nEnter Mobile number:")
                    info_address=input("\nEnter Address:")
                    c.execute("""INSERT INTO info(id,name,email,mobile,address) 
                                VALUES(?,?,?,?,?)""",(info_id,info_name,info_email,info_mobile,info_address))
                    con.commit()
                    print("\nData Added Successfully!")

        elif(ip==2):
            print("***DELETE DATA***")
            del_id=int(input("\nEnter ID to delete it's data:\n"))
            c.execute("DELETE FROM info WHERE id= (?) ",(del_id,))
            con.commit()

        elif(ip==3):
            print("***MODIFY DATA***")
            modify_id=int(input("Enter ID to modify it's data:\n"))
            while(True):
                print("Enter 1 modify ID\nEnter 2 to modify Name\nEnter 3 to Modify email\nEnter 4 to Modify Mobile\nEnter 5 to address\nEnter 6 to Exit")
                da=int(input())
                if(da==1):
                    mod_id=input("Enter new id")
                    c.execute("UPDATE info SET id= (?) WHERE id = (?) ",(mod_id, modify_id))
                    con.commit()
                elif(da==2):
                    mod_name=input("Enter new Name")
                    c.execute("UPDATE info SET name=(?) WHERE id = (?) ", (mod_name,modify_id))
                    con.commit()
                elif(da==3):
                    mod_email=input("Enter new email")
                    c.execute("UPDATE info SET email=(?) WHERE id = (?) ", (mod_email,modify_id))
                    con.commit()
                elif(da==4):
                    mod_mobile=input("Enter new mobile number")
                    c.execute("UPDATE info SET mobile= (?) WHERE id = (?) ", (mod_mobile,modify_id))
                    con.commit()
                elif(da==5):
                    mod_address=input("Enter new address")
                    c.execute("UPDATE info SET address= (?) WHERE id = (?) " , (mod_address,modify_id))
                    con.commit()
                elif(da==6):
                    print("Done Modifying Data")
                    break
        elif(ip==4):
            print("***Display Data***")
            c.execute("SELECT * FROM info ")
            result=c.fetchall()
            for a in result:
                print("ID ",a[0])
                print("NAME ",a[1])
                print("E-MAIL ID ",a[2])
                print("MOBILE NUMBER ",a[3])
                print("ADDRESS ",a[4])
                print("\n")
            con.commit()
        elif(ip==5):
            break

if (init_data==2):
    avail_id=int(input("Enter ID: "))
    c.execute("SELECT id FROM info")
    check_id=c.fetchall()
    check_id=[i[0] for i in check_id]
    if (avail_id in check_id):
        c.execute("SELECT * FROM info where id=(?) " , (avail_id,))
        res=c.fetchall()
        for r in res:
            print("ID ",r[0])
            print("NAME ",r[1])
            print("E-MAIL ID ",r[2])
            print("MOBILE NUMBER ",r[3])
            print("ADDRESS ",r[4])
        con.commit()
    else:
        print("ID Not Available!")
print("***********Thank You***********")
con.close()