import makeCodes
import makeData
import csvReader


# makes the codes for all the guests in the csv file
def codes_from_file(file_name):

    num_of_guests = len(csvReader.tuplify(file_name))  # get the number of guests from the csv file

    # makes the codes for all the guests, using the makeCodes module
    data = makeData.structify(csvReader.tuplify(file_name))
    codes = []

    for i in range(num_of_guests):
        codes.append(makeCodes.encode(makeData.make_data(data[i])))

    makeCodes.image_all(codes)  # saves the images for all guests in the csv file


# makes the code for a single guest
def codes_from_tuple(input_data):

    data = makeData.struct(input_data[6], input_data[5], input_data[1])

    code = makeCodes.encode(data)
    makeCodes.image(code, input_data[0])  # saves the image with the name being "guest" + the primary key of the guest in George's database


# test function, modify as needed
def test():
    tup = csvReader.tuplify('guests_test2.csv')[0]  # uses the first guest from the csv test file
    print(tup)  # prints the tuple for debugging
    codes_from_tuple(tup)


# main function, modify as needed
def main():
    pass

if __name__ == '__main__':

    test() # run for testing
    main() # run for real for real nocap
