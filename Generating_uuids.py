import uuid
import json
import sqlite3
 
connection_obj = sqlite3.connect('Database1.db')
 
cursor_obj = connection_obj.cursor()



def uuid_should_go():
    cursor_obj.execute("SELECT * FROM GUEST WHERE uuid IS NULL") #find the next record with no uuid 
    remaining_uuids = cursor_obj.fetchall()
    if remaining_uuids:
        return int(remaining_uuids[0][0]) 
    else:
        return False
    
def make_id(): #makes a uuid

    id = uuid.uuid4()
    return str(id)

def check_id(uuid1): # checks if that uuid already exists
    cursor_obj.execute("SELECT * FROM GUEST WHERE uuid = ?", (uuid1,))
    exists = cursor_obj.fetchone()
    if exists:
        return False
    else:
        return True
    
def add_uuid(uuid1, location):# adds the uuid to the Guest and 
    cursor_obj.execute("UPDATE GUEST SET uuid = ? WHERE id = ?", (uuid1, location)) 
    cursor_obj.execute("SELECT * FROM GUEST WHERE id = ?", (location, ))
    connection_obj.commit() 
    return cursor_obj.fetchone()

def run():
    if uuid_should_go():
        uuid1 = make_id()
        check_id(uuid1)
        location = uuid_should_go()
        return (add_uuid(uuid1,location))








# # creates the structure for the data
# def struct(is_speaker, access, uuid):
#     data = {
#         "is_speaker": is_speaker,
#         "access": access,
#         "uuid": uuid
#     }

#     return data


# # make the tuples from tuplify function into the struct below
# def structify(tuplified_data):
#     result = []
#     for data in tuplified_data:
#         result.append(struct(data[6], data[5], data[1]))
#     return result


# # serializes data in a json format, and returns a list of strings
# def make_data(data):
#     return json.dumps(data)


