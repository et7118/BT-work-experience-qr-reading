# generates the ids and data that will go in the qr code

import uuid
import json


# makes the ids and appends them to list l_ids
def make_ids(ids):
    id = uuid.uuid4()
    ids.append(id)
    print('Your UUID is: ' + str(id))


# creates the structure for the data as follows:
# example_data = {
#     "is_speaker": False,
#     "access": True,
#     "id": "e3ad8836-fdde-46ae-a983-dedd45a09880"
# }
def struct(is_speaker, access, id):
    data = {
        "is_speaker": is_speaker,
        "access": access,
        "id": id
    }
    return data


def make_data(data):
    data_string = json.dumps(data)
    return data_string
