import sqlite3
from datetime import datetime

connection_obj = sqlite3.connect('Database1.db')
cursor_obj = connection_obj.cursor()


def check_check_in(qrcodevalue_uuid):
    cursor_obj.execute("SELECT id FROM GUEST WHERE uuid = ?", (qrcodevalue_uuid,)) #gets the id from guest so it can act as a foreign key
    id = cursor_obj.fetchone()[0]
    cursor_obj.execute("SELECT * FROM CHECK_IN WHERE guest_id = ?", (id,)) #gets that id has already logged in 
    already_entered = cursor_obj.fetchone()
    if already_entered:
        return False
    else:                       #insets the data to say that the user has logged in 
        date = datetime.now()  
        day = datetime.weekday(date)
        cursor_obj.execute("""
INSERT INTO CHECK_IN(guest_id,weekday)
VALUES (?,?)
""", (id,day))
        connection_obj.commit() 
        return True

    
