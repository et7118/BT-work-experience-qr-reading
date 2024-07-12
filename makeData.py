# generates the ids and data that will go in the qr code

import uuid
import json


# creates the structure for the data
def struct(is_speaker, access, uuid):
    data = {
        "is_speaker": is_speaker,
        "access": access,
        "uuid": uuid
    }

    return data  # returns a dictionary


# make the tuples from tuplify function into the struct below
def structify(tuplified_data):
    result = []
    for data in tuplified_data:
        result.append(struct(data[6], data[5], data[1]))
    return result  # returns a list of dictionaries


# serializes data in a json format, and returns string
def make_data(data):
    return json.dumps(data)

