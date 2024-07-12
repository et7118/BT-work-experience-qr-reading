import sqlite3

connection_obj = sqlite3.connect('Database1.db')
cursor_obj = connection_obj.cursor()



def check_qr(qrcodevalue):
    cursor_obj.execute("SELECT first_name, access, is_speaker FROM GUEST WHERE uuid = ?", (qrcodevalue['uuid'],))
    Guest_table_info = cursor_obj.fetchone()
    if Guest_table_info:

        if Guest_table_info[2] == qrcodevalue['is_speaker'] and Guest_table_info[1] == qrcodevalue['access']:
            return [True,('Hello '+ Guest_table_info[0])]
        else:
            return [False,('incorect1')]
    else:
        return [False,('incorect')]

    connection_obj.close()

#qrcodevalue = {'is_speaker': 0, 'access': 0, 'uuid': '123e4567-e89b-12d3-a456-426614174001'}

#print(check_qr(qrcodevalue))