import sqlite3
 
connection_obj = sqlite3.connect('Database1.db')
 
cursor_obj = connection_obj.cursor()
 
cursor_obj.execute("DROP TABLE IF EXISTS GUEST")
cursor_obj.execute("DROP TABLE IF EXISTS CHECK_IN")
 

Guest_table = """ CREATE TABLE GUEST(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uuid CHAR(36),
            first_name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            email VARCHAR(40) NOT NULL,
            access INTEGER NOT NULL CHECK(access IN (0, 1)),
            is_speaker INTEGER DEFAULT 0 CHECK(is_speaker IN (0, 1)),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """
 
Check_in_table = """
CREATE TABLE CHECK_IN (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_id INTEGER,
    weekday INTEGER CHECK(weekday IN (0, 1, 2, 3, 4, 5, 6)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (guest_id) REFERENCES GUEST(id)
);
"""

cursor_obj.execute(Guest_table)
print('hi')
cursor_obj.execute(Check_in_table)
print("Done")



data  =[('123e4567-e89b-12d3-a456-426614174000','John','Doe','john.doe@example.com',1), 
('123e4567-e89b-12d3-a456-426614174001','Jane','Doe','jane.doe@example.com',0),
('123e4567-e89b-12d3-a456-426614174002','Jim','Beam','jim.beam@example.com',1),
('123e4567-e89b-12d3-a456-426614174003','Jill','Hill','jill.hill@example.com',0),
('123e4567-e89b-12d3-a456-426614174004','Jack','Hill','jack.hill@example.com',1),
]


cursor_obj.executemany("""
INSERT INTO GUEST(uuid,first_name,last_name,email,access)
VALUES (?, ?, ?, ?, ?)
""", data)




cursor_obj.execute("""
INSERT INTO GUEST(first_name,last_name,email,access)
VALUES ('barry', 'blevins', 'barry@h4rrym8.com', 1)
""")
cursor_obj.execute("""
INSERT INTO GUEST(first_name,last_name,email,access)
VALUES ('Larry', 'Llevins', 'Larry@h4rrym8.com', 1)
""")





data = [
    (3, 4),
    (2, 0)
]

cursor_obj.executemany("""
INSERT INTO CHECK_IN(guest_id, weekday)
VALUES (?, ?)
""", data)
connection_obj.commit()



cursor_obj.execute("SELECT * FROM GUEST")
Guest_table_info = cursor_obj.fetchall()
for column in Guest_table_info:
    print(column)

cursor_obj.execute("SELECT * FROM GUEST WHERE id = 1")
Guest_table_info = cursor_obj.fetchall()
for column in Guest_table_info:
    print(column)
cursor_obj.execute("SELECT * FROM GUEST WHERE uuid IS NULL")
Guest_table_info = cursor_obj.fetchall()
for column in Guest_table_info:
    print(column)

cursor_obj.execute("SELECT * FROM CHECK_IN")
Guest_table_info = cursor_obj.fetchall()
for column in Guest_table_info:
    print(column)


connection_obj.close()