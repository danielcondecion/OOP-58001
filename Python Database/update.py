import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Daniel\Documents\College\Object Oriented Programming\FINALS\database\Python Database\Database2.accdb;')
    print("Connected to a Database")

    Fullname = "Condecion, Daniel M."
    Assignment = 98
    Laboratory = 95
    Quiz = 99
    Exam = 99
    user_id = 9

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Fullname = ? WHERE id=?', (Fullname, user_id))
    record.execute('UPDATE Table1 SET Assignment = ? WHERE id=?', (Assignment, user_id))
    record.execute('UPDATE Table1 SET Laboratory = ? WHERE id=?', (Laboratory, user_id))
    record.execute('UPDATE Table1 SET Quiz = ? WHERE id=?', (Quiz, user_id))
    record.execute('UPDATE Table1 SET Exam = ? WHERE id=?', (Exam, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")
