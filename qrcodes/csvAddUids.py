# writes the extra uid column to the csv input file
import csv
from makeData import make_ids

# adds uuids to the list dat
dat = []
for i in range(3):
    make_ids(dat)


# Function to add a new column named 'uids' to a CSV file
def add_uids_column(input_file, output_file, uids_data):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read the header and add the new column header
        header = next(reader)
        header.append('uids')
        writer.writerow(header)

        # Iterate through each row, add the new column data, and write to output
        for i, row in enumerate(reader):
            row.append(uids_data[i % len(uids_data)])  # Cycling through uids_data if necessary
            writer.writerow(row)

    print(f"File saved to {output_file}")


if __name__ == "__main__":
    
    # Define input and output file paths
    input_file = 'guests_test.csv'  # Replace with actual file path
    output_file = 'guests_test2.csv'  # Replace with desired output file path

    # Add 'uids' column to the CSV file
    add_uids_column(input_file, output_file, dat)
