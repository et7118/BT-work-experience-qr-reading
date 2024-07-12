import makeCode
import makeData
import Generating_uuids

# makes the code for a single guest
def codes_from_tuple(input_data):

    data = makeData.struct(input_data[6], input_data[5], input_data[1])

    code = makeCode.encode(data)
    makeCode.image(code, input_data[0])  # saves the image with the name being "guest" + the primary key of the guest in George's database


# main function, modify as needed
def main():
    tuple = Generating_uuids.run()
    print(tuple)
    codes_from_tuple(tuple)
print('hi')
main()