import csv
from argparse import ArgumentParser


# allows for arguments to be passed in from the command line
def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        '-f', '--file', help='The csv file to read from', default='guests_test2.csv'
    )
    return parser.parse_args()

# converts the csv file to a load of tuples
def tuplify(filename):
    data_tuples = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_tuple = (
                row['id'],
                row['uuid'],
                row['first_name'],
                row['last_name'],
                row['email'],
                row['access'],
                row['is_speaker'],
                row['created_at']
            )
                
            data_tuples.append(data_tuple)
    return data_tuples

if __name__ == '__main__':
    # Example usage
    args = get_args()
    csv_filename = args.file
    guest_tuples = tuplify(csv_filename)

    # print to check
    for guest in guest_tuples:
        print(guest)
