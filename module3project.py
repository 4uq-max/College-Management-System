'''
Created on 15-Aug-2017

@author: Dishant
'''
import cx_Oracle
from _overlapped import NULL
connection = cx_Oracle.connect('system/2314022@Localhost/XE')
cursor1 = connection.cursor()
cursor2 = connection.cursor()

while True:
    mainmenu=input("*****************MAIN MENU****************\n1. New User\n2. Log-in\n3. Change Password\n4. Exit\n")
    if mainmenu == "1":
        
        userid=input("Enter your Faculty ID or Roll No\n")
        if(userid.isdigit()):
            cursor1.execute("""SELECT * FROM MODULE3.STUDENTDB WHERE ROLLNO= :param1""",{'param1':userid})
            cursor1.fetchall()
            
        else:
            cursor2.execute("""SELECT * FROM MODULE3.FACULTYDB WHERE FACULTY_ID= : param1""",{'param1':userid})   
            cursor2.fetchall() 
        
        if(cursor1.rowcount==1 or cursor2.rowcount==1):
            password=input("Enter Password\n")
            cursor1.execute("INSERT INTO MODULE3.USERDB VALUES (:userid1 ,:password1)",{
            'userid1' : userid,
            'password1' : password,
            })
            connection.commit()
    
            print("A new user has been successfully created")
        else:
            print("Roll No. or Faculty ID does not exist")

    elif mainmenu == "2":
        
        userid3=input("Enter your Faculty ID or Roll No.\n")
        if(userid3.isdigit()):
            cursor1.execute("""SELECT * FROM MODULE3.STUDENTDB WHERE RollNo=:param1""",{'param1':userid3})
            variable4=cursor1.fetchall()
            if(cursor1.rowcount==1):
                usermenu="4"
            else:
                usermenu=NULL
                print("Student not found")
            
        else:
            cursor2.execute("""SELECT * FROM MODULE3.FACULTYDB WHERE FACULTY_ID= : param3""",{'param3':userid3})
            variable3=cursor2.fetchall()
            if(cursor2.rowcount==1):
                if(variable3[0][3]=="Principal"):
                    usermenu="1"
                elif(variable3[0][3]=="HOD"):
                    usermenu="2"
                elif(variable3[0][3]=="Faculty"):
                    usermenu="3"
            else:
                usermenu=NULL
                print("User not found")
        if usermenu == "1":
            password6=input("Enter your password\n")
            cursor2.execute("""SELECT PASSWORD FROM MODULE3.USERDB WHERE USERID= : param1""",{'param1' :userid3})
            variable13=cursor2.fetchall()
            
            if(variable13[0][0]==password6):
                while True:
                    submenu1=input("******** Welcome Dr. Amit Wason *********\n1. Student Maintenance\n2. Faculty Maintenance\n3. Output\n4. Logout\n")
                    if submenu1=="1":
                        while True:
                            functionmenu11=input("********Student Maintenance***********\n1. Add new student\n2. Modify Student Detail\n3. Delete Student\n4. Back\n")
                            if(functionmenu11=="1"):
                                rollNo=input("Enter the Roll No. of student\n")
                                name=input("Enter the Name of student\n")
                                fatherName=input("Enter the Father's Name of student\n")
                                address=input("Enter the Address of student\n")
                                phoneNo=input("Enter the Phone No. of student\n")
                                emailId=input("Enter the Email ID of student\n")
                                pcmMarks=input("Enter the aggregate marks in PCM\n")
                                branch=input("Enter the Branch to which student belongs\n")
                                cursor1.execute("INSERT INTO MODULE3.STUDENTDB VALUES (:rollNo,:name,:fatherName,:address,:phoneNo,:emailId,:pcmMarks,:branch)",{
                                    'rollNo' : rollNo,
                                    'name'   : name,
                                    'fatherName' : fatherName,
                                    'address':address,
                                    'phoneNo':phoneNo,
                                    'emailId':emailId,
                                    'pcmMarks': pcmMarks,
                                    'branch':branch
                                    })
                                connection.commit()
                                print("Student added successfully")
                            elif functionmenu11=="2":
                                rollNo1=input("Enter student Roll No.\n")
                                cursor1.execute("""SELECT * FROM MODULE3.STUDENTDB WHERE RollNo= :param1""",{'param1': rollNo1})
                                studentdb=cursor1.fetchall()
                                if(cursor1.rowcount==1):
                                    print(*studentdb[0], sep='  ')
                                    rollNo=input("Enter the Roll No. of student\n")
                                    name=input("Enter the Name of student\n")
                                    fatherName=input("Enter the Father's Name of student\n")
                                    address=input("Enter the Address of student\n")
                                    phoneNo=input("Enter the Phone No. of student\n")
                                    emailId=input("Enter the Email ID of student\n")
                                    pcmMarks=input("Enter the aggregate marks in PCM\n")
                                    branch=input("Enter the Branch to which student belongs\n")
                                    cursor1.execute("""UPDATE MODULE3.STUDENTDB SET RollNo= :param1,NAME= :param2,FATHERNAME= :param3,ADDRESS= :param4,PHONENO= :param5,EMAILID= :param6,MARKS_PCM= :param7,BRANCH= :param8 WHERE RollNo= :param9""",{'param1': rollNo,'param2': name,'param3': fatherName,'param4': address,'param5': phoneNo,'param6': emailId,'param7':pcmMarks ,'param8': branch,'param9': rollNo1})
                                    connection.commit()
                                    print("Details modified Successfully")
                                else:
                                    print("Student not found")
                            elif functionmenu11=="3":
                                rollNo2=input("Enter student Roll No.\n")
                                cursor1.execute("""SELECT * FROM MODULE3.STUDENTDB WHERE RollNo= :param1""",{'param1': rollNo2})
                                studentdb=cursor1.fetchall()
                                if(cursor1.rowcount==1):
                                    print(*studentdb[0], sep='  ')
                                    confirmation=input("Are you sure you want to delete the records for this student...Press 1 for confirmation\n")
                                    if(confirmation=="1"):
                                        cursor2.execute("""DELETE FROM MODULE3.STUDENTDB WHERE ROLLNO= :param1""",{'param1':rollNo2})
                                        connection.commit()
                                        print("Student details have been deleted successfully")
                                    else:
                                        print("Student details deletion unsuccessful")
                                else:
                                    print("Student not found")
                            elif functionmenu11=="4":
                                break
                    elif submenu1=="2":
                        while True:
                            functionmenu21=input("**********Faculty Maintenance**********\n1. Add new Faculty\n2. Modify Faculty Detail\n3. Delete Faculty\n4. Back\n")
                            if(functionmenu21=="1"):
                                facultyID=input("Enter the Faculty ID of faculty\n")
                                name=input("Enter the Name of faculty\n")
                                address=input("Enter the Address of faculty\n")
                                designation=input("Enter the Designation of faculty\n")
                                department=input("Enter the department of faculty\n")
                                phoneNo=input("Enter the Phone No. of faculty\n")
                                experience=input("Enter the Experience of faculty\n")
                                favoriteSubjects=input("Enter the Favorite Subjects of faculty\n")
                                cursor1.execute("INSERT INTO MODULE3.FACULTYDB VALUES (:facultyID,:name,:address,:designation,:department,:phoneNo,:experience,:favoriteSubjects)",{
                                    'facultyID' : facultyID,
                                    'name'   : name,
                                    'address' : address,
                                    'designation':designation,
                                    'department':department,
                                    'phoneNo':phoneNo,
                                    'experience': experience,
                                    'favoriteSubjects':favoriteSubjects
                                    })
                                connection.commit()
                                print("Faculty added successfully")
                            elif functionmenu21=="2":
                                facultyID1=input("Enter the Faculty ID of faculty\n")
                                cursor2.execute("""SELECT * FROM MODULE3.FACULTYDB WHERE FACULTY_ID= :param1""",{'param1': facultyID1})
                                facultydb=cursor2.fetchall()
                                if(cursor2.rowcount==1):
                                    print(*facultydb[0], sep='  ')
                                    facultyID=input("Enter the Faculty ID of faculty\n")
                                    name=input("Enter the Name of faculty\n")
                                    address=input("Enter the Address of faculty\n")
                                    designation=input("Enter the Designation of faculty\n")
                                    department=input("Enter the department faculty\n")
                                    phoneNo=input("Enter the Phone No. of faculty\n")
                                    experience=input("Enter the Experience of faculty\n")
                                    favouriteSubjects=input("Enter the Favorite Subjects of faculty\n")
                                    cursor2.execute("""UPDATE MODULE3.FACULTYDB SET FACULTY_ID= :param1,NAME= :param2,ADDRESS= :param3,DESIGNATION= :param4,DEPARTMENT= :param5,PHONENO= :param6,EXPERIENCE= :param7,FAVORITESUBJECTS= :param8 WHERE FACULTY_ID= :param9""",{'param1': facultyID,'param2': name,'param3': address,'param4': designation,'param5': department,'param6': phoneNo,'param7': experience,'param8':favouriteSubjects,'param9': facultyID1})
                                    connection.commit()
                                    print("Details modified Successfully")
                                else:
                                    print("User not found")
                            elif functionmenu21=="3":
                                facultyID2=input("Enter Faculty ID \n")
                                cursor2.execute("""SELECT * FROM MODULE3.FACULTYDB WHERE FACULTY_ID= :param1""",{'param1': facultyID2})
                                facultydb=cursor2.fetchall()
                                if(cursor2.rowcount==1):
                                    print(*facultydb[0], sep='  ')
                                    confirmation=input("Are you sure you want to delete the records for this student...Press 1 for confirmation\n")
                                    if(confirmation=="1"):
                                        cursor2.execute("""DELETE FROM MODULE3.FACULTYDB WHERE FACULTY_ID= :param1""",{'param1':facultyID2})
                                        connection.commit()
                                        print("Faculty details have been deleted successfully")  
                                    else:
                                        print("Faculty details deletion unsuccessful")
                                else:
                                    print("User not found")
                            elif functionmenu21=="4":
                                break
                    elif submenu1=="3":
                        while True:
                            functionmenu31=input("************OUTPUT**************\n1. List of all Students\n2. List of students department wise\n3. Details of particular student\n4. Three toppers department wise\n5. List of all faculty\n6. List of faculty department wise\n7. My profile\n8. Back\n")
                            if functionmenu31=="1":
                                cursor1.execute("""SELECT NAME FROM MODULE3.STUDENTDB""")
                                value4=cursor1.fetchall()
                                for i in range(0,cursor1.rowcount):
                                    print(value4[i][0])
                            elif functionmenu31=="2":
                                cursor1.execute("""SELECT NAME FROM MODULE3.STUDENTDB WHERE BRANCH= :param1""",{'param1':'CSE'})
                                print("Students of CSE:\n")
                                value5=cursor1.fetchall()
                                for i in range(0,cursor1.rowcount):
                                    print(value5[i][0])
                                cursor1.execute("""SELECT NAME FROM MODULE3.STUDENTDB WHERE BRANCH= :param1""",{'param1':'ME'})
                                print("Students of ME:\n")
                                value5=cursor1.fetchall()
                                for i in range(0,cursor1.rowcount):
                                    print(value5[i][0])
                                cursor1.execute("""SELECT NAME FROM MODULE3.STUDENTDB WHERE BRANCH= :param1""",{'param1':'ECE'})
                                print("Students of ECE:\n")
                                value5=cursor1.fetchall()
                                for i in range(0,cursor1.rowcount):
                                    print(value5[i][0])
                                cursor1.execute("""SELECT NAME FROM MODULE3.STUDENTDB WHERE BRANCH= :param1""",{'param1':'BT'})
                                print("Students of BT:\n")
                                value5=cursor1.fetchall()
                                for i in range(0,cursor1.rowcount):
                                    print(value5[i][0])
                            elif functionmenu31=="3":
                                rollNo3=input("Enter the roll no of student\n")
                                cursor1.execute("""SELECT * FROM MODULE3.STUDENTDB WHERE RollNo= :param1""",{'param1':rollNo3})
                                value6=cursor1.fetchall()
                                if(cursor1.rowcount==1):
                                    print(*value6[0], sep='  ')
                                else:
                                    print("Student not found")
                            elif functionmenu31=="4":   
                                cursor1.execute("""SELECT NAME FROM(SELECT * FROM MODULE3.STUDENTDB ORDER BY MARKS_PCM DESC) WHERE BRANCH= :param1 AND ROWNUM<=3 ORDER BY MARKS_PCM DESC""",{'param1':'CSE'}) 
                                print("Toppers of CSE:\n")
                                value7=cursor1.fetchall()
                                for i in range(0,cursor1.rowcount):
                                    print(value7[i][0])
                                cursor1.execute("""SELECT NAME FROM(SELECT * FROM MODULE3.STUDENTDB ORDER BY MARKS_PCM DESC) WHERE BRANCH= :param1 AND ROWNUM<=3 ORDER BY MARKS_PCM DESC""",{'param1':'ME'}) 
                                print("Toppers of ME:\n")
                                value7=cursor1.fetchall()
                                for i in range(0,cursor1.rowcount):
                                    print(value7[i][0])
                                cursor1.execute("""SELECT NAME FROM(SELECT * FROM MODULE3.STUDENTDB ORDER BY MARKS_PCM DESC) WHERE BRANCH= :param1 AND ROWNUM<=3 ORDER BY MARKS_PCM DESC""",{'param1':'ECE'}) 
                                print("Toppers of ECE:\n")
                                value7=cursor1.fetchall()
                                for i in range(0,cursor1.rowcount):
                                    print(value7[i][0])
                                cursor1.execute("""SELECT NAME FROM(SELECT * FROM MODULE3.STUDENTDB ORDER BY MARKS_PCM DESC) WHERE BRANCH= :param1 AND ROWNUM<=3 ORDER BY MARKS_PCM DESC""",{'param1':'BT'}) 
                                print("Toppers of BT:\n")
                                value7=cursor1.fetchall()
                                for i in range(0,cursor1.rowcount):
                                    print(value7[i][0])
                            elif functionmenu31=="5":
                                cursor2.execute("""SELECT NAME FROM MODULE3.FACULTYDB""")
                                value9=cursor2.fetchall()  
                                for i in range(0,cursor2.rowcount):
                                    print(value9[i][0])
                            elif functionmenu31=="6":   
                                cursor2.execute("""SELECT NAME FROM MODULE3.FACULTYDB WHERE DEPARTMENT= :param1""",{'param1':'CSE'})
                                print("Faculty of CSE:\n")
                                value8=cursor2.fetchall()
                                for i in range(0,cursor2.rowcount):
                                    print(value8[i][0])
                                cursor2.execute("""SELECT NAME FROM MODULE3.FACULTYDB WHERE DEPARTMENT= :param1""",{'param1':'ME'})
                                print("Faculty of ME:\n")
                                value8=cursor2.fetchall()
                                for i in range(0,cursor2.rowcount):
                                    print(value8[i][0])
                                cursor2.execute("""SELECT NAME FROM MODULE3.FACULTYDB WHERE DEPARTMENT= :param1""",{'param1':'ECE'})
                                print("Faculty of ECE:\n")
                                value8=cursor2.fetchall()
                                for i in range(0,cursor2.rowcount):
                                    print(value8[i][0])
                                cursor2.execute("""SELECT NAME FROM MODULE3.FACULTYDB WHERE DEPARTMENT= :param1""",{'param1':'BT'})
                                print("Faculty of BT:\n")
                                value8=cursor2.fetchall()
                                for i in range(0,cursor2.rowcount):
                                    print(value8[i][0])
                            elif functionmenu31=="7":
                                cursor2.execute("""SELECT * FROM MODULE3.FACULTYDB WHERE FACULTY_ID= : param1""",{'param1':userid3})   
                                value10=cursor2.fetchall()
                                print(*value10[0], sep='  ') 
                            elif functionmenu31=="8":
                                break
                    elif submenu1=="4":
                        break
            else:
                print("Wrong Password")   
        elif usermenu == "2":
            department=variable3[0][4]
            password7=input("Enter your password\n")
            cursor2.execute("""SELECT PASSWORD FROM MODULE3.USERDB WHERE USERID= : param1""",{'param1' :userid3})
            variable14=cursor2.fetchall()
            if(variable14[0][0]==password7):
                while True:
                    cursor2.execute("""SELECT NAME FROM MODULE3.FACULTYDB WHERE DEPARTMENT=:param1 AND DESIGNATION='HOD'""",{'param1':department})
                    value1=cursor2.fetchall()
                    print("************Welcome",value1[0][0],"***********")
                    print("1. List of all ",department," Student\n2. Detail of a student\n3. Three toppers of ",department," department\n4.",department,"Faculty List\n5. My Profile\n6. Log out\n")
                    submenu2=input()
                    if submenu2=="1":
                        cursor1.execute("""SELECT NAME FROM MODULE3.STUDENTDB WHERE BRANCH= :param1""",{'param1':department})
                        value11=cursor1.fetchall()
                        for i in range(0,cursor1.rowcount):
                                    print(value11[i][0])
                    elif submenu2=="2":
                        rollNo4=input("Enter the Roll No. of student\n")
                        cursor1.execute("""SELECT * FROM MODULE3.STUDENTDB WHERE RollNo= :param1 AND BRANCH= :param2""",{'param1':rollNo4,'param2':department})
                        value11=cursor1.fetchall()
                        if(cursor1.rowcount==1):
                            print(*value11[0], sep='  ') 
                        else:
                            print("Student not found")
                    elif submenu2=="3":
                        cursor1.execute("""SELECT NAME FROM(SELECT * FROM MODULE3.STUDENTDB ORDER BY MARKS_PCM DESC) WHERE BRANCH= :param1 AND ROWNUM<=3 ORDER BY MARKS_PCM DESC""",{'param1':department}) 
                        print("Three Toppers of",department)
                        value11=cursor1.fetchall()
                        for i in range(0,cursor1.rowcount):
                                    print(value11[i][0])
                    elif submenu2=="4":
                        cursor2.execute("""SELECT NAME FROM MODULE3.FACULTYDB WHERE (DEPARTMENT= :param1) AND (DESIGNATION= 'HOD' OR DESIGNATION='Faculty')""",{'param1':department})
                        value11=cursor2.fetchall()
                        for i in range(0,cursor2.rowcount):
                                    print(value11[i][0])
                    elif submenu2=="5": 
                        cursor2.execute("""SELECT * FROM MODULE3.FACULTYDB WHERE FACULTY_ID= : param1""",{'param1':userid3})   
                        value11=cursor2.fetchall()
                        print(*value11[0], sep='  ')  
                    elif submenu2=="6":
                        break
            else:
                print("Wrong Password")        
        elif usermenu == "3":
            departmentFaculty=variable3[0][4]
            password8=input("Enter your password\n")
            cursor2.execute("""SELECT PASSWORD FROM MODULE3.USERDB WHERE USERID= : param1""",{'param1' :userid3})
            variable15=cursor2.fetchall()
            if(variable15[0][0]==password8):
                while True:
                    cursor2.execute("""SELECT NAME FROM MODULE3.FACULTYDB WHERE DEPARTMENT=:param1 AND DESIGNATION='Faculty'""",{'param1':departmentFaculty})
                    value2=cursor2.fetchall()
                    print("************Welcome Er.",value2[0][0],"***********")
                    print("1. Students of",departmentFaculty,"department\n2. A particular student of",departmentFaculty,"department.\n3. My Profile\n4. Logout\n")
                    submenu3=input()
                    if submenu3=="1":
                        cursor1.execute("""SELECT NAME FROM MODULE3.STUDENTDB WHERE BRANCH= :param1""",{'param1':departmentFaculty})
                        value14=cursor1.fetchall()
                        for i in range(0,cursor1.rowcount):
                                    print(value14[i][0])
                    elif submenu3=="2":
                        rollNo5=input("Enter the Roll No. of student\n")
                        cursor1.execute("""SELECT * FROM MODULE3.STUDENTDB WHERE RollNo= :param1 AND BRANCH= :param2""",{'param1':rollNo5,'param2':departmentFaculty})
                        value12=cursor1.fetchall()
                        if(cursor1.rowcount==1):
                            print(*value12[0], sep='  ')
                        else:
                            print("Student not found")
                    elif submenu3=="3":
                        cursor2.execute("""SELECT * FROM MODULE3.FACULTYDB WHERE FACULTY_ID= : param1""",{'param1':userid3})   
                        value12=cursor2.fetchall()
                        print(*value12[0], sep='  ') 
                    elif submenu3=="4":
                        break
            else:
                print("Wrong Password")          
        elif usermenu == "4":
            
            branchStudent=variable4[0][7]
            password5=input("Enter your password\n")
            cursor1.execute("""SELECT PASSWORD FROM MODULE3.USERDB WHERE USERID= : param1""",{'param1' :userid3})
            variable2=cursor1.fetchall()
            if(variable2[0][0]==password5):
                while True:
                    cursor1.execute("""SELECT NAME FROM MODULE3.STUDENTDB WHERE BRANCH=:param1""",{'param1':branchStudent})
                    value3=cursor1.fetchall()
                    print("************Welcome",value3[0][0],"***********\n")
                    print("1. List of Faculty of ",branchStudent," department\n2. My Profile \n3. Logout\n")
                    submenu4=input()
                    if(submenu4=="1"):
                        cursor2.execute("""SELECT NAME FROM MODULE3.FACULTYDB WHERE DEPARTMENT= :param1""",{'param1': branchStudent})
                        value13=cursor2.fetchall()
                        for i in range(0,cursor2.rowcount):
                            print(value13[i][0])
                    elif(submenu4=="2"):
                        cursor1.execute("""SELECT * FROM MODULE3.STUDENTDB WHERE RollNo= :param1""",{'param1': userid3})
                        value13=cursor1.fetchall()
                        print(*value13[0], sep='  ')
                    elif(submenu4=="3"):
                        break
            else:
                print("Wrong Password")    
    elif mainmenu == "3":
        userid2=input("Enter your Faculty ID or Roll No\n")
        if(userid2.isdigit()):
            cursor1.execute("""SELECT * FROM MODULE3.STUDENTDB WHERE ROLLNO= :param1""",{'param1':userid2})
            cursor1.fetchall() 
        else:
            cursor2.execute("""SELECT * FROM MODULE3.FACULTYDB WHERE FACULTY_ID= : param1""",{'param1':userid2})   
            cursor2.fetchall() 
            print(cursor2.rowcount)
        
        if(cursor1.rowcount==1 or cursor2.rowcount==1):
            password2=input("Enter Existing Password\n")
            cursor1.execute("""SELECT PASSWORD FROM MODULE3.USERDB WHERE USERID= : param1""",{'param1' :userid2})
            variable=cursor1.fetchall()
            
            if(variable[0][0]==password2):
                password3=input("Enter New Password\n")
                password4=input("Confirm New Password\n")
                if(password3==password4):
                    cursor1.execute("""UPDATE MODULE3.USERDB SET PASSWORD = :param1 WHERE USERID= :param2""",{'param1': password3,'param2': userid2})
                    connection.commit()
                    print("Your password has been successfully changed")
                else:
                    print("Password mismatch")
            else:
                print("Authentication Failed")
        else:
            print("Roll No or Faculty ID does not exist")
            
    elif mainmenu == "4":    
        print("Thank You! Have a nice day")
        break   
connection.close()    